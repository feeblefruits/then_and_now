from django import forms
from then_and_now_project.models import BeforePhoto, AfterPhoto

class BeforePhotoForm(forms.ModelForm):
    class Meta:
        model = BeforePhoto
        fields = ['title', 'description', 'pseudonym', 'photo']

class AfterPhotoForm(forms.ModelForm):
    class Meta:
        model = AfterPhoto
        fields = ['title', 'description', 'pseudonym', 'photo']
