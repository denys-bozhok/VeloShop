from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'), name='index'),
    path('products/', include('products.urls'), name='products'),
    path('users/', include('users.urls'), name='users'),
    path('carts/', include('carts.urls'), name='carts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
