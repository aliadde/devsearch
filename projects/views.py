from django.shortcuts import render

# Create your views here.
def base(request):
      return render(request, 'projects/base.html' )

def singlepage(request):
      return render(request, 'projects/singleproject.html' )
      
def projects(request):
      return render(request, 'projects/projects.html' )
      