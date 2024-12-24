from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage # 2st = actually a TypeOfError. 3st = TypeOfError

def pagination(request ,projects):

      results = 9 # how much project shuld be shown in each page
      page = request.GET.get('page') # get page number from front end 
      paginator = Paginator(projects, results) # each page 3 project 
      try: 
            projects = paginator.page(page) # get projects of user choosed page

      except PageNotAnInteger: # if user do not choose wich page 
            # set default page to 1st page
            
            page = 1 
            projects = paginator.page(page) # get projects of user choosed page
      except EmptyPage : 
            # if user search for page is not exist
            page = paginator.num_pages # set page to last page
            projects = paginator.page(page)

      if paginator.num_pages > 5 : # if count of page are more than 5 
            # should call custom range 
            custom_range = pagination_Range(paginator ,page )
            return projects, paginator, custom_range
      else:
            custom_range = 0 
            return projects, paginator , custom_range

def pagination_Range(paginator, page):

      # for lots of pages
      left_index = int(page) - 4 # we want three pages before current page
       
      if left_index < 1 :
            left_index = 1 

      right_index = int(page) + 4 # we want three pages after current page

      if right_index > paginator.num_pages : 
            right_index = int(paginator.num_pages) + 1  #  + 1 because range do not include number is endof range(, end) 
      
      custom_range = range(left_index, right_index) # we create a range for that
      
      return custom_range

def searchProjects(request):
      search_query = ''
      if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
      
      tags = Tag.objects.filter(name__icontains=search_query)
            
      
      projects = Project.objects.distinct().filter( 
            Q(title__icontains = search_query) |
            Q(description__icontains=search_query) |
            Q(owner__name__icontains=search_query) |
            Q(tags__in=tags)
      )
      
      return projects, search_query