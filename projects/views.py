from django.shortcuts import render
from django.http import HttpResponse

# each function here represents a view

def project_list(request):
    return render(request, 'projects/index.html')
