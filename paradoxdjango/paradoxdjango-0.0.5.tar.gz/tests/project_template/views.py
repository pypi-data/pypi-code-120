from paradoxdjango.http import HttpResponse


def empty_view(request, *args, **kwargs):
    return HttpResponse()
