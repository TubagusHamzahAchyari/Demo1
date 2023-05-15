import barcode
import qrcode
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
    cutomer_data = models.ForeignKey(CustomerData, null=True, blank=True, on_delete=models.CASCADE)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}{self.customer_data.name}', writer=ImageWriter())
        code.write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):  # overriding save()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.name)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.qr_code.save(f'{self.name}.png', File(buffer), save=False)
        super().save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)