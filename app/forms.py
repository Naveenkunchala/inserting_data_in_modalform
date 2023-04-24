from django import forms
from app.models import *

class TopicForms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        
        
class WebpageForms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        # fields=['topics_names','name']
        # exclude=['name']
        # widgets={'name':forms.PasswordInput}
        # labels={'name':'username','topics_names':'Topicname'}
        # help_texts={'name':'Only Alphbets'}
        
        
class AccessRecordsForms(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
        