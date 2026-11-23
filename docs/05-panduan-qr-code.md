# Bagian 5: Panduan Paket Aset QR Code Resmi

> **Website Resmi SMP Wijaya Sukodono**  
> 📥 **Unduh Versi Microsoft Word**: [05-panduan-qr-code.docx](05-panduan-qr-code.docx)  
> Navigasi: [Kembali ke Bagian 4: SOP Operator](04-sop-operator.md) | [Indeks Dokumentasi](README.md)

---

## 5.1 Ringkasan Panduan

Dokumen ini berisi panduan penggunaan paket aset QR Code resmi untuk website **SMP Wijaya Sukodono** (`https://smpwijayasukodono.sch.id`). Seluruh aset dirancang agar praktis ditempelkan pada materi promosi digital (foto, poster, video) maupun media cetak fisik.

---

## 5.2 📦 Isi Paket Aset (`qr-kit-smpwijayasukodono.zip`)

| File Aset | Format & Resolusi | Kegunaan Utama & Karakteristik |
| :--- | :--- | :--- |
| **`qr-badge-smpwijayasukodono.png`** | PNG transparan luar (1200×1480 px) | **Siap tempel langsung** di foto & video (CapCut, Canva, Premiere). Sudah memakai kartu putih sudut membulat, bayangan lembut agar kontras di latar gelap/terang, serta label domain dan nama sekolah. |
| **`qr-plain-smpwijayasukodono.png`** | PNG latar putih (1500×1500 px) | QR polos beresolusi tinggi bila ingin didesain ulang di Canva/Figma atau ditempeli logo sekolah di bagian tengah. |
| **`qr-smpwijayasukodono.svg`** | Vektor SVG murni | File master yang tidak akan pecah saat diperbesar untuk kebutuhan cetak spanduk, brosur, atau video resolusi tinggi 4K. |

---

## 5.3 ⚙️ Spesifikasi Teknis QR Code

* **URL Tujuan**: `https://smpwijayasukodono.sch.id`
* **Tipe QR Code**: **Statis Permanen**  
  Tidak menggunakan layanan tautan perantara berbayar (non-redirect tracking pihak ketiga) sehingga tidak akan kedaluwarsa dan selalu aktif selamanya selama domain website sekolah dapat diakses.
* **Error Correction Level**: **Level H (High / 30%)**  
  Pola QR code tetap dapat dipindai dengan akurat meskipun gambar/video mengalami kompresi otomatis media sosial atau saat disisipkan logo kecil di bagian tengahnya.

---

## 5.4 🎨 Panduan Penggunaan di Berbagai Media Promosi

### 1. Foto & Poster Digital (Instagram Feed, Status WhatsApp, Facebook)
* Gunakan file **`qr-badge-smpwijayasukodono.png`** agar langsung terlihat rapi dan elegan tanpa perlu membuat bingkai tambahan manual.
* Posisikan di **pojok kanan bawah** atau **kiri bawah** dengan proporsi ukuran minimal **12–15%** dari total lebar poster.
* Beri jarak aman dari tepi kanvas (jangan menempel terlalu mepet) agar tidak terpotong (*crop*) otomatis saat dipratinjau di feed media sosial.

### 2. Video Vertikal (TikTok, Instagram Reels, YouTube Shorts)
* Tempatkan **`qr-badge-smpwijayasukodono.png`** di **pojok kiri atas** atau tampilkan di **tengah layar pada sekuens akhir (*outro*)**.
* Tampilkan minimal selama **5–8 detik** agar penonton memiliki waktu yang cukup untuk memindai dengan perangkat lain atau mengambil tangkapan layar (*screenshot*).
* **Penting**: Hindari menaruh QR Code di area kanan bawah dan bawah tengah karena area tersebut tertutup tombol *Like*, *Comment*, *Share*, serta teks *caption* bawaan aplikasi.

### 3. Video Horizontal (YouTube 16:9, TV Informasi / Videotron Sekolah)
* Tempatkan **`qr-badge-smpwijayasukodono.png`** di pojok kiri bawah atau kanan bawah (lebar minimal 150–200 px pada resolusi Full HD 1080p).
* Untuk produksi video beresolusi 4K, manfaatkan file vektor **`qr-smpwijayasukodono.svg`** agar tepi garis kode tetap tajam sempurna.

### 4. Desain Ulang & Media Cetak Fisik (Spanduk, Baliho, Banner, Brosur)
* Gunakan **`qr-smpwijayasukodono.svg`** untuk kebutuhan cetak skala besar agar pola QR tidak buram atau pecah ketika dicetak dalam meteran.
* Jika menggunakan **`qr-plain-smpwijayasukodono.png`** untuk tata letak khusus atau menyematkan logo sekolah di bagian tengah QR:
  * Pastikan luas logo tidak melebihi **20%** dari total luas QR Code agar tidak mengganggu pola pemindaian.
  * Pertahankan ruang kosong putih (*quiet zone*) di sekeliling QR Code minimal selebar 4 kotak modul QR agar sensor kamera mudah mengunci fokus.

---

## 5.5 ✅ Checklist Pengujian Sebelum Publikasi

Sebelum materi promosi dipublikasikan secara umum atau dicetak massal:
1. Lakukan **uji pindai nyata (*real scan test*)** menggunakan kamera bawaan ponsel (Android Google Lens dan iPhone Camera).
2. Pastikan hasil pemindaian langsung memunculkan tautan `https://smpwijayasukodono.sch.id` tanpa jeda eror.
3. Cek apakah tampilan website terbuka dengan sempurna di peramban ponsel.
