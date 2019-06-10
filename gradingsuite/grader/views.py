import os

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie

from grader.models import Assignment, RubricSection, RubricItem, Submission


@ensure_csrf_cookie
def index(request):
    template = loader.get_template("grader/index.html")
    context = {
        "assignments": Assignment.objects.all(),
    }
    return HttpResponse(template.render(context, request))


@ensure_csrf_cookie
def assignment(request, assignment_id):
    template = loader.get_template("grader/assignment.html")
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    rubric = assignment.rubric_set.all()[0]
    submissions = rubric.submission_set.all()
    context = {
        "assignment": assignment,
        "submissions": submissions,
    }
    return HttpResponse(template.render(context, request))


def get_sections(rubric):
    output = {}
    for section in RubricSection.objects.filter(rubric=rubric.id):
        items = [item.text for item in RubricItem.objects.filter(section=section.id)]
        output[section.name] = items
    return output


@ensure_csrf_cookie
def submission(request, assignment_id, submission_id):
    template = loader.get_template("grader/submission.html")
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    # with open(assignment.rubric_filename, 'r') as f:
    #     rubric = json.load(f)
    rubric = assignment.rubric_set.all()[0]
    # sections = get_sections(rubric)
    if submission.project_files():
        filename = os.path.join(
            assignment.home_dir,
            submission.filename,
            submission.project_files()[0]
        )
        with open(filename, 'r') as f:
            submission_contents = f.read()
    else:
        submission_contents = []
    context = {
        "assignment": assignment,
        "submission": submission,
        "rubric": rubric,
        "submission_contents": submission_contents,
        # "sections": sections,
    }
    return HttpResponse(template.render(context, request))


@ensure_csrf_cookie
def get_file_contents(request, assignment_id):
    file = request.POST.get("filename", "")
    submission = request.POST.get("submission", "")
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    full_path = os.path.join(assignment.home_dir, submission, file)

    with open(full_path, 'r') as f:
        contents = f.read()
    return HttpResponse(contents)
