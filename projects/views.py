'''
Each function here represents a view.
This is where the logic is set out for actions
such as retrieving data from the database.
'''

from django.shortcuts import render
from projects.models import Project


def all_projects(request):
    '''
    Function to return all projects in the database.
    '''
    # query database to return all project objects stored therein
    projects = Project.objects.all()
    # param 1 = request
    # param 2 = the template to be used
    # param 3 = all projects object as a dict
    return render(request, 'projects/all_projects.html', {'projects': projects})


def project_detail(request, pk):
    '''
    Function to return the details of a single project.
    '''
    # retrieve the object having the primary key in question
    project = Project.objects.get(pk=pk)
    # param 1 = request
    # param 2 = the template to be used
    # param 3 = the individual project in question
    return render(request, 'projects/detail.html', {'project': project})
