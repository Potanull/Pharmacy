from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', include('main.urls')),
    path('database/', include('database.urls')),
    path('users/', include('users.urls')),
    path('client/', include('client.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)