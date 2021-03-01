from django.db import models
from product.models import Product
# Create your models here.
class Event(models.Model):
    description = models.TextField(blank=True)
    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField(auto_now_add=True)
class EventDetail(models.Model):
    event_id = models.ForeignKey(Event, related_name='EventId', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,related_name='ProductIdEvent',on_delete=models.CASCADE)
    discount = models.IntegerField(default='')