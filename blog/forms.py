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
        labels = {
            'addresse': '',
        }
        help_texts = {
            'name': _('adresse email'),
        }