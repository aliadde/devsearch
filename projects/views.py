from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
def base(request):
      return render(request, 'base.html' )

def projects(request):
      projects = Project.objects.all()
      context = {'projects':projects}
      return render(request,'projects/projects.html', context )
      
def singlepage(request, id ):
      # method get : get that projects has that id 
      project = Project.objects.get(id=id)
      tags = project.tags.all()
      return render(request, 'projects/singleproject.html',{'project': project ,'tags':tags} )


@login_required(login_url='/login')
def createProject(request):
      form = ProjectForm() 
      if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
                  return redirect('projects')
      
      context = {'form' : form}
      return render(request , 'projects/project_form.html', context)

@login_required(login_url='/login')
def updateProject(request,pk):
      project = Project.objects.get(id=pk)
      form = ProjectForm(instance=project) 
      if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES ,instance=project)
            if form.is_valid():
                  form.save()
                  return redirect('projects')
      
      context = {'form' : form}
      return render(request , 'projects/project_form.html', context)

@login_required(login_url='/login')
def deleteProject(request, pk):
      
      project = Project.objects.get(id=pk)
      if request.method == 'POST':
            project.delete()
            print('Project Deleted ')
            return redirect('projects')
            
      context = {'project':project}
      return render(request, 'projects/delete.html' ,context) 