import os

from django.db import models


def file_endings(language):
    endings = {
        "python": [
            ".py",
        ],
    }
    return endings[language]


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    home_dir = models.CharField(max_length=1000, default="/")
    language = models.CharField(max_length=200, default="python")
    rubric_filename = models.CharField(max_length=1000, default='sample_rubric.json')


class Rubric(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    is_blank = models.BooleanField(default=True)


class RubricSection(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, default="General")


class RubricItem(models.Model):
    section = models.ForeignKey(RubricSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, default="")
    possible_points = models.IntegerField()
    optional = models.BooleanField()


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    institution_id = models.CharField(max_length=200)


class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    filename = models.CharField(max_length=1000)
    rubric = models.ForeignKey(Rubric, on_delete=models.SET_NULL, null=True)

    def project_files(self):
        self.files = []
        home_dir = self.rubric.assignment.home_dir
        full_path = os.path.join(home_dir, self.filename)
        for subdir in os.listdir(full_path):
            full_subdir = os.path.join(full_path, subdir)
            # if it's a file with one of the endings for the language of the assignment
            if not os.path.isdir(full_subdir):
                for ending in file_endings(self.rubric.assignment.language):
                    if full_subdir.endswith(ending):
                        self.files.append(subdir)

        return self.files


class GradedItem(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    rubric_item = models.ForeignKey(RubricItem, null=True, on_delete=models.SET_NULL)
    earned_points = models.IntegerField()
