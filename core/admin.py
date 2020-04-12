from django.contrib import admin
from .models import Item, ItemRatings, ItemReviews

admin.site.register(Item)
admin.site.register(ItemRatings)
admin.site.register(ItemReviews)