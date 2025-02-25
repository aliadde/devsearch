from django.db import models
from django.contrib.auth.models import User
import uuid

# skill is child of profile
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE,       
            null=True, blank=True)

      name = models.CharField(max_length=200, blank=True, null=True)
      
      email = models.EmailField(max_length=500, blank=True,null=True)
      
      username =models.CharField(max_length=200, blank=True, null=True)
      
      location = models.CharField(max_length=200, blank=True, null=True)
      
      short_intro = models.CharField(max_length=200, blank=True, null=True)
      
      bio = models.TextField(blank=True, null=True)
      
      profile_image = models.ImageField(blank=True,null=True,
            default='user-default.png', upload_to='profiles/')
                        
      social_github  = models.CharField(max_length=200, blank=True, null=True)
      social_twitter = models.CharField(max_length=200, blank=True, null=True)
      social_linkdin = models.CharField(max_length=200, blank=True, null=True)
      social_youtube = models.CharField(max_length=200, blank=True, null=True)
      social_website = models.CharField(max_length=200, blank=True, null=True)

      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4 ,
                  unique=True , primary_key=True , editable=False )

      def __str__(self):
            return str(self.user.username)


class Skill(models.Model):
      owner = models.ForeignKey(Profile,on_delete=models.CASCADE,
                  null=True, blank=True)
                  
      id = models.UUIDField(unique=True,
                  default=uuid.uuid4,primary_key=True,editable=False)
                  
      name = models.CharField(max_length=100 , null=True, blank=True)
      description = models.TextField(max_length=1000 , null=True, blank=True)

      created = models.DateTimeField(auto_now_add=True)
                  
      def __str__(self):
            return str(self.name)


# meesages and comment

class Message(models.Model):
      sender = models.ForeignKey(Profile,
                         on_delete=models.SET_NULL, null=True,blank=True)
      # this is ok user do not have account and send message

      recipient =  models.ForeignKey(Profile,
                         on_delete=models.SET_NULL, null=True,blank=True, related_name='messages')
      #  if we do not set related_name we can not acces to the sender and recipient . because we use that twice with foreignkey

      name = models.CharField( max_length=200 , blank=True,null=True)
      # near the profiel give us name of user sending message, we want to have anouther name. 

      email =  models.EmailField(max_length=200 , blank=True,null=True)
      # anouther email to send 

      subject = models.CharField( max_length=200 , null=True, blank=True)
      # wen need subject to defined issue sender will send

      body = models.TextField()
      # textfiled for the message

      is_read = models.BooleanField(default=False, null=True)
      # is read or not?  

      created = models.DateTimeField(auto_now_add=True) # we always want Date 
      id = models.UUIDField(default=uuid.uuid4 ,
                  unique=True , primary_key=True , editable=False ) 
      # we always need unique id to prrvent from interuption in getting data 

      def __str__(self):
            if self.subject == None:
                  return self.body[0:20]
            else:
                  return self.subject

      class Meta: 
            ordering = [
                  "is_read",
                  "-created",
            ]