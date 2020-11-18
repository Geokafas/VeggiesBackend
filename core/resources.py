# this module is responsible for importing and exporting products from/to files.
#django-import-export-2.4.0 is the library
from import_export import resources
from .models import Item

class ItemResource(resources.ModelResource):

    class Meta:
        model = Item
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('product_id',)
        exclude = ('product_picture')