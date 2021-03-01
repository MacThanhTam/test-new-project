from django.db import models
import locale
from django.urls import  reverse
# Create your models here.
status_choices = (
    ('Full','Còn hàng'),
    ('Empty','Hết hàng'),
    )
class Category(models.Model):
    category_name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.category_name
        
class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    category_id = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/products',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    author = models.CharField(max_length=200, db_index=True)
    ISBM = models.IntegerField(default='')
    publish = models.DateField()
    publisher = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices= status_choices)
    page_number = models.IntegerField(default='')
    cover_type = models.CharField(max_length=50, default='')
    size = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ('title',)
        index_together = (('id','slug'),)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product:product_detail',args=[self.id,self.slug])
        # return reverse('product.views.product_detail', args=[str(self.id)])
class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/images/products')

    def __str__(self):
        return self.product.title

