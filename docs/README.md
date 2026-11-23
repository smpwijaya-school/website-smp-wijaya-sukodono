# Dokumentasi Resmi Pengembangan & Operasional Website SMP Wijaya Sukodono

Selamat datang di pusat dokumentasi resmi website **SMP Wijaya Sukodono** (`https://smpwijayasukodono.sch.id`).

Dokumentasi ini disusun secara modular agar memudahkan seluruh pihak—mulai dari pimpinan sekolah, panitia SPMB, operator Tata Usaha (TU), tim media/humas, hingga pengembang teknis—dalam memahami, mengelola, dan mengembangkan sistem informasi sekolah.

---

## 📌 Ringkasan Identitas Institusi & Proyek

| Atribut | Keterangan Resmi |
| :--- | :--- |
| **Nama Sekolah** | SMP Wijaya Sukodono (Jenjang SMP Swasta) |
| **NPSN / Akreditasi** | 20540036 / Terakreditasi B |
| **Alamat Resmi** | Desa Pekarungan, Kec. Sukodono, Kab. Sidoarjo, Jawa Timur 61258 |
| **Kontak Telepon** | (031) 8830995 |
| **Kepala Sekolah** | Yennis Fitriyan, S.E., M.Pd. |
| **Model Proyek** | Kontribusi Sukarela Alumni (Pro Bono) — *Ultra Low-Maintenance* |
| **Arsitektur Teknologi** | Astro + Tailwind CSS v4 + Pages CMS + GitHub + Cloudflare Pages |
| **Estimasi Biaya Rutin** | ± Rp 55.000 – Rp 70.000 / tahun (Hanya perpanjangan domain resmi `.sch.id`) |

---

## 📚 Peta & Daftar Dokumen

Silakan pilih bagian dokumen di bawah ini sesuai dengan kebutuhan Anda:

| Dokumen | Sasaran Pembaca | Topik Pembahasan |
| :--- | :--- | :--- |
| 📄 **[Bagian 1: Product Requirements Document (PRD)](01-prd.md)** | Tim Pengembang & Manajemen Sekolah | Latar belakang proyek, analisis kebutuhan pengguna, peta 9 halaman website, batasan ruang lingkup (*out of scope*), serta rincian efisiensi biaya operasional tahunan. |
| 🏗️ **[Bagian 2: Arsitektur & GitOps](02-arsitektur.md)** | Developer & Maintainer Teknis | Diagram alur kerja GitOps Static Site, struktur direktori repositori lengkap, konfigurasi Cloudflare Pages, security headers, dan edge redirects. |
| 🎨 **[Bagian 3: Spesifikasi Sistem Desain](03-design-system.md)** | Desainer UI & Tim Kreatif | Filosofi lambang sekolah, palet warna resmi (hex codes), hierarki tipografi (*Plus Jakarta Sans* & *JetBrains Mono*), aspek rasio gambar, dan standar aksesibilitas UI. |
| 📋 **[Bagian 4: SOP Operator & Pengelolaan Website](04-sop-operator.md)** <br>*(Tersedia format [Word .docx](04-sop-operator.docx))* | Operator TU, Guru, & Pembina OSIS | Panduan masuk ke dashboard Pages CMS (tanpa kata sandi), alur penulisan berita, cara membuka/menutup pendaftaran SPMB, tips kompresi gambar, dan lembar serah terima akun. |
| 📱 **[Bagian 5: Panduan Aset QR Code Resmi](05-panduan-qr-code.md)** <br>*(Tersedia format [Word .docx](05-panduan-qr-code.docx))* | Tim Publikasi, Humas, & Editor Video | Spesifikasi teknis QR code permanen (Level H), panduan penempelan pada poster Instagram/WA, video vertikal TikTok/Reels, video horizontal YouTube, dan media cetak fisik. |

---

## 🧭 Panduan Cepat Berdasarkan Peran

### 1. Bagi Pengembang / Kontributor Teknis
1. Pelajari spesifikasi arsitektur di [02-arsitektur.md](02-arsitektur.md).
2. Jalankan perintah instalasi dan pengembangan:
   ```bash
   npm install
   npm run dev
   ```
3. Pastikan memvalidasi skema data sebelum melakukan komit:
   ```bash
   npm run check
   ```

### 2. Bagi Operator Tata Usaha (TU) & Bapak/Ibu Guru
1. Baca panduan operasional pada [04-sop-operator.md](04-sop-operator.md).
2. Kunjungi dashboard CMS di `https://app.pagescms.org` dan masuk via tautan email resmi.
3. Unggah foto kegiatan langsung melalui Pages CMS. Sistem secara otomatis akan me-resize dan mengompresi foto di latar belakang agar website selalu cepat dibuka oleh wali murid. Anda juga dapat menggunakan tombol **"⚡ Kompres Foto Upload"** di dalam CMS jika diperlukan.

### 3. Bagi Tim Humas, OSIS, & Media Promosi
1. Baca panduan aset QR code pada [05-panduan-qr-code.md](05-panduan-qr-code.md).
2. Gunakan `qr-badge-smpwijayasukodono.png` untuk materi konten media sosial dan `qr-smpwijayasukodono.svg` untuk media cetak spanduk atau baliho.
