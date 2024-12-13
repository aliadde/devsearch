from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages



      # log out
def logOutPage(request):
      if not request.user.is_authenticated :
            return redirect('login')

      elif request.method == 'POST':
            logout(request) 
            print('\n\n\n logged out ')
            messages.success(request,'succesfully logged out ')
            return redirect('profiles')
      elif request.method == 'GET':
            return  render(request, 'users/logout.html')


      # log in 
def loginPage(request):
      if request.user.is_authenticated :
            return redirect('profiles')
      elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            try:
                  user = User.objects.get(username=username)
                  print("\nuser is exist")
            except:
                  messages.error(request ," Invalid user, user doe not exisst")

            user = authenticate(request , username=username , password=password)
            if user is not None :
                  login(request,user)
                  return redirect('profiles')
            else:
                  messages.error(request ,'password or username dow not exist')

      return render(request, 'users/login_register.html',{})



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