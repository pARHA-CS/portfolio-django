from django.db import models

# About Model
class About(models.Model):
    short_description: models.TextField = models.TextField()
    description: models.TextField = models.TextField()
    image = models.ImageField(upload_to ="about")
    
    class Meta:
        verbose_name = "À propos de moi"
        verbose_name_plural = "À propos de moi"
        
    def __str__(self):
        return "À propos de moi"

# Service Model
class Service(models.Model):
    name: models.CharField = models.CharField(max_length=100, verbose_name="Nom du service")
    description: models.TextField = models.TextField(verbose_name="À propos du service")
    
    def __str__(self):
        return self.name
    
# Recent Work Model
class RecentWork(models.Model):
    title:models.CharField = models.CharField(max_length=100, verbose_name= "Nom du projet")
    description: models.TextField = models.TextField()
    technology: models.CharField = models.CharField(max_length=20)
    image = models.ImageField(upload_to = "projets")
    
    def __str__(self):
        return self.title
    
#CLient Model
class Client(models.Model):
    name: models.CharField = models.CharField(max_length=100, verbose_name="Nom du client")
    description: models.TextField = models.TextField(verbose_name="Demande du client")
    image = models.ImageField(upload_to = "clients", default="default.png")
    
    def __str__(self):
        return self.name