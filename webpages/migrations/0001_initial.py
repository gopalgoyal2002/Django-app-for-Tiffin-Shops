# Generated by Django 3.2.16 on 2023-01-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='1_products_img')),
                ('product_title', models.CharField(blank=True, max_length=250, null=True)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('offer_price', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]