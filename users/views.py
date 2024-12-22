from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .forms import CustomUCF, ProfileForm, SkillForm
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles, pagination

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
            username = request.POST['username'].lower()
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
                  
                  return redirect(request.GET['next'] if 'next' in request.GET else 'account')
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
      profiles , search_query = searchProfiles(request)
      profiles, paginator, custom_range =   pagination(request, profiles) 
      
      if custom_range != 0 : # if not 0 , means we have range
            context = {
                  'profiles':profiles, 
                  'search_query':search_query ,
                  'customRange': custom_range,
                  }
            
            
      else: # NO custom range 
            context = {
                  'profiles':profiles, 
                  'search_query':search_query ,
                  'customRange':paginator.page_range,
                  } 
            

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
      page = "create"
      profile = request.user.profile 
      form = SkillForm()
      if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                  skill = form.save(commit=False)
                  skill.owner = profile
                  skill.save()
                  messages.success(request , 'New Skill Created ')
                  return redirect('account')


      context = {"form": form ,'page':page}
      return render(request, 'users/skill_form.html',context) 

@login_required(login_url ='login') 
def updateSkill(request, pk):
      page = "update"
      profile = request.user.profile 
      skill = profile.skill_set.get(id=pk)
      form = SkillForm(instance=skill)

      if request.method == 'POST':
            form = SkillForm(request.POST, instance= skill)
            if form.is_valid():
                  form.save()
                  messages.success(request , 'Skill Updated')
                  return redirect('account')


      context = {"form": form ,'page':page}
      return render(request, 'users/skill_form.html',context) 

@login_required(login_url ='login') 
def deleteSkill(request, pk):
      profile = request.user.profile
      skill = profile.skill_set.get(id=pk)
      if request.method == 'POST':
            skill.delete()
            messages.success(request, "skill deleted")
            return redirect('account')
      context = {'object':skill}
      return render(request, 'delete.html', context)

@login_required(login_url ='login') 
def inbox(request):
      context = {}
      return render(request, 'users/inbox.html', context )