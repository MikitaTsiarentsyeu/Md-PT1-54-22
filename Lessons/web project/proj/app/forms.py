from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=300)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField()
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)

    def clean_subtitle(self):

        sub_data = self.cleaned_data['subtitle']
        ttl_data = self.cleaned_data['title']

        if sub_data == ttl_data:
            raise ValidationError("The title and subtitle values should be different")

        return sub_data
