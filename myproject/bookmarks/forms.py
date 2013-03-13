from django import forms
from bookmarks.models import Bookmark
 
 
class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields= ('author', 'url', 'title')
        widgets = {
            'author': forms.HiddenInput(),
        }
    tags = forms.CharField(max_length=100, required=False)