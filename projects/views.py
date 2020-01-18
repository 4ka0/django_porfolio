from django.shortcuts import render
from projects.models import Project

# each function here represents a view
# this is where the logic is set out for actions
# such as retrieving data from the database 

'''
def project_list(request):
    return render(request, 'projects/index.html')
'''

def all_projects(request):
    # query database to return all project objects stored therein
    projects = Project.objects.all()
    # pass the projects object to the template using a dict as a third argument
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})
