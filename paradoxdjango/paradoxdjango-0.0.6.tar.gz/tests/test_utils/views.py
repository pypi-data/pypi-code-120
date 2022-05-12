from paradoxdjango.http import HttpResponse
from paradoxdjango.shortcuts import get_object_or_404
from paradoxdjango.template import Context, Template

from .models import Person


def get_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return HttpResponse(person.name)


def no_template_used(request):
    template = Template("This is a string-based template")
    return HttpResponse(template.render(Context({})))


def empty_response(request):
    return HttpResponse()
