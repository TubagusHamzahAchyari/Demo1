# Generated by Django 4.2.1 on 2023-05-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entryrecording', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes/'),
        ),
    ]
