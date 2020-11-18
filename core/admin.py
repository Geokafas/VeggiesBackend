from django.contrib import admin
from .models import Item, ItemRatings, ItemReviews
from import_export.admin import ImportExportModelAdmin
from .resources import *

class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource

admin.site.register(Item,ItemAdmin)
admin.site.register(ItemRatings)
admin.site.register(ItemReviews)

