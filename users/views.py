from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .forms import CustomUCF, ProfileForm, SkillForm
from django.contrib.auth.decorators import login_required

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
      page = 'login'
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

# register / sign up 
def register(request):
      if request.method == 'POST':
            form = CustomUCF(request.POST)
            if form.errors :
                  for error in form.errors:
                        
                        print(error)
            if form.is_valid() :
                  # its not gonna save completly
                  user = form.save(commit=False)
                  # check no one in database with same username (lowercase)
                  user.username = user.username.lower()
                  # then save
                  user.save()

                  messages.success(request, 'User account created' )
                  redirect('profiles')
                  # then log in 
                  login(request, user)
                  messages.success(request,'User account created')
                  return redirect('editaccount')
            else:       
                  print('get request')
                  

      form = CustomUCF()
      page = 'register'
      context = {'page':page ,'form':form}
      return render(request, 'users/login_register.html',context)

# profiles
def profiles(request):
      profiles = Profile.objects.all()
      
      if request.user:
            # if y=user logged in have to be remove from list of profiles
            rm = request.user.username
            # removing and set profiles again
            profiles = profiles.exclude(name=rm)
      
      context = {'profiles':profiles } 
      return render(request, 'users/profiles.html',context)

# single user profile
def userProfile(request, pk):

      profile = Profile.objects.get(id=pk)
      skills = profile.skill_set.all()
      context = {'profile':profile,'skills':skills }

      return render(request, 'users/user_profile.html', context)

# accout  user
@login_required(login_url ='login') 
def userAccount(request):
      profile = request.user.profile
      if request.session :
            print("\n\n re  \t  ", request.session  )
       
      userprojects = profile.project_set.all()
      context = {
            'profile':profile,
            'projects':userprojects,
      }
      return render(request,'users/account.html',context )

# editing account information
@login_required(login_url ='login') 
def editAccount(request):
      profile = request.user.profile
      form = ProfileForm(instance=profile)
      if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                  form.save()
                  return redirect('account')

      context = {'form':form}
      return render(request,'users/profile_form.html', context )
 
@login_required(login_url ='login') 
def createSkill(request):
      form = SkillForm()
      context = {"form": form}
      return render(request, 'users/skill_form.html',context) 