from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    directions = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
