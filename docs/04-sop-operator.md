# Bagian 4: SOP Pengelolaan Website Resmi & Serah Terima Akun

> **Panduan Siap Cetak untuk Operator Tata Usaha (TU), Guru, dan Pembina Sekolah**  
> 📥 **Unduh Versi Microsoft Word**: [04-sop-operator.docx](04-sop-operator.docx)  
> Navigasi: [Kembali ke Bagian 3: Design System](03-design-system.md) | [Indeks Dokumentasi](README.md) | [Lanjut ke Bagian 5: Panduan QR Code](05-panduan-qr-code.md)

---

## 4.1 Cara Login ke Dashboard Pengelola (Pages CMS)

Pengelolaan konten website tidak memerlukan akses server atau akun GitHub. Operator sekolah dapat masuk dengan tautan aman tanpa kata sandi:

1. Buka peramban (*browser*) di komputer atau ponsel, lalu kunjungi:  
   👉 **`https://app.pagescms.org`**
2. Masukkan alamat email pengelola yang telah didaftarkan (misal: `tatausaha.smpwijaya@gmail.com`).
3. Buka kotak masuk email tersebut, cari email dari **Pages CMS**, lalu klik tombol/tautan **Sign in / Magic Link**.
4. Anda akan langsung masuk ke dashboard administrasi website SMP Wijaya Sukodono tanpa perlu mengingat kata sandi yang rumit.

---

## 4.2 Cara Menambah & Mengelola Berita Baru

1. Pada menu navigasi sisi kiri dashboard, klik menu **Berita & Pengumuman**.
2. Klik tombol **Add an entry** (Tambah Baru) di sudut kanan atas.
3. Lengkapi formulir isian:
   - **Judul Berita**: Tuliskan judul kegiatan secara jelas dan menarik.
   - **Tanggal Publikasi**: Pilih tanggal pelaksanaan atau publikasi.
   - **Kategori**: Pilih salah satu (`Kegiatan`, `Prestasi`, `Pengumuman`, atau `Akademik`).
   - **Ringkasan Singkat**: Masukkan 1–2 kalimat pengantar (akan tampil pada kartu cuplikan berita di halaman beranda).
   - **Foto Sampul**: Unggah foto utama berorientasi mendatar/landscape (ukuran maksimal 500 KB).
   - **Isi Berita**: Tuliskan narasi lengkap berita. Anda dapat menggunakan format tebal, miring, daftar poin, dan menambahkan foto di dalam naskah.
4. Pastikan opsi **Simpan sebagai Draft** dalam posisi nonaktif (**off**) bila ingin langsung tayang.
5. Klik tombol **Save**. Sistem akan otomatis memproses dan memperbarui website publik dalam waktu **30–60 detik**.

---

## 4.3 Cara Mengatur SPMB, Fasilitas, & Data Guru

### A. Pengaturan SPMB (Penerimaan Siswa Baru)
1. Buka menu **Pengaturan SPMB (Penerimaan Siswa Baru)** pada panel navigasi.
2. **Buka/Tutup Pendaftaran**:
   - Beri tanda centang pada **Status SPMB Dibuka?** untuk membuka penerimaan siswa baru.
   - Hapus tanda centang jika kuota telah terpenuhi atau periode belum dibuka. Website secara cerdas akan mengganti tombol pendaftaran dengan tombol WhatsApp TU serta menampilkan pesan penutupan resmi.
3. **Tahun Ajaran & Banner Berjalan**: Sesuaikan tahun ajaran aktif (misal `2026/2027` atau `2027/2028`) dan isi pesan teks notifikasi running banner di bilah atas website.
4. **Jadwal Gelombang & Biaya/Beasiswa**: Perbarui tanggal gelombang inden/reguler, syarat administrasi berkas, dan keterangan program beasiswa/KIP.
5. **Formulir & Kontak Panitia**: Perbarui URL tautan Google Forms pendaftaran, unggah berkas brosur digital PDF, dan isi nomor kontak WhatsApp panitia SPMB.
6. Klik **Save**.

### B. Memperbarui Data Guru & Staf
1. Buka menu **Direktori Guru & Staf**.
2. Klik tombol `+` untuk menambahkan staf/guru baru, atau klik data guru yang sudah ada untuk mengubah jabatan, bidang mata pelajaran, atau foto profil (rasio persegi 1:1).
3. Klik **Save**.

### C. Mengelola Fasilitas & Ekstrakurikuler (Foto Banyak / Galeri)
1. Buka menu **Fasilitas Sekolah** atau **Ekstrakurikuler**.
2. Setiap item memiliki kolom **Foto Sampul Utama** serta kolom **Galeri Foto Tambahan (List)**.
3. Klik tombol `+` pada galeri foto tambahan untuk memasukkan foto ke-2, ke-3, dst.
4. Pada website publik, foto-foto tersebut akan disajikan dalam tampilan modal lightbox interaktif lengkap dengan navigasi panah, thumbnail, dan penghitung foto.
5. Klik **Save**.

### D. Mengubah Foto & Konten Hero Utama (Beranda)
1. Buka menu **Pengaturan Sekolah & Beranda** pada panel navigasi sisi kiri Pages CMS.
2. Cari bagian **Hero Utama / Banner Beranda**:
   - **Foto Latar Belakang Hero**: Klik kolom foto untuk mengunggah atau memilih foto sampul beranda baru (disarankan rasio mendatar 16:9, resolusi 1600×900 px, ukuran di bawah 500 KB dalam format WebP/JPG).
   - **Teks Label / Badge Atas**: Sesuaikan teks badge di atas judul, atau biarkan kosong agar otomatis menggunakan `NPSN • AKREDITASI • SIDOARJO`.
   - **Judul Utama Hero & Teks Sorotan Emas**: Sesuaikan kalimat utama beranda. Isian *Teks Sorotan Emas* akan otomatis diberi warna aksen emas almamater.
   - **Deskripsi / Tagline Singkat**: Kalimat pengantar sekolah di bawah judul utama.
   - **Tombol Utama & Tombol Kedua**: Sesuaikan teks tombol dan tautan tujuan (default mengarah ke `/spmb` dan `/profil`).
3. Klik tombol **Save** di sudut kanan atas untuk mempublikasikan perubahan ke website.

---

## 4.4 Panduan Kompresi Gambar Sebelum Upload

Untuk menjaga kecepatan akses website sekolah di perangkat ponsel wali murid dan menghemat ruang repositori Git, **seluruh foto wajib dikompresi terlebih dahulu** sehingga berukuran di bawah **500 KB** (jangan mengunggah file foto mentah kamera berukuran 3 MB – 10 MB).

### Alat Kompresi Online Cepat (Gratis & Tanpa Instal Aplikasi):
1. **TinyPNG / TinyJPG** (`https://tinypng.com`)
   - Buka website, seret (*drag and drop*) foto ke layar, tunggu proses kompresi otomatis, lalu unduh hasilnya.
2. **Squoosh by Google** (`https://squoosh.app`)
   - Unggah foto, pilih format output **WebP** atau **MozJPEG**, atur *Quality* ke 75–80%, dan tetapkan lebar maksimal (*resize width*) ke **1200 px** atau **1600 px**.
3. **ILoveIMG** (`https://www.iloveimg.com/compress-image`)
   - Praktis untuk mengompresi puluhan foto kegiatan sekaligus dalam satu kali klik.

---

## 4.5 Lembar Serah Terima Akun & Catatan Perpanjangan Domain

| Item Layanan Digital | Informasi Akun Resmi |
| :--- | :--- |
| **Alamat Website Resmi** | `https://smpwijayasukodono.sch.id` |
| **Email Induk Sekolah (Gmail)** | `smpwijayas@gmail.com` |
| **Penyedia Registrar Domain .sch.id** | Rumahweb |
| **Estimasi Biaya Perpanjangan** | Rp 60.000 / tahun |
| **Jatuh Tempo Perpanjangan** | 1 tahun sekali sejak tanggal aktivasi domain |
| **Layanan Hosting & CDN** | Cloudflare Pages (Free Tier — Biaya Rp 0) |
| **Penyimpanan Repositori Kode** | GitHub Private Repository (Biaya Rp 0) |
