import uuid
from django.db import models
from django.contrib.auth.models import User

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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=127)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null= True)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_booming_product(self):
        return self.product_views > 50
    
    def increment_views(self):
        self.product_views += 1
        self.save()