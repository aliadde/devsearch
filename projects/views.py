from django.shortcuts import render
from .models import Project

# Create your views here.

def base(request):
      return render(request, 'projects/base.html' )

def projects(request):
      projects = Project.objects.all()

      context = {'projects':projects}
      return render(request, 'projects/projects.html', context )
      
def singlepage(request, id ):
      # method get : get that projects has that id 
      project = Project.objects.get(id=id)
      tags = project.tags.all()
      return render(request, 'projects/singleproject.html',{'project': project ,'tags':tags} )


def createProject(request ):

      context = {}
      return render(request , 'projects/project_form.html', context)