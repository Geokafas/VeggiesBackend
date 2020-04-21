from rest_framework import serializers

from .models import Item, ItemRatings, ItemReviews

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('product_title', 'product_price','product_id','product_picture','product_description','product_quantity','product_category')

class ItemRatingsSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ItemRatings
        fields = ('product_rating','product_id')

class ItemReviewsSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ItemReviews
        fields = ('product_review', 'pub_date','product_id')
