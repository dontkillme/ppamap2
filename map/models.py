from django.db import models
from descriptions.models import Faction, Event, Place, CreationDataModel, Description

class Icon(models.Model):
  name = models.CharField(max_length = 255)
  image = models.ImageField(upload_to = "gfx/icons/")

  def __str__(self):
    return self.name


class POI(CreationDataModel):
  name = models.CharField(max_length = 255)
  lat = models.DecimalField(max_digits=13, decimal_places=9)
  long = models.DecimalField(max_digits=13, decimal_places=9)
  icon = models.ForeignKey(Icon, null = True)
  event = models.ForeignKey(Event, null = True)
  place = models.ForeignKey(Place, null = True)
  main_faction = models.ForeignKey(Faction, null = True, related_name = "poi_main_faction")
  related_factions = models.ManyToManyField(Faction, blank = True)
  description = models.ForeignKey(Description, null = True)

  def __str__(self):
    return self.name
  
  
class Polygons(CreationDataModel):
  name = models.CharField(max_length = 255)
  polygon = models.TextField()
  event = models.ForeignKey(Event, null = True)
  place = models.ForeignKey(Place, null = True)
  main_faction = models.ForeignKey(Faction, null = True, related_name = "poly_main_faction")
  related_factions = models.ManyToManyField(Faction, blank = True)
  description = models.ForeignKey(Description, null = True)
  
  def __str__(self):
    return self.name