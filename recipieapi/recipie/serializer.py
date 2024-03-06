from django.contrib.auth.models import User
from rest_framework import serializers

from recipie.models import Recipie,Review_or_Comment


class RecipieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Recipie
        fields=['name','ingredients','cuisine','meal_type','created_on','edited_at']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Review_or_Comment
        fields=['recipie_id','user','rating','review','comment','created_at']


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)           #Password hide chythu veykn use chyunne code

    class Meta:
        model=User
        fields=['id','username','password']

    def create(self, validated_data):  #after validation      (password Encrypted)
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u
