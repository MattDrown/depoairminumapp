document.addEventListener('DOMContentLoaded', function() {
    // Cek apakah kita ada di halaman tambah/edit pelanggan
    const latField = document.getElementById('id_latitude');
    const longField = document.getElementById('id_longitude');

    if (latField && longField) {
        // Buat container untuk peta di atas field latitude
        const mapContainer = document.createElement('div');
        mapContainer.id = 'map';
        mapContainer.style.height = '400px';
        mapContainer.style.width = '100%';
        mapContainer.style.marginBottom = '20px';
        
        // Sisipkan peta sebelum field latitude
        latField.closest('.form-row').parentNode.insertBefore(mapContainer, latField.closest('.form-row'));

        // Koordinat Default (Tenggarong)
        let defaultLat = -0.4234; 
        let defaultLng = 116.9854;
        let zoomLevel = 13;

        // Kalau lagi edit data (sudah ada isinya), pakai koordinat yang ada
        if (latField.value && longField.value) {
            defaultLat = latField.value;
            defaultLng = longField.value;
            zoomLevel = 16; // Lebih zoom in kalau sudah ada lokasi
        }

        // Inisialisasi Peta Leaflet
        const map = L.map('map').setView([defaultLat, defaultLng], zoomLevel);

        // Pakai Tile dari OpenStreetMap (Gratis)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // Marker (Pin)
        let marker;

        // Kalau sudah ada koordinat, pasang marker
        if (latField.value && longField.value) {
            marker = L.marker([defaultLat, defaultLng]).addTo(map);
        }

        // Event: Saat peta diklik
        map.on('click', function(e) {
            const lat = e.latlng.lat;
            const lng = e.latlng.lng;

            // Update field input
            latField.value = lat.toFixed(6);
            longField.value = lng.toFixed(6);

            // Pindahkan marker
            if (marker) {
                marker.setLatLng(e.latlng);
            } else {
                marker = L.marker(e.latlng).addTo(map);
            }
        });
    }
});