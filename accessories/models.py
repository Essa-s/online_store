from django.db import models
from utl import path_and_rename

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

CHOICES = [(i,f'{i}') for i in range(1,6)]
class Accessories(models.Model):
    class Meta:
        verbose_name_plural = "Accessories"
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    stars = models.IntegerField(choices=CHOICES)
    image = models.ImageField(upload_to=path_and_rename)
    catgory = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    