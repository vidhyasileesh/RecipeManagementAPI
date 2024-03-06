from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Recipie(models.Model):
    name=models.CharField(max_length=200)
    ingredients=models.TextField()
    cuisine=models.CharField(max_length=300)
    meal_type=models.CharField(max_length=300)
    created_on=models.DateTimeField(auto_now_add=True)
    edited_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review_or_Comment(models.Model):
    recipie_id=models.ForeignKey(Recipie,related_name='reviews',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(null=True,blank=True)
    review=models.TextField()
    comment=models.CharField(max_length=600,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.recipie_id.name
