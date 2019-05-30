from django.http import HttpResponse
from django.template import loader

from grader.models import Assignment


def index(request):
    template = loader.get_template("grader/index.html")
    context = {
        "assignments": Assignment.objects.all(),
    }
    return HttpResponse(template.render(context, request))