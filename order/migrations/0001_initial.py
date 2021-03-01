# Generated by Django 3.1.5 on 2021-01-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='', max_length=200)),
                ('total_price', models.IntegerField(default='')),
                ('delivery_info', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField(default=0)),
                ('price', models.IntegerField(default='')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderId', to='order.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductId', to='product.product')),
            ],
        ),
    ]
