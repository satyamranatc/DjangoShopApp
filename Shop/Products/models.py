from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="ProductImage/")
    Description = models.CharField(max_length=1000)
    Category = models.CharField(max_length=500)



