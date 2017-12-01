from rest_framework import serializers
from descriptions.models import Description, Event, Faction, Place
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('pk', 'username')

class DescriptionSerializer(serializers.ModelSerializer):
  mod_user = UserSerializer(source='modification_user', read_only = True)
  creator_user = UserSerializer(source='creator', read_only = True)
  
  class Meta:
    model = Description
    fields = ('pk', 'name', 'text', 'author', 'creation_date', 'modification_date', 'mod_user', 'creator_user')