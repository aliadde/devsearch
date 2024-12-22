from django.shortcuts import render,redirect
from .models import Project ,Tag
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from .utils import searchProjects, pagination




def notFoundPage(request, error):
      context = {'error':error}
      return render(request , '404page.html',context) 


def base(request):
      try:
            return render(request, 'base.html' )
      except:
            return notFoundPage(request=request,error="An Error for base.html views.py ")


def projects(request):
      projects, search_query = searchProjects(request) 
      # serch_query is content user searched in search bar 

      projects, paginator, custom_range = pagination(request, projects)
      
      if custom_range != 0 : # if not 0 , means we have range

            context = {'projects':projects , 
                  'search_query':search_query, 
                  'customRange':custom_range, # we send custom range
                  }
      else: # NO custom range 
            context = {'projects':projects , 
                  'search_query':search_query, 
                  'customRange':paginator.page_range, # we send that paginator real range 
                  }

      return render(request,'projects/projects.html', context )


def singlepage(request, id ):
      # method get : get that projects has that id 
      projectobj = Project.objects.get(id=id)
      tags = projectobj.tags.all()
      form = ReviewForm() # instance of REviewForm in forms.py
      if request.method == 'POST':
            form = ReviewForm(request.POST)
            review = form.save(commit=False)
            review.project = projectobj # Foreignkey(Project, ... ) so need instance of project 
            review.owner = request.user.profile # foreignkey(Profile , ...) so neeed instance of profile of user sub minting
            review.save() 

            projectobj.get_vote_count
            messages.success(request, 'Thank You To Leave Message and improve our community')
            # updating vote ration 
            return redirect('singleproject', id=projectobj.id)
            

      
      context = {'project': projectobj ,'tags':tags ,'form':form}
      
      return render(request, 'projects/singleproject.html',context )


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
            messages.success(request, "project deleted")
            return redirect('account')
            
      context = {'object':project}
      return render(request, 'delete.html' ,context) 