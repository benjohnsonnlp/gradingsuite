from django.contrib import admin

# Register your models here.
from grader.models import *

admin.site.register(Assignment)
admin.site.register(Rubric)
admin.site.register(RubricSection)
admin.site.register(RubricItem)
