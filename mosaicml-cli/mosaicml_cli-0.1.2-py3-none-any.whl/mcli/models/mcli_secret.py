""" MCLI Abstraction for Secrets """
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Type, Union

import yaml

from mcli.models import MCLIPlatform
from mcli.serverside.job.mcli_k8s_job import MCLIK8sJob
from mcli.utils.utils_kube import base64_decode, base64_encode, read_secret
from mcli.utils.utils_kube_labels import label
from mcli.utils.utils_serializable_dataclass import SerializableDataclass, T_SerializableDataclass

SECRET_MOUNT_PATH_PARENT = Path('/etc/secret')


class SecretType(Enum):
    """ Enum for Types of Secrets Allowed """
    docker_registry = 'docker_registry'
    ssh = 'ssh'
    generic = 'generic'
    mounted = 'mounted'
    generic_mounted = 'generic_mounted'
    environment = 'environment'
    generic_environment = 'generic_environment'
    s3_credentials = 's3_credentials'

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def ensure_enum(cls, val: Union[str, SecretType]) -> SecretType:
        if isinstance(val, str):
            return SecretType[val]
        elif isinstance(val, SecretType):
            return val
        raise ValueError(f'Unable to ensure {val} is a SecretType Enum')


DEPRECATED_SECRETS: Dict[SecretType, SecretType] = {
    SecretType.generic_environment: SecretType.environment,
    SecretType.generic_mounted: SecretType.mounted,
}


@dataclass
class MCLISecret(SerializableDataclass, ABC):
    """
    The Base Secret Class for MCLI Secrets

    Secrets can not nest other SerializableDataclass objects
    """

    name: str
    secret_type: SecretType

    @property
    def kubernetes_type(self) -> str:
        """The corresponding Kubernetes secret type for this class of secrets
        """
        return 'Opaque'

    @abstractmethod
    def add_to_job(self, kubernetes_job: MCLIK8sJob) -> bool:
        """Add a secret to a job
        """

    @property
    def required_packing_fields(self) -> Set[str]:
        """ All required fields for packing up the secret """
        return set()

    def unpack(self, data: Dict[str, str]):
        """Unpack the Kubernetes secret `data` field to fill in required secret values

        All required packing fields must be present.
        By default looks for all required fields and base64 decodes them

        Args:
            data (Dict[str, str]): _description_
        """

        missing_fields = self.required_packing_fields - data.keys()
        if missing_fields:
            raise ValueError('Missing required field(s) to unpack Secret: '
                             f'{",".join(missing_fields)}')

        for required_field in self.required_packing_fields:
            setattr(self, required_field, base64_decode(data[required_field]))

    def pack(self) -> Dict[str, str]:
        """The `data` field for the corresponding kubernetes secret
        Validated to ensure fully completed

        By default base64 encodes all required fields
        """
        filled_fields = asdict(self)
        data = {k: v for k, v in filled_fields.items() if k in self.required_packing_fields}
        for key, value in data.items():
            if not isinstance(value, str):
                raise TypeError(f'All keys in a secret must be strings, got {key}: {type(value)}')
            data[key] = base64_encode(value)
        return data

    def pull(self, platform: MCLIPlatform):
        with MCLIPlatform.use(platform):
            # Read the secret if it exists
            secret = read_secret(self.name, platform.namespace)
            if not secret:
                raise RuntimeError(f'Could not find secret {self.name} in platform {platform.name}')
            assert isinstance(secret['data'], dict)
            self.unpack(secret['data'])

    @classmethod
    def from_dict(cls: Type[T_SerializableDataclass], data: Dict[str, Any]) -> T_SerializableDataclass:
        secret_type = data.get('secret_type', None)
        if not secret_type:
            raise ValueError(f'No `secret_type` found for secret with data: \n{yaml.dump(data)}')

        secret_type: SecretType = SecretType.ensure_enum(secret_type)
        data['secret_type'] = secret_type

        # pylint: disable-next=import-outside-toplevel
        from mcli.objects.secrets import (MCLIDockerRegistrySecret, MCLIEnvVarSecret, MCLIMountedSecret, MCLIS3Secret,
                                          MCLISSHSecret)
        secret: Optional[MCLISecret] = None
        secret_type = DEPRECATED_SECRETS.get(secret_type, secret_type)
        if secret_type == SecretType.docker_registry:
            secret = MCLIDockerRegistrySecret(**data)
        elif secret_type == SecretType.mounted:
            secret = MCLIMountedSecret(**data)
        elif secret_type == SecretType.environment:
            secret = MCLIEnvVarSecret(**data)
        elif secret_type == SecretType.ssh:
            secret = MCLISSHSecret(**data)
        elif secret_type == SecretType.s3_credentials:
            secret = MCLIS3Secret(**data)
        else:
            raise NotImplementedError(f'Secret of type: { secret_type } not supported yet')
        assert isinstance(secret, MCLISecret)
        return secret  # type: ignore

    @property
    def kubernetes_labels(self) -> Dict[str, str]:
        """Labels to add to all Kubernetes secrets
        """
        labels = {
            label.mosaic.SECRET_TYPE: self.secret_type.value.replace('_', '-'),
            **label.mosaic.version.get_version_labels(),
        }
        return labels

    @property
    def kubernetes_annotations(self) -> Dict[str, str]:
        """Annotations to add to all Kubernetes secrets
        """
        return {}


@dataclass
class MCLIGenericSecret(MCLISecret):
    """Secret class for generic secrets
    """
    value: Optional[str] = None

    @property
    def disk_skipped_fields(self) -> List[str]:
        return ['value']

    @property
    def required_packing_fields(self) -> Set[str]:
        return set(self.disk_skipped_fields)

    def add_to_job(self, kubernetes_job: MCLIK8sJob) -> bool:
        del kubernetes_job
        # Missing context on how it should be added to a job
        raise NotImplementedError
