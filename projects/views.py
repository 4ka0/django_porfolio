from django.shortcuts import render

# each function here represents a view

def project_list(request):
    return render(request, 'projects/index.html')
