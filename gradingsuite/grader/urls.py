from django.urls import path

from grader import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assignments/<int:assignment_id>/', views.assignment, name='assignment'),
    path('assignments/<int:assignment_id>/submission/<int:submission_id>', views.submission, name='submission'),
    path('assignments/<int:assignment_id>/submission/file_contents', views.get_file_contents, name='file_contents'),
]