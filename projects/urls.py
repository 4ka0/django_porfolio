from django.urls import path
from projects import views

urlpatterns = [
    path('', views.all_projects),  # points to site/projects
    # path('test', views.project_list),  # points to site/projects/test
]
