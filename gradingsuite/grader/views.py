from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from grader.models import Assignment
from grader.submissions import get_submissions


def index(request):
    template = loader.get_template("grader/index.html")
    context = {
        "assignments": Assignment.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def assignment(request, assignment_id):
    template = loader.get_template("grader/assignment.html")
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submissions = get_submissions(assignment.home_dir)
    context = {
        "assignment": assignment,
        "submissions": submissions,
    }
    return HttpResponse(template.render(context, request))
