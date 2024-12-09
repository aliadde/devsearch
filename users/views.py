from django.shortcuts import render
from .models import Profile,Skill

# Create your views here.
def profiles(request):
      profiles = Profile.objects.all()
      
      return render(request, 'users/profiles.html',{'profiles':profiles})

def userprofile(request, pk):

      context = {}
      return render(request, 'users/user-profile.html', context)