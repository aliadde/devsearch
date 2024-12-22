from django import forms
from django.forms  import widgets
from .models import Project ,Review

class ProjectForm(forms.ModelForm):
      class Meta:
            model = Project
            fields = ['title','description','demo_link','source_link'
                      ,'tags','featured_image']
            widgets = {
                  'tags': forms.CheckboxSelectMultiple(),
            }

            
      def __init__(self,*args, **kwargs):
            super(ProjectForm, self).__init__(*args,**kwargs)
            for name , field in self.fields.items():
                  field.widget.attrs.update(
                        {
                              'class':"input input--text" ,
                               'id':"formInput#text" ,
                        }
                  )

class ReviewForm(forms.ModelForm):
      class Meta :
            model = Review
            fields = ['value', 'body']
            labels = {
                  'value':'vote',
                  'body': 'comment'
            }

      def __init__(self,*args, **kwargs):
            super(ReviewForm, self).__init__(*args,**kwargs)
            for name , field in self.fields.items():
                  field.widget.attrs.update(
                        {
                              'class':"input input--text" ,
                               'id':"formInput#text" ,
                        }
                  )