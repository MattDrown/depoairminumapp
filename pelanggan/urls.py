from django.urls import path
from . import views

urlpatterns = [
    # Ini artinya kalau buka halaman utama, panggil fungsi dashboard
    path('', views.dashboard, name='dashboard'),
    path('tambah/', views.tambah_pelanggan, name='tambah_pelanggan'),
]