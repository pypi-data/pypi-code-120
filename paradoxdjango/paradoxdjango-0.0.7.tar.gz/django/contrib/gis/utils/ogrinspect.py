"""
This module is for inspecting OGR data sources and generating either
models for GeoDjango and/or mapping dictionaries for use with the
`LayerMapping` utility.
"""
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal.field import (
    OFTDate,
    OFTDateTime,
    OFTInteger,
    OFTInteger64,
    OFTReal,
    OFTString,
    OFTTime,
)


def mapping(data_source, geom_name="geom", layer_key=0, multi_geom=False):
    """
    Given a DataSource, generate a dictionary that may be used
    for invoking the LayerMapping utility.

    Keyword Arguments:
     `geom_name` => The name of the geometry field to use for the model.

     `layer_key` => The key for specifying which layer in the DataSource to use;
       defaults to 0 (the first layer).  May be an integer index or a string
       identifier for the layer.

     `multi_geom` => Boolean (default: False) - specify as multigeometry.
    """
    if isinstance(data_source, str):
        # Instantiating the DataSource from the string.
        data_source = DataSource(data_source)
    elif isinstance(data_source, DataSource):
        pass
    else:
        raise TypeError(
            "Data source parameter must be a string or a DataSource object."
        )

    # Creating the dictionary.
    _mapping = {}

    # Generating the field name for each field in the layer.
    for field in data_source[layer_key].fields:
        mfield = field.lower()
        if mfield[-1:] == "_":
            mfield += "field"
        _mapping[mfield] = field
    gtype = data_source[layer_key].geom_type
    if multi_geom:
        gtype.to_multi()
    _mapping[geom_name] = str(gtype).upper()
    return _mapping


def ogrinspect(*args, **kwargs):
    """
    Given a data source (either a string or a DataSource object) and a string
    model name this function will generate a GeoDjango model.

    Usage:

    >>> from django.contrib.gis.utils import ogrinspect
    >>> ogrinspect('/path/to/shapefile.shp','NewModel')

    ...will print model definition to stout

    or put this in a Python script and use to redirect the output to a new
    model like:

    $ python generate_model.py > myapp/models.py

    # generate_model.py
    from django.contrib.gis.utils import ogrinspect
    shp_file = 'data/mapping_hacks/world_borders.shp'
    model_name = 'WorldBorders'

    print(ogrinspect(shp_file, model_name, multi_geom=True, srid=4326,
                     geom_name='shapes', blank=True))

    Required Arguments
     `datasource` => string or DataSource object to file pointer

     `model name` => string of name of new model class to create

    Optional Keyword Arguments
     `geom_name` => For specifying the model name for the Geometry Field.
       Otherwise will default to `geom`

     `layer_key` => The key for specifying which layer in the DataSource to use;
       defaults to 0 (the first layer).  May be an integer index or a string
       identifier for the layer.

     `srid` => The SRID to use for the Geometry Field.  If it can be determined,
       the SRID of the datasource is used.

     `multi_geom` => Boolean (default: False) - specify as multigeometry.

     `name_field` => String - specifies a field name to return for the
       __str__() method (which will be generated if specified).

     `imports` => Boolean (default: True) - set to False to omit the
       `from django.contrib.gis.db import models` code from the
       autogenerated models thus avoiding duplicated imports when building
       more than one model by batching ogrinspect()

     `decimal` => Boolean or sequence (default: False).  When set to True
       all generated model fields corresponding to the `OFTReal` type will
       be `DecimalField` instead of `FloatField`.  A sequence of specific
       field names to generate as `DecimalField` may also be used.

     `blank` => Boolean or sequence (default: False).  When set to True all
       generated model fields will have `blank=True`.  If the user wants to
       give specific fields to have blank, then a list/tuple of OGR field
       names may be used.

     `null` => Boolean (default: False) - When set to True all generated
       model fields will have `null=True`.  If the user wants to specify
       give specific fields to have null, then a list/tuple of OGR field
       names may be used.

    Note: Call the _ogrinspect() helper to do the heavy lifting.
    """
    return "\n".join(_ogrinspect(*args, **kwargs))


def _ogrinspect(
    data_source,
    model_name,
    geom_name="geom",
    layer_key=0,
    srid=None,
    multi_geom=False,
    name_field=None,
    imports=True,
    decimal=False,
    blank=False,
    null=False,
):
    """
    Helper routine for `ogrinspect` that generates GeoDjango models corresponding
    to the given data source.  See the `ogrinspect` docstring for more details.
    """
    # Getting the DataSource
    if isinstance(data_source, str):
        data_source = DataSource(data_source)
    elif isinstance(data_source, DataSource):
        pass
    else:
        raise TypeError(
            "Data source parameter must be a string or a DataSource object."
        )

    # Getting the layer corresponding to the layer key and getting
    # a string listing of all OGR fields in the Layer.
    layer = data_source[layer_key]
    ogr_fields = layer.fields

    # Creating lists from the `null`, `blank`, and `decimal`
    # keyword arguments.
    def process_kwarg(kwarg):
        if isinstance(kwarg, (list, tuple)):
            return [s.lower() for s in kwarg]
        elif kwarg:
            return [s.lower() for s in ogr_fields]
        else:
            return []

    null_fields = process_kwarg(null)
    blank_fields = process_kwarg(blank)
    decimal_fields = process_kwarg(decimal)

    # Gets the `null` and `blank` keywords for the given field name.
    def get_kwargs_str(field_name):
        kwlist = []
        if field_name.lower() in null_fields:
            kwlist.append("null=True")
        if field_name.lower() in blank_fields:
            kwlist.append("blank=True")
        if kwlist:
            return ", " + ", ".join(kwlist)
        else:
            return ""

    # For those wishing to disable the imports.
    if imports:
        yield "# This is an auto-generated Django model module created by ogrinspect."
        yield "from django.contrib.gis.db import models"
        yield ""
        yield ""

    yield "class %s(models.Model):" % model_name

    for field_name, width, precision, field_type in zip(
        ogr_fields, layer.field_widths, layer.field_precisions, layer.field_types
    ):
        # The model field name.
        mfield = field_name.lower()
        if mfield[-1:] == "_":
            mfield += "field"

        # Getting the keyword args string.
        kwargs_str = get_kwargs_str(field_name)

        if field_type is OFTReal:
            # By default OFTReals are mapped to `FloatField`, however, they
            # may also be mapped to `DecimalField` if specified in the
            # `decimal` keyword.
            if field_name.lower() in decimal_fields:
                yield (
                    "    %s = models.DecimalField(max_digits=%d, decimal_places=%d%s)"
                ) % (
                    mfield,
                    width,
                    precision,
                    kwargs_str,
                )
            else:
                yield "    %s = models.FloatField(%s)" % (mfield, kwargs_str[2:])
        elif field_type is OFTInteger:
            yield "    %s = models.IntegerField(%s)" % (mfield, kwargs_str[2:])
        elif field_type is OFTInteger64:
            yield "    %s = models.BigIntegerField(%s)" % (mfield, kwargs_str[2:])
        elif field_type is OFTString:
            yield "    %s = models.CharField(max_length=%s%s)" % (
                mfield,
                width,
                kwargs_str,
            )
        elif field_type is OFTDate:
            yield "    %s = models.DateField(%s)" % (mfield, kwargs_str[2:])
        elif field_type is OFTDateTime:
            yield "    %s = models.DateTimeField(%s)" % (mfield, kwargs_str[2:])
        elif field_type is OFTTime:
            yield "    %s = models.TimeField(%s)" % (mfield, kwargs_str[2:])
        else:
            raise TypeError("Unknown field type %s in %s" % (field_type, mfield))

    # TODO: Autodetection of multigeometry types (see #7218).
    gtype = layer.geom_type
    if multi_geom:
        gtype.to_multi()
    geom_field = gtype.django

    # Setting up the SRID keyword string.
    if srid is None:
        if layer.srs is None:
            srid_str = "srid=-1"
        else:
            srid = layer.srs.srid
            if srid is None:
                srid_str = "srid=-1"
            elif srid == 4326:
                # WGS84 is already the default.
                srid_str = ""
            else:
                srid_str = "srid=%s" % srid
    else:
        srid_str = "srid=%s" % srid

    yield "    %s = models.%s(%s)" % (geom_name, geom_field, srid_str)

    if name_field:
        yield ""
        yield "    def __str__(self): return self.%s" % name_field
