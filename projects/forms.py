from django import forms
from django.forms  import widgets
from .models import Project

class ProjectForm(forms.ModelForm):
      class Meta:
            model = Project
            fields = ['title','description','demo_link','source_link'
                      ,'tags','featured_image']
            widgets = {
                  'tags': forms.CheckboxSelectMultiple(),
            }

            
      # آخرم به زور فهمیدم چیشد توی این کده پایین 
      def __init__(self,*args, **kwargs):
            super(ProjectForm, self).__init__(*args,**kwargs)
            for name , field in self.fields.items():
                  field.widget.attrs.update(
                        {
                              'class':"input input--text" ,
                               'id':"formInput#text" ,
                        }
                  )


