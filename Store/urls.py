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
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls'), name='orders'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))