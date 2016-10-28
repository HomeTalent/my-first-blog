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
        fields = ('address','service')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
        }
        labels = {
            'address': '',
            'service': 'Quel est le service dont vous avez le plus besoin ? (facultatif)'
        }
