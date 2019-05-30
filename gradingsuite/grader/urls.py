from django.urls import path

from grader import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assignments/<int:assignment_id>', views.assignment, name='assignment'),
]