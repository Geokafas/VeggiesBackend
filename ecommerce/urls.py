from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#Nav-bar title
admin.site.site_header = 'VeggieStreet'
#Browser tab title is "index_title"|"site_title"
admin.site.site_title  = 'VeggieStreet'
#Main container title
admin.site.index_title  = 'Administration panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
