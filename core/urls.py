from django.urls import include, path
#from .views import item_list
from rest_framework import routers
from . import views

app_name = 'core'

# urlpatterns = [
#     path('', item_list, name='item-list')
# ]


router = routers.DefaultRouter()
router.register(r'item', views.ItemsViewSet)
router.register(r'itemRatings', views.ItemsRatingsViewSet)
router.register(r'itemReviews', views.ItemsReviewsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]