from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.template import loader

from grader.models import Assignment
from grader.submissions import get_submissions, Submission
from grader.templatetags.grader_extras import get_contents


def index(request):
    template = loader.get_template("grader/index.html")
    context = {
        "assignments": Assignment.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def assignment(request, assignment_id):
    template = loader.get_template("grader/assignment.html")
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submissions = get_submissions(assignment.home_dir, assignment)
    context = {
        "assignment": assignment,
        "submissions": submissions,
    }
    return HttpResponse(template.render(context, request))


def submission(request, assignment_id):
    template = loader.get_template("grader/submission.html")
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submission = Submission(request.GET.get("path"), assignment)
    context = {
        "assignment": assignment,
        "submission": submission,
    }
    return HttpResponse(template.render(context, request))


def get_file_contents(request, assignment_id):
    file = request.POST.get("filename", "")
    with open(file, 'r') as f:
        contents = f.read()
    # assignment = get_object_or_404(Assignment, pk=assignment_id)
    # submission = Submission(request.GET.get("path"), assignment)
    return HttpResponse(contents)
