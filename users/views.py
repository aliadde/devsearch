from django.shortcuts import render
from .models import Profile,Skill
from django.http import Http404
# from ..projects.models import Project
# Create your views here.
def profiles(request):
      profiles = Profile.objects.all()
      
      return render(request, 'users/profiles.html',{'profiles':profiles})

def userprofile(request, pk):
      
      profile = Profile.objects.get(id=pk)
      skills = profile.skill_set.all()
      # other way to fillter skills have description or not 
      # have description
      # => topskill = profile.skill_set.exclude(description__exact="")
      # do not have description+

      context = {'profile':profile,'skills':skills }
      return render(request, 'users/user-profile.html', context)