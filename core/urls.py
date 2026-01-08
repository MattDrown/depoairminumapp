from django.contrib import admin
from django.urls import path, include  # <--- Pastikan ada include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Kita arahkan URL utama ('') ke file urls milik aplikasi pelanggan
    path('', include('pelanggan.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)