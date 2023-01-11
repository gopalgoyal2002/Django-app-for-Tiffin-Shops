from django.db import models

# Create your models here.
class Products(models.Model):
    product_image = models.ImageField(blank=True, null=True, upload_to = "static/1_products_img")
    product_title = models.CharField(blank=True, null=True, max_length = 250)
    product_price = models.IntegerField(blank=True, null=True)
    offer_price = models.CharField(blank=True, null=True, max_length = 250)
    created_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return str(self.product_title)
