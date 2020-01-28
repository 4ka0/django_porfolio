from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # points to site/projects
    path('', views.all_projects, name='all_projects'), 
    # '<int:pk>' gets an integer representing the primary key for 
    # an object in the database (only an int is accepted)
    # the first param is passed to the second param, basically
    path('<int:pk>', views.project_detail, name='project_detail'),
]
