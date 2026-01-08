from django.shortcuts import render
from .models import Pelanggan
import json
from django.shortcuts import render, redirect

def dashboard(request):
    # Ambil semua data pelanggan yang punya koordinat lengkap
    data_pelanggan = Pelanggan.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
    
    # Kita susun datanya biar enak dibaca sama JavaScript nanti
    list_lokasi = []
    for p in data_pelanggan:
        # Cek ada foto atau enggak
        foto_url = p.foto_lokasi.url if p.foto_lokasi else ""
        
        list_lokasi.append({
            'nama': p.nama,
            'lat': float(p.latitude),
            'lng': float(p.longitude),
            'alamat': p.alamat,
            'foto': foto_url
        })
    
    context = {
        # Convert list Python jadi JSON String biar bisa dibaca JS
        'lokasi_json': json.dumps(list_lokasi) 
    }
    
    return render(request, 'pelanggan/dashboard.html', context)

def tambah_pelanggan(request):
    if request.method == 'POST':
        # Ambil data dari form HTML
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')
        alamat = request.POST.get('alamat')
        lat = request.POST.get('latitude')
        lng = request.POST.get('longitude')
        foto = request.FILES.get('foto_lokasi') # Ingat, file ambilnya pakai FILES

        # Simpan ke Database
        Pelanggan.objects.create(
            nama=nama,
            no_hp=no_hp,
            alamat=alamat,
            latitude=lat,
            longitude=lng,
            foto_lokasi=foto
        )
        
        # Setelah simpan, balik ke dashboard
        return redirect('dashboard')

    return render(request, 'pelanggan/tambah_pelanggan.html')