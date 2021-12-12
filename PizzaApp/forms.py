from django import forms

from .models import Topic,Entry,Topin

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=('text','image','price')
        labels={'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}

class TopinForm(forms.ModelForm):
    class Meta:
        model=Topin
        fields=['text']
        labels={'text':''}

