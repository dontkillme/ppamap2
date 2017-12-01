from django.contrib.auth.models import User
from django.db import models


class DescriptionModel(models.Model):
  name = models.CharField(max_length = 255)
  text = models.TextField(blank = True, null = True)
  
  def __str__(self):
    return self.name

  class Meta:
    abstract = True
    
    
class CreationDataModel(models.Model):
  creation_date = models.DateTimeField(auto_now_add = True)
  creator = models.ForeignKey(User, related_name = "+")
  modification_date = models.DateTimeField(auto_now = True)  
  modification_user = models.ForeignKey(User, related_name = "+")

  def __str__(self):
    return self.author
  
  class Meta:
    abstract = True


class Faction(DescriptionModel):
  logo = models.ImageField(upload_to = "faction/logos/")


class Event(DescriptionModel):
  date_from = models.DateTimeField()
  date_to = models.DateTimeField()


class Place(DescriptionModel):
  start_date = models.DateField()


class Description(DescriptionModel, CreationDataModel):
  author = models.CharField(max_length = 255)