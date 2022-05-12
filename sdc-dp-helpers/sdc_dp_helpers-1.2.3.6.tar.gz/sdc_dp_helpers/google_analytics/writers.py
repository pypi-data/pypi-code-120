"""
    CUSTOM WRITER CLASSES
        - Class which manages writer tasks like
        auth, write metadata, write file, create dir structure
"""
import gzip
import io
import json
import os

import boto3
from interface import implements

from sdc_dp_helpers.base_writer import BaseWriter, CustomLocalJsonWriter


class GAV3Writer:
    def __init__(self, bucket, folder_path, profile_name=None):
        if profile_name is None:
            self.boto3_session = boto3.Session()
        else:
            self.boto3_session = boto3.Session(profile_name=profile_name)
        self.s3_resource = self.boto3_session.resource("s3")
        self.bucket = bucket
        self.folder_path = folder_path

    @staticmethod
    def _partition_by_date(dataset, date_key):
        partition_dataset = {}
        for row in dataset:
            date_value = row.get(date_key)

            if date_value not in partition_dataset:
                partition_dataset[date_value] = []
            partition_dataset[date_value].append(row)

        return partition_dataset

    @staticmethod
    def _partition_by_profile(dataset):
        partition_dataset = {}
        for row in dataset:
            date_value = row.get("profileId")

            if date_value not in partition_dataset:
                partition_dataset[date_value] = []
            partition_dataset[date_value].append(row)

        return partition_dataset

    def write_partitions_to_s3(self, dataset, date_key="ga:date"):
        """
        If we pull data over a period of time for the same dimensions, we will
        begin to see discrepancies in the data.

        This is because the sampling means that if we pull one set of data on different
        days, the metrics might be slightly different, and we end up with duplication.

        So the plan is to ensure that if we:
            - pull from a specific date, we overwrite all that days data in the buckets.
            - this way, we ensure all data is original and in its most updated state.
        """
        data_by_view_id = self._partition_by_profile(dataset)
        for view_id, view_id_dataset in data_by_view_id.items():
            data_by_date = self._partition_by_date(view_id_dataset, date_key=date_key)
            for date, date_dataset in data_by_date.items():
                write_path = f"{self.folder_path}/{view_id}/{date}.json"
                print(
                    f"Writing data to s3://{write_path} partitioned by view_id and date."
                )
                self.s3_resource.Object(self.bucket, write_path).put(
                    Body=json.dumps(date_dataset)
                )


class CustomS3GZJsonWriter(CustomLocalJsonWriter, implements(BaseWriter)):
    """Class Extends Basic LocalGZJsonWriter"""

    def __init__(
        self,
        file_name: str,
        folder_path: str,
        bucket: str,
        profile_name: str = None,
        **kwargs,
    ):
        self.os_path_sep = "/"

        if profile_name is None:
            self.boto3_session = boto3.Session()
        else:
            self.boto3_session = boto3.Session(profile_name=profile_name)

        self.bucket = bucket
        """Writes a general object to s3"""
        self.s3_resource = self.boto3_session.resource("s3")
        super().__init__(file_name=file_name, folder_path=folder_path, **kwargs)
        self.metadata_file = kwargs.get("metadata_file", "metadata.json.gz")

    def set_full_path(self, nested_dirs: list = None):
        """Set full path to write to"""
        # creates full path
        full_path = [self.folder_path] + nested_dirs
        return os.path.join(*full_path).replace("\\", "/")

    # pylint: disable=no-member,too-many-arguments
    def write_to_s3(
        self,
        json_data,
        data_path,
        mode="w",
        encoding="utf-8",
        ensure_ascii=False,
        default=None,
    ):
        """
        Write report to s3 bucket
        """
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode=mode) as file_:
            with io.TextIOWrapper(file_, encoding=encoding) as textio_obj:
                textio_obj.write(
                    json.dumps(json_data, ensure_ascii=ensure_ascii, default=default)
                )
        # write to s3
        buffer.seek(0)
        self.s3_resource.Bucket(self.bucket).put_object(
            Key=os.path.join(self.full_path, data_path).replace("\\", "/"), Body=buffer
        )

    def write_metadata(self, metadata: dict):
        """ "
        Creates required GA/ViewID/metricName structure
        """
        # create directory structure if not exists
        self.full_path = self.set_full_path(
            nested_dirs=[metadata.get("viewID", "."), metadata.get("metricName", "")]
        )
        self.write_to_s3(json_data=metadata, data_path=self.metadata_file, mode="w")

    def write_file(self):
        """
        upload python dict into s3 bucket with gzip archive
        """
        # generate a unix timestamp suffix for file
        suff = self.timestamp_suffix()
        data_path = "{}_{}.json.gz".format(self.file_name, suff)
        self.write_to_s3(self.data, data_path, mode="wb")
        self.data = []
