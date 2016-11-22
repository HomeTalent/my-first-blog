# -*- coding: utf8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class MultiSelectField(models.Field):
    __metaclass__ = models.SubfieldBase

    def get_internal_type(self):
        return "CharField"

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def _get_FIELD_display(self, field):
        value = getattr(self, field.attname)
        choicedict = dict(field.choices)

    def formfield(self, **kwargs):
        # don't call super, as that overrides default widget if it has choices
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name), 
                    'help_text': self.help_text, 'choices':self.choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultiSelectFormField(**defaults)

    def get_db_prep_value(self, value):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return ",".join(value)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        return value.split(",")

    def contribute_to_class(self, cls, name):
        super(MultiSelectField, self).contribute_to_class(cls, name)
        if self.choices:
            func = lambda self, fieldname = name, choicedict = dict(self.choices):",".join([choicedict.get(value,value) for value in getattr(self,fieldname)])
            setattr(cls, 'get_%s_display' % self.name, func)

class Mail(models.Model):
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

    USER_TYPES = (
        ('A', 'ASKER'),
        ('T', 'TASKER')
    )
    
    address = models.EmailField()
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPES,
        default='A'
    )
    service = models.MultiSelectField(
        max_length=254,
        choices=SERVICES_CHOICES
    )
    created_date = models.DateTimeField(
        default=timezone.now
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.address
