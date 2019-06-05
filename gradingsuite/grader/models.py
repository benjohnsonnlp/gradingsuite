from django.db import models


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    home_dir = models.CharField(max_length=1000, default="/")
    language = models.CharField(max_length=200, default="python")
    rubric_filename = models.CharField(max_length=1000, default='sample_rubric.json')

class Rubric(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=200, default="")


class RubricSection(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, default="General")


class RubricItem(models.Model):
    section = models.ForeignKey(RubricSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, default="")
    possible_points = models.IntegerField()
    earned_points = models.IntegerField()