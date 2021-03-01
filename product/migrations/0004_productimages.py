# Generated by Django 3.1.5 on 2021-02-25 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210220_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to='images/products/')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
