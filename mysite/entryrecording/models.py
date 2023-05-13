import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.db import models



# make Customers Model
class CustomerData(models.Model):
    customer_number = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=50)
    postal_zip = models.CharField(max_length=15)
    region = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

class Purchase(models.Model):
    purchase_number = models.CharField(max_length=15, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    comment = models.CharField(max_length=50)

# Barcode
class Customer(models.Model):
    name = models.CharField(max_length=50)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # overriding save()
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)