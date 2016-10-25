from django import forms

from .models import Post
from .models import Mail

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ('address',)
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
        }
        labels = {
            'address': '',
        }