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

class Mail(models.Model):
    SERVICES_CHOICES = (
        ('bricolage', 'Bricolage'),
        ('jardinage', 'Jardinage'),
        ('demenagement', 'Demenagement'),
        ('menage-repassage', 'Menage/Repassage'),
        ('assemblage-meuble', 'Assemblage meuble'),
        ('informatique', 'Informatique'),
        ('ramassage-livraison', 'Rammassage et livraison'),
        ('animaux', 'Animaux'),
        ('evenementiel', 'Evenementiel'),
        ('prestation-administratif', 'Prestations Administratif'),
        ('service-personne', 'Service à la personne'),
    )
    
    address = models.EmailField()
    service = models.CharField(choices=SERVICES_CHOICES)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.address
