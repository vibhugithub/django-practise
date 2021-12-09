from django.db import models
from django.db.models import Model
# Create your models 
class Email(models.Model):
    email = models.EmailField(max_length=254)