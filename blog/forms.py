# -*- coding: utf8 -*-

from django import forms
from .models import Post
from .models import Mail

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class MailFormAsker(forms.ModelForm):

    class Meta:

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

        services = forms.MultipleChoiceField(widget=forms.SelectMultiple,

        model = Mail
        exclude = ['service']
        fields = ('services','address','user_type')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
            'user_type': forms.HiddenInput()
        }
        labels = {
            'services': 'Mes besoins !',
            'address': ''
        }

class MailFormTasker(forms.ModelForm):

    class Meta:
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

        services = forms.MultipleChoiceField(widget=forms.SelectMultiple, 
                                            choices=SERVICES_CHOICES)

        model = Mail
        exclude = ['service']
        fields = ('services', 'address','user_type')
        widgets = {
            'address': forms.EmailInput(attrs={'placeholder': 'mail@example.com'}),
            'user_type': forms.HiddenInput()
        }
        labels = {
            'services': 'Mes talents !',
            'address': ''
        }
