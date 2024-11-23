from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Project(models.Model):
      # it gonna inherite username from profile db tb 
      owner = models.ForeignKey(Profile,null=True,
                                 blank=True, on_delete= models.SET_NULL) 
      
      # title of the post 
      title = models.CharField(max_length=2000)

      #blank: for the django  null: is for database requirement
      description = models.TextField(null=True, blank=True)
      
      # image 
      featured_image = models.ImageField( null=True, blank=True , default='default.jpg')
      # demo link is for user has deployed their project to the internet and have their link for us just to see demo
      demo_link = models.CharField(max_length=2000 ,null=True, blank=True)
      
      # source link is for user has deployed their project to the internet and have their link 
      source_link = models.CharField(max_length=2000 ,null=True, blank=True)
      
      # refrence the tag to project 
      tags = models.ManyToManyField('Tag')

      # Vote has be store in project
      vote_total = models.IntegerField(default=0,null=True,blank=True)
      vote_ratio = models.IntegerField(default=0,null=True,blank=True)
      
      # Time of the creation of this post for us
      created = models.DateTimeField(auto_now_add=True)
      
      # id of the user. Django create User ID for us by default. UU ID are unique and have 16
      # char that are mix of nuber and char 
      id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False )
      
      
      # __str__ is python class 
      def __str__(self):
            return self.title
      
      # Review table 
class Review(models.Model):
      VOTE_TYPES =(
            ('Up' ,'Up Vote'),
            ('Down' ,'Down Vote')
      )
      # Own =
      project = models.ForeignKey(Project, on_delete=models.CASCADE)
      body = models.TextField(null=True, blank=True)
      value = models.CharField(max_length=2000 ,null=True, blank=True, choices=VOTE_TYPES)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False )      

      def __str__(self):
            return self.value
      
      
class Tag(models.Model):
      name = models.CharField(max_length=200)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False )  
      
      def __str__(self):
            return self.name      