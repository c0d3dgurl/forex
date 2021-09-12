from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls'))
]

admin.site.site_header ='Forex'
admin.site.site_title ='Forex'
admin.site.index_title ='Welcome Admin'
admin.site.site_url = 'http://localhost:8080'  # Removes the 'View Site' link

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)