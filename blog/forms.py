# -*- coding: utf8 -*-

from django import forms
from .models import Post
from .models import Mail

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class MailFormAsker(forms.ModelForm):
    
    SERVICES_CHOICES = (
        ('bricolage', 'Bricolage'),
        ('jardinage', 'Jardinage'),
        ('demenagement', 'Déménagement'),
        ('menage-repassage', 'Ménage/Repassage'),
        ('assemblage-meuble', 'Assemblage meuble'),
        ('informatique', 'Informatique'),
        ('coursier', 'Coursier'),
        ('animaux', 'Garde d\'animaux'),
        ('evenementiel', 'Evénementiel'),
        ('prestation-administratif', 'Administratif'),
        ('service-personne', 'Service à la personne'),
        ('mode-beaute', 'Mode, Beauté & Bien-être')
    )

    services = forms.MultipleChoiceField(label='Mes besoins !',
                                        widget=forms.SelectMultiple(attrs={'class': 'selectpicker'}),
                                        choices=SERVICES_CHOICES)
    class Meta:

        model = Mail
        exclude = ['service']
        fields = ('address','user_type')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
            'user_type': forms.HiddenInput()
        }
        labels = {
            'address': ''
        }

class MailFormTasker(forms.ModelForm):

    SERVICES_CHOICES = (
        ('bricolage', 'Bricolage'),
        ('jardinage', 'Jardinage'),
        ('demenagement', 'Déménagement'),
        ('menage-repassage', 'Ménage/Repassage'),
        ('assemblage-meuble', 'Assemblage meuble'),
        ('informatique', 'Informatique'),
        ('coursier', 'Coursier'),
        ('animaux', 'Garde d\'animaux'),
        ('evenementiel', 'Evénementiel'),
        ('prestation-administratif', 'Administratif'),
        ('service-personne', 'Service à la personne'),
        ('mode-beaute', 'Mode, Beauté & Bien-être')
    )

    services = forms.MultipleChoiceField(label='Mes talents !',
                                        widget=forms.SelectMultiple(attrs={'class': 'selectpicker'}),
                                        choices=SERVICES_CHOICES)
    class Meta:
        model = Mail
        exclude = ['service']
        fields = ('address','user_type')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
            'user_type': forms.HiddenInput()
        }
        labels = {
            'address': ''
        }
