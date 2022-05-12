# Fake views for testing url reverse lookup
from paradoxdjango.http import HttpResponse
from paradoxdjango.template.response import TemplateResponse


def index(request):
    pass


def client(request, id):
    pass


def client_action(request, id, action):
    pass


def client2(request, tag):
    pass


def template_response_view(request):
    return TemplateResponse(request, "response.html", {})


def snark(request):
    return HttpResponse("Found them!")
