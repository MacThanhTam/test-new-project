from django.db import models
from user.models import CustomerUser
from product.models import Product
# Create your models here.
class Order(models.Model):
    user_id = models.ForeignKey(CustomerUser, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='',max_length=200)
    total_price = models.IntegerField(default='')
    delivery_info = models.CharField(max_length=200, default='')
class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order,related_name='OrderId',on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='ProductId',on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=0)
    price = models.IntegerField(default='')