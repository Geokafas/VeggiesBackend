from django.shortcuts import render
from .models import Item, ItemRatings, ItemReviews
from rest_framework import viewsets
from .serializers import ItemSerializer, ItemRatingsSerializer, ItemReviewsSerializer
from django.utils.translation import gettext as _

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemsRatingsViewSet(viewsets.ModelViewSet):
    queryset = ItemRatings.objects.all()
    serializer_class = ItemRatingsSerializer

class ItemsReviewsViewSet(viewsets.ModelViewSet):
    queryset = ItemReviews.objects.all()
    serializer_class = ItemReviewsSerializer