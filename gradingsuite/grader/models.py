from django.db import models


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    home_dir = models.CharField(max_length=1000, default="/")
