# Generated by Django 4.2.1 on 2023-05-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entryrecording', '0003_customer_cutomer_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
