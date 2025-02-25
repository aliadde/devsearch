from django.contrib.auth.models import User
from .models import  Profile , Skill 
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
# email sending 
from django.core.mail import send_mail
from django.conf import settings

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

      subject = 'account created.'
      message = 'You have been Created.\n We are so happy to you joind us'
      send_mail(
            subject , 
            message ,
            settings.EMAIL_HOST_USER , 
            [profile.email] ,
            fail_silently=False,
      )



def updateUser(sender,instance ,created, **kwargs):
      profile = instance
      user = profile.user
      # if user just updating information of profile
      if not created :
            user.first_name = profile.name
            user.username = profile.username
            user.save()
            print(user.username) 

      subject = 'account updated.'
      message = 'You have been Updated your profile'
      send_mail(
            subject , 
            message ,
            settings.EMAIL_HOST_USER , 
            [profile.email] ,
            fail_silently=False,
      )
 

def profileDelete(sender,instance , **kwargs ):
      user = instance.user
      user.delete()
      print('\n\n \n\n \n\n    user delted from profile  ...')


def save(sender,instance,**kwargs):
      print('\n\n\n\t SAVED \n\n\n\t\n')
      print('\n\n\n')


      
      
#if any save happend 
post_save.connect(save,sender=User)
#if any save happend 
post_save.connect(save,sender=Profile)
# update profile page * user has been logged in *
post_save.connect(updateUser,sender=Profile)
# if user register
post_save.connect(createprofile, sender=User)
# if user delete
post_delete.connect(profileDelete, sender=Profile)   

