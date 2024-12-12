from django.contrib.auth.models import User
from .models import  Profile , Skill 
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
# __

# try:
#     comment = User.objects.get(pk=user_id)
# except User.DoesNotExist:
#     user = None

# ___

#signal for the profile save      
def createprofile(sender , instance, created , **kwargs):
      if created :
            user = instance
            print(user)
            profile = Profile.objects.create(
                  user = user,
                  name = user.first_name,
                  username = user.username,
                  email = user.email,
            )


def profileDelete(sender,instance , **kwargs ):
      user = instance.user
      user.delete()
      print('\n\n \n\n \n\n    user delted from profile  ...')


def save(sender,instance,**kwargs):
      print('\n\n\n\t SAVED \n\n\n\t\n')
      print('\n\n\n')


      
      
      
post_save.connect(save,sender=User)
post_save.connect(save,sender=Profile)
post_save.connect(createprofile, sender=User)
post_delete.connect(profileDelete, sender=Profile)   


