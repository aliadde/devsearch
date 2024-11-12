from django.shortcuts import render
from .models import Project
# Create your views here.
def base(request):
      return render(request, 'projects/base.html' )

def singlepage(request, id ):
      projects = Project.objects.all()
      for item in projects: 
            if str(item.id) == id:
                  project = item 
      
      return render(request, 'projects/singleproject.html',{'project': project } )
      
def projects(request):
      projects = Project.objects.all()

      context = {'projects':projects}
      return render(request, 'projects/projects.html', context )
      