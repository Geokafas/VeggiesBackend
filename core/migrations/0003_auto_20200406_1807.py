# Generated by Django 2.2.8 on 2020-04-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200406_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product_picture',
            field=models.ImageField(default='no-img.jpg', upload_to='items/'),
        ),
    ]
