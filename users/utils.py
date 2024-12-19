from .models import Profile , Skill
# for search bar 
from django.db.models import Q


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