import os

from django.contrib import admin

# Register your models here.
from grader.models import *

admin.site.register(Rubric)
admin.site.register(RubricSection)
admin.site.register(RubricItem)
admin.site.register(Submission)
admin.site.register(Student)


def create_submission(assignment, dir):
    # old_rubric = assignment.rubric_set.all()[0]
    rubric = assignment.rubric_set.all()[0]
    # rubric.pk = None  # makes this a new copy
    # rubric.save()
    # for section in old_rubric.rubricsection_set.all():
    #     new_section = RubricSection.objects.get(pk=section.id)
    #     new_section.pk = None
    #     new_section.rubric = rubric
    #     new_section.save()
    #     for item in section.rubricitem_set.all():
    #         new_item = RubricItem.objects.get(pk=item.id)
    #         new_item.pk = None
    #         new_item.section = new_section
    #         new_item.save()
    try:
        student = Student.objects.get(institution_id=dir)
    except:
        student = Student(name=dir, email=(dir + "@umbc.edu"), institution_id=dir)  # TODO: get email domain from config
        student.save()
    submission = Submission(student=student, filename=dir, rubric=rubric)

    submission.save()
    return submission


def populate_submissions(modeladmin, request, queryset):
    for assignment in queryset:
        home_dir = assignment.home_dir
        for subdir in os.listdir(home_dir):
            full_subdir = os.path.join(home_dir, subdir)
            if os.path.isdir(full_subdir):
                create_submission(assignment, subdir)


class AssignmentAdmin(admin.ModelAdmin):
    actions = [populate_submissions]


admin.site.register(Assignment, AssignmentAdmin)