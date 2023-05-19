from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    add_image = forms.BooleanField(initial=True)
    class Meta:
        model = Post
        fields = ('title', 'text','add_image','image',)
    class Media:
        js = ('conditionalpostform.js',)
    def clean(self):
        if self.cleaned_data['add_image'] and self.cleaned_data['image'] is None:
            raise forms.ValidationError('This works')

