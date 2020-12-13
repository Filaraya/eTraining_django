from django import forms
from .models import*

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title','summary', 'code', 'content_type']
        
class InstructorForm (forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'email']
        labels ={'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        

    