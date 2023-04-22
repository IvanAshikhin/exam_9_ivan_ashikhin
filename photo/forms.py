from django import forms
from photo.models import Photo


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Find')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'signature']
