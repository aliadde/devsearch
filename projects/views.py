from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.http import HttpResponseNotFound
def notFoundPage(request, error):
      context = {'error':error}
      return render(request , '404page.html',context) 


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
      profile = request.user.profile
      form = ProjectForm() 
      if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                  project = form.save(commit=False)
                  project.owner = profile
                  project.save()
                  return redirect('account')
      
      context = {'form' : form}
      return render(request , 'projects/project_form.html', context)

@login_required(login_url='/login')
def updateProject(request,pk):
      profile = request.user.profile
      try:
            project = profile.project_set.get(id=pk)
            print('\n\n\n')
            print('project ', project)
      except:
            return notFoundPage(request=request,error='you can not access to this project to edit, sorry dadasham')
            
      
      form = ProjectForm(instance=project) 
      if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES ,instance=project)
            if form.is_valid():
                  form.save()
                  return redirect('account')
      context = {'form' : form}
      return render(request , 'projects/project_form.html', context)
      
            
@login_required(login_url='/login')
def deleteProject(request, pk):
      profile = request.user.profile
      try:
            project = profile.project_set.get(id=pk)
            print('\n\n\n')
            print('project ', project)
      except:
            return notFoundPage(request=request,error='you can not access to this project to delete, sorry dadasham')
            
      if request.method == 'POST':
            project.delete()
            print('Project Deleted ')
            return redirect('account')
            
      context = {'project':project}
      return render(request, 'projects/delete.html' ,context) 