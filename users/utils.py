from .models import Profile , Skill
# for search bar 
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(request ,profiles):

      results = 6  # how much project shuld be shown in each page
      page = request.GET.get('page') # get page number from front end 
      paginator = Paginator(profiles, results) # each page 3 project 
      try: 
            profiles = paginator.page(page) # get projects of user choosed page

      except PageNotAnInteger: # if user do not choose wich page 
            # set default page to 1st page
            
            page = 1 
            profiles = paginator.page(page) # get projects of user choosed page
      except EmptyPage : 
            # if user search for page is not exist
            page = paginator.num_pages # set page to last page
            profiles = paginator.page(page)

      if paginator.num_pages > 5 : # if count of page are more than 5 
            # should call custom range 
            custom_range = pagination_Range(paginator ,page )
            return profiles, paginator, custom_range
      else:
            custom_range = 0 
            return profiles, paginator , custom_range

def pagination_Range(paginator, page):

      # for lots of pages
      left_index = int(page) - 4 # we want three pages before current page
       
      if left_index < 1 :
            left_index = 1 

      right_index = int(page) + 4 # we want three pages after current page

      if right_index > paginator.num_pages : 
            right_index = paginator.num_pages + 1  #  + 1 because range do not include number is endof range(, end) 
      
      custom_range = range(left_index, right_index) # we create a range for that
      
      return custom_range 


def searchProfiles(request):
      search_query = ''
      if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
      
      # CHECK SKILLS HAS THAT NAME 
      skills = Skill.objects.filter(name__icontains= search_query)

      # check profile name and short_intro has the search value or not
      profiles = Profile.objects.distinct().filter(
            Q(name__icontains= search_query) |
             Q(short_intro__icontains= search_query) |
             Q(skill__in=skills)
             )

      if request.user:
            # if y=user logged in have to be remove from list of profiles
            rm = request.user.username
            # removing and set profiles again
            profiles = profiles.exclude(name=rm)
      
      return profiles, search_query