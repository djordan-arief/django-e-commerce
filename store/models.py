from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Database table
class Category(models.Model):

    # database fields
    name = models.CharField(max_length=255, db_index= True)
    slug = models.SlugField(max_length=255, unique= True)

    class Meta:
        verbose_name_plural = 'categories'

    # string representation of the class
    def __str__(self):
        return self.name
    

# Database table
class Product(models.Model):

    # database fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    author = models.CharField(max_length= 255)
    title = models.CharField(max_length= 255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    # string representation of the class
    def __str__(self):
        return self.title
    