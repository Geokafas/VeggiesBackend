# Generated by Django 2.2.8 on 2020-04-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_itemratings_itemreviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemratings',
            name='product_rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
