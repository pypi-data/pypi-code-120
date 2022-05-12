from django.contrib.contenttypes.models import ContentType
from django.db import transaction


def compile_path_node(ct_id, object_id):
    return f'{ct_id}:{object_id}'


def decompile_path_node(repr):
    ct_id, object_id = repr.split(':')
    return int(ct_id), int(object_id)


def object_to_path_node(obj):
    """
    Return a representation of an object suitable for inclusion in a CablePath path. Node representation is in the
    form <ContentType ID>:<Object ID>.
    """
    ct = ContentType.objects.get_for_model(obj)
    return compile_path_node(ct.pk, obj.pk)


def path_node_to_object(repr):
    """
    Given the string representation of a path node, return the corresponding instance.
    """
    ct_id, object_id = decompile_path_node(repr)
    ct = ContentType.objects.get_for_id(ct_id)
    return ct.model_class().objects.get(pk=object_id)


def create_cablepath(node):
    """
    Create CablePaths for all paths originating from the specified node.
    """
    from dcim.models import CablePath

    cp = CablePath.from_origin(node)
    if cp:
        cp.save()


def rebuild_paths(obj):
    """
    Rebuild all CablePaths which traverse the specified node
    """
    from dcim.models import CablePath

    cable_paths = CablePath.objects.filter(path__contains=obj)

    with transaction.atomic():
        for cp in cable_paths:
            cp.delete()
            if cp.origin:
                create_cablepath(cp.origin)
