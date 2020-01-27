from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_projects),  # points to site/projects
    path('<int:pk>', views.project_detail)  # '<int:pk>' gets an integer 
                                            # representing the primary key for 
                                            # an object in the database
                                            # (only an int is accepted)
                                            # the first param is passed to 
                                            # the second param, basically
    # path('test', views.project_list),  # points to site/projects/test
]
