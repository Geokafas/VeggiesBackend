# this module is responsible for importing and exporting products from/to files.
from import_export import resources
from .models import Item

class ItemResource(resources.ModelResource):

    class Meta:
        model = Item
        skip_unchanged = True
        report_skipped = False
        exclude = ('product_picture')
        #fields = ('product_title','product_price','product_quantity','product_category')
        #export_order = ('id', 'price', 'author', 'name')