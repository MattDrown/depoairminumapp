from django.db import models

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100, verbose_name="Nama Pelanggan")
    no_hp = models.CharField(max_length=20, verbose_name="Nomor HP/WA")
    alamat = models.TextField(verbose_name="Alamat Lengkap")
    
    # Koordinat (Latitude & Longitude)
    # Kita set null=True biar bisa disimpan dulu walau koordinat belum ada
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Foto Lokasi
    foto_lokasi = models.ImageField(upload_to='foto_pelanggan/', null=True, blank=True, verbose_name="Foto Depo/Rumah")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Data Pelanggan"