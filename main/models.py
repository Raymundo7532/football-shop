import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('t-shirt', 'T-shirt'),
        ('pants', 'Pants'),
        ('socks', 'Socks'),
        ('shoes', 'Shoes'),
        ('goalkeeper glove', 'Goalkeeper Glove'),
        ('ball', 'Ball'),
        ('tumbler', 'Tumbler'),
    ]

    name = models.CharField(max_length=127)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null= True)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_booming_product(self):
        return self.product_views > 20000
    
    def increment_views(self):
        self.product_views += 1
        self.save()

class Employee(models.Model):
    nama = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    persona = models.TextField()

    def get_name(self):
        return self.nama
    
    def get_age(self):
        return self.age
    
    def get_persona(self):
        return self.persona