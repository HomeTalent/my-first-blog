from django import forms

from .models import Post
from .models import Mail

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class MailFormAsker(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ('service','address','user_type')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
            'user_type': forms.HiddenInput()
        }
        labels = {
            'service': 'Mon besoin !',
            'address': ''
        }

class MailFormTasker(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ('service','address','user_type')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
            'user_type': forms.HiddenInput()
        }
        labels = {
            'service': 'Mon talent !',
            'address': ''
        }