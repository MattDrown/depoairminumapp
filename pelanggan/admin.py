from django.contrib import admin
from .models import Pelanggan

@admin.register(Pelanggan)
class PelangganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'no_hp', 'alamat', 'latitude', 'longitude')
    search_fields = ('nama', 'alamat')

    class Media:
        # Load CSS Leaflet (CDN Online biar cepet)
         css = {
            'all': ('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',)
        }
        # Load JS Leaflet & Script buatan kita tadi
         js = (
            'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
            'pelanggan/js/admin_map.js', 
        )