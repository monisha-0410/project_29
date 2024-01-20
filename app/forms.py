from django import forms
from app.models import *

class Topicform(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class Webpageform(forms.ModelForm):
    class Meta():
        model=WebPage
        fields='__all__'
        

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')

class AccessRecordform(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'  
        labels={'date':'Published_date'}     