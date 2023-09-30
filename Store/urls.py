from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app import urls
from products import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'), name='index'),
    path('products/', include('products.urls'), name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
