# DOKUMENTASI INDUK PENGEMBANGAN & OPERASIONAL WEBSITE RESMI SMP WIJAYA SUKODONO

**Product Requirements Document (PRD), Arsitektur GitOps Static Site, Spesifikasi Design System, dan SOP Operator Sekolah**  
*NPSN 20540036 • AKREDITASI B • DESA PEKARUNGAN, KEC. SUKODONO, KAB. SIDOARJO*

---

## Ringkasan Proyek

| Atribut Proyek | Keterangan |
| :--- | :--- |
| **Nama Institusi** | SMP Wijaya Sukodono (Jenjang SMP — Swasta) |
| **NPSN / Akreditasi** | 20540036 / Terakreditasi B |
| **Alamat Resmi** | Desa Pekarungan, Kec. Sukodono, Kab. Sidoarjo, Jawa Timur 61258 |
| **Kontak Telepon** | (031) 8830995 |
| **Kepala Sekolah** | Yennis Fitriyan, S.E., M.Pd. |
| **Model Proyek** | Kontribusi Sukarela Alumni (Pro Bono) — Ultra Low-Maintenance |
| **Arsitektur Teknologi** | Astro + Tailwind CSS v4 + Pages CMS + GitHub + Cloudflare Pages |
| **Estimasi Biaya Rutin** | ± Rp 55.000 – Rp 70.000 / tahun (khusus perpanjangan domain .sch.id; hosting & CMS Rp 0) |
| **Versi Dokumen** | Versi 1.0 — November 2026 |

---

## BAGIAN 1: Product Requirements Document (PRD)

### 1.1 Ringkasan Proyek & Tujuan
Proyek ini bertujuan membangun website resmi berdomain `.sch.id` bagi SMP Wijaya Sukodono yang kredibel, cepat diakses melalui ponsel, aman dari ancaman peretasan maupun spam, mudah diperbarui oleh guru atau operator Tata Usaha (TU) tanpa latar belakang IT, serta memiliki biaya operasional tahunan sangat rendah (hanya biaya perpanjangan domain resmi sekitar Rp 55.000–Rp 70.000 per tahun).

Pemilihan arsitektur Static Site berbasis Astro dan Cloudflare Pages yang dikombinasikan dengan Pages CMS menghilangkan seluruh kebutuhan sewa server bulanan, perawatan database, maupun risiko celah keamanan plugin yang umum terjadi pada website sekolah berbasis CMS tradisional yang jarang dirawat.

### 1.2 Persona Pengguna
1. **Pengunjung Publik (Orang Tua, Calon Siswa, Masyarakat, Dinas Pendidikan)**: Mencari informasi resmi mengenai profil SMP Wijaya Sukodono, akreditasi, fasilitas belajar, prestasi siswa, kegiatan terbaru, serta informasi Sistem Penerimaan Murid Baru (SPMB). Mayoritas mengakses dari perangkat seluler.
2. **Editor Konten (Guru / Operator TU / Pembina OSIS)**: Pengguna non-teknis yang membutuhkan antarmuka penulisan sederhana layaknya Microsoft Word untuk mengunggah berita, foto kegiatan, pembaruan data guru/fasilitas, serta menyalakan atau mematikan pengumuman SPMB.
3. **Maintainer Teknis (Alumni / Developer)**: Bertanggung jawab pada perancangan awal, deployment, konfigurasi domain .sch.id, dan pelatihan singkat. Target intervensi pasca-rilis adalah kurang dari 2 jam per tahun.

### 1.3 Ruang Lingkup & Peta Situs (9 Halaman Utama)

| Halaman / Rute | Tipe Data | CMS? | Ringkasan Konten & Fitur |
| :--- | :--- | :---: | :--- |
| **1. Beranda (`/`)** | Dinamis (JSON + 3 Berita) | Ya | Top bar SPMB (kondisional), Hero + Signature Experience Card (6+ Dekade / Purna Widya ke-LXIV), Sambutan Kepala Sekolah, 4 Program Unggulan, Pimpinan Sekolah, Pratinjau Fasilitas, 3 Berita Terbaru, CTA SPMB. |
| **2. Tentang Kami (`/profil`)** | File Tunggal (MD/YAML) | Ya | Identitas resmi (NPSN 20540036, Akreditasi B), Sejarah singkat, Visi & Misi, serta Filosofi Logo SMP Wijaya Sukodono. |
| **3. Fasilitas (`/fasilitas`)** | Koleksi JSON | Ya | Katalog sarana prasarana sekolah (Ruang Kelas, Lab Komputer, Perpustakaan, Lab IPA, Lapangan Olahraga, Musholla) dengan filter kategori dan modal Lightbox 'Lihat Foto'. |
| **4. Ekstrakurikuler (`/ekstrakurikuler` & `/ekskul`)** | Koleksi JSON | Ya | Katalog kegiatan ekskul (Marching Band, Voli, Pramuka, Paskibra, Tari, Hadrah, Futsal, Literasi) lengkap dengan filter kategori bidang, jadwal, lokasi, pembina, prestasi, dan CTA pendaftaran. Rute legacy `/ekskul` otomatis dialihkan via HTTP 301 (`_redirects`) ke `/ekstrakurikuler`. Menu di navbar berlabel 'Ekskul'. |
| **5. Guru & Staf (`/guru`)** | Koleksi JSON | Ya | Blok khusus Pimpinan Sekolah (Kepala Sekolah & Wakasek), fitur pencarian & filter bidang, serta grid direktori guru mata pelajaran dan staf TU. |
| **6. Berita (`/berita`)** | Koleksi Markdown | Ya | Artikel unggulan terbaru, pencarian judul, filter kategori (Kegiatan, Prestasi, Pengumuman, Akademik), dan daftar arsip berita. |
| **7. Detail Berita (`/berita/[id]`)** | Pre-rendered Dinamis | Ya | Halaman bacaan artikel penuh, foto sampul 16:9, tombol bagikan langsung ke WhatsApp & salin tautan, serta berita terkait. |
| **8. Info SPMB (`/spmb` & `/ppdb`)** | File Tunggal (JSON) | Ya | Status SPMB (Dibuka/Ditutup), tahun ajaran, pesan penutupan, 4 langkah alur pendaftaran, syarat berkas, jadwal gelombang, info beasiswa/KIP, unduh brosur PDF, FAQ interaktif, serta tautan formulir Google Forms & WA panitia. Rute legacy `/ppdb` otomatis dialihkan via HTTP 301 (`_redirects`) ke `/spmb`. |
| **9. Kontak (`/kontak`)** | Global Config (JSON) | Ya | Alamat lengkap Desa Pekarungan Sukodono, nomor telepon (031) 8830995, tombol WhatsApp TU, email resmi @smpwijayasukodono.sch.id, jam layanan, dan embed Google Maps. |

**Di Luar Ruang Lingkup (Out of Scope):**  
Sistem Informasi Akademik (SIAKAD), login siswa/orang tua, e-rapor online, ujian berbasis komputer (CBT/E-Learning), dan penyimpanan database berkas pendaftar internal berada di luar ruang lingkup website ini. Proses pengumpulan data formulir SPMB dialihkan ke Google Forms sekolah atau portal resmi Dinas Pendidikan agar tetap gratis dan aman.

### 1.4 Kebutuhan Non-Fungsional & Estimasi Biaya

| Komponen | Layanan / Keterangan | Estimasi Biaya |
| :--- | :--- | :--- |
| **Domain Resmi Sekolah** | .sch.id (Rumahweb / Qwords / Jagoan Hosting, syarat PANDI) | ± Rp 55.000 – Rp 70.000 / tahun |
| **Hosting, CDN & SSL** | Cloudflare Pages (Free Tier, unlimited bandwidth & requests) | Rp 0 |
| **Repositori Kode & Konten** | GitHub (Private Repository — Single Source of Truth) | Rp 0 |
| **Dashboard Admin (CMS)** | Pages CMS (app.pagescms.org — fitur Email Collaborators) | Rp 0 |
| **Email Resmi Sekolah** | Cloudflare Email Routing (`info@smpwijayasukodono.sch.id` -> Gmail TU) | Rp 0 |
| **Formulir & Analitik** | Google Forms (SPMB) + Cloudflare Web Analytics | Rp 0 |
| **TOTAL BIAYA OPERASIONAL** | Beban rutin tahunan sekolah | **± Rp 55.000 – Rp 70.000 / tahun** |

---

## BAGIAN 2: Arsitektur & Detail Implementasi Teknis

### 2.1 Alur Kerja Sistem (GitOps Static Architecture)

```
[Guru / Operator TU]
       │
       │  1. Login ke https://app.pagescms.org (via tautan Email / tanpa akun GitHub)
       ▼
  [Pages CMS]  (Membaca skema formulir dari file .pages.yml di root repositori)
       │
       │  2. Klik Save -> otomatis membuat Git Commit berisi file .md / .json / gambar
       ▼
[GitHub Repository]  (Single Source of Truth: kode sumber Astro + konten sekolah)
       │
       │  3. Trigger Webhook otomatis setiap ada push ke branch main
       ▼
[Cloudflare Pages]  (Menjalankan `npm run build` -> output HTML/CSS/JS statis murni)
       │
       │  4. Distribusi ke Edge CDN Global + HTTPS otomatis
       ▼
[https://smpwijayasukodono.sch.id]  (Perubahan tayang secara publik dalam 30–60 detik)
```

### 2.2 Struktur Direktori Proyek

```
website-smp-wijaya-sukodono/
├── .pages.yml                    # Konfigurasi dashboard admin Pages CMS
├── astro.config.mjs              # Konfigurasi Astro + Tailwind v4 + Sitemap
├── package.json                  # Dependensi dan build scripts
├── wrangler.jsonc                # Konfigurasi Cloudflare Workers Static Assets & Routing
├── public/
│   ├── favicon.svg               # Favicon vektor resmi
│   ├── robots.txt                # Petunjuk spider mesin pencari
│   ├── _headers                  # Konfigurasi HTTP Security Headers Cloudflare Pages
│   ├── _redirects                # Konfigurasi HTTP 301 Edge Redirects (/ppdb -> /spmb, /ekskul -> /ekstrakurikuler)
│   └── images/
│       ├── logo-smp-wijaya.svg   # Logo vektor resmi SMP Wijaya Sukodono
│       ├── hero/                 # Foto hero web format WebP teroptimasi
│       ├── ekskul/               # Foto kegiatan ekstrakurikuler WebP
│       └── uploads/              # Folder foto yang diunggah lewat Pages CMS
├── tsconfig.json                 # Konfigurasi TypeScript Astro Strict
└── src/
    ├── styles/
    │   └── global.css            # Design Tokens SMP Wijaya & Self-hosted Fonts
    ├── content.config.ts         # Skema validasi Zod & Tipe Data Content Layer
    ├── content/
    │   ├── berita/               # Koleksi artikel berita (.md)
    │   └── data/
    │       ├── pengaturan.json   # Identitas global & sambutan Kepsek
    │       ├── spmb.json         # Pengaturan SPMB (status, alur, jadwal, syarat, FAQ, kontak)
    │       ├── profil.md         # Sejarah, Visi & Misi Dinamis
    │       ├── fasilitas.json    # Daftar sarana prasarana sekolah
    │       ├── ekstrakurikuler.json # Katalog kegiatan ekstrakurikuler sekolah
    │       └── guru.json         # Direktori pimpinan, guru, dan staf TU
    ├── components/
    │   ├── Navbar.astro          # Navigasi utama + responsif drawer aksesibel
    │   ├── TopBarSPMB.astro      # Banner pengumuman SPMB kondisional
    │   ├── Footer.astro          # Footer 4 kolom resmi
    │   ├── FacilityModal.astro   # Lightbox modal foto fasilitas (Aksesibel + Focus Trap)
    │   └── EkskulModal.astro      # Lightbox modal foto ekstrakurikuler (Aksesibel + Focus Trap)
    ├── layouts/
    │   └── BaseLayout.astro      # Meta SEO + OpenGraph WhatsApp + Global Assets
    └── pages/
        ├── index.astro           # Beranda
        ├── profil.astro          # Tentang Kami & Filosofi Logo (Koneksi dinamis ke profil.md)
        ├── fasilitas.astro       # Katalog Sarana Prasarana
        ├── ekstrakurikuler.astro # Katalog Ekstrakurikuler & Minat Bakat (Menu: Ekskul)
        ├── guru.astro            # Direktori Guru & Tenaga Kependidikan
        ├── spmb.astro            # Informasi SPMB Resmi
        ├── kontak.astro          # Kontak Resmi & Embed Maps
        └── berita/
            ├── index.astro       # Arsip & Pencarian Berita
            └── [id].astro        # Halaman Baca Berita Lengkap
```

---

## BAGIAN 3: Spesifikasi Sistem Desain (Design System)

### 3.1 Palet Warna Resmi (Diturunkan dari Logo Sekolah)

| Nama Token | Hex | Asal dari Logo | Aturan Penggunaan |
| :--- | :--- | :--- | :--- |
| **Deep Ocean 950** | `#082F49` | Jangkar gelap tepi logo | Background Hero, Footer, Banner gelap, Heading utama |
| **Deep Ocean 900** | `#0C4A6E` | Variasi gelap Deep Ocean | Surface kartu di area gelap, hover state gelap |
| **Wijaya Cerulean 600** | `#0284C7` | Pena biru vertikal di tengah logo | Primary CTA button, tautan aktif, ikon utama, focus ring |
| **Wijaya Cyan 500** | `#06B6D4` | Versi ramah-layar perisai cyan logo | Aksen garis tipis, badge sekunder pada area gelap |
| **Cyan Tint 50** | `#ECFEFF` | Tint lembut perisai cyan | Latar badge kategori, kotak ikon program & avatar fallback |
| **Candi Gold 400** | `#FACC15` | Gapura candi bertingkat kuning emas | Highlight prestise di area gelap, angka Experience Card, CTA SPMB |
| **Candi Gold 600** | `#CA8A04` | Versi kontras tinggi emas candi | Aksen teks/ikon emas di atas latar terang/putih |
| **Surface White** | `#FFFFFF` | Buku terbuka putih pada logo | Background kanvas utama dan permukaan kartu |
| **Surface Muted** | `#F8FAFC` | Tint netral bersih | Zebra-banding antar section agar halaman terasa lapang |
| **Ink Primary** | `#0F172A` | Tipografi hitam tegas pada logo | Teks paragraf dan judul utama pada latar terang |
| **Ink Secondary** | `#475569` | Netral abu-abu seimbang | Subjudul, metadata berita, teks deskripsi pendukung |

### 3.2 Tipografi & Rasio Gambar
- **Font Utama**: *Plus Jakarta Sans* (Heading & Body text)
- **Font Aksen/Data**: *JetBrains Mono* (NPSN, Tanggal, Label Eyebrow, Angka Statistik)
- **Rasio Gambar**:
  - Hero Cover: `16:9`
  - Foto Kepala Sekolah: `4:5` (Object-top)
  - Thumbnail Berita: `16:9` (`aspect-video`)
  - Foto Fasilitas: `4:3`
  - Direktori Guru & Staf: `1:1`

---

## BAGIAN 4 (LEMBAR SIAP CETAK): SOP Pengelolaan Website Resmi & Serah Terima Akun

### 4.1 Cara Login ke Dashboard Pengelola (Pages CMS)
1. Buka browser di laptop atau smartphone, kunjungi: `https://app.pagescms.org`
2. Masukkan alamat email pengelola yang didaftarkan.
3. Buka kotak masuk email dan klik tautan **Magic Link** untuk langsung masuk tanpa kata sandi.
4. Pilih repositori website SMP Wijaya Sukodono untuk mulai memperbarui isi.

### 4.2 Cara Menambah Berita Baru
1. Pada menu sisi kiri, klik **Berita & Pengumuman**, lalu klik **Add an entry**.
2. Isi kolom:
   - **Judul Berita**
   - **Tanggal Publikasi**
   - **Kategori** (`Kegiatan`, `Prestasi`, `Pengumuman`, `Akademik`)
   - **Ringkasan Singkat** (1–2 kalimat)
   - **Foto Sampul** (Maksimal 1 MB, format mendatar / landscape)
   - **Isi Berita** (Ketik atau salin naskah lengkap)
3. Pastikan kolom **Simpan sebagai Draft** dalam keadaan MATI (*off*).
4. Klik **Save**. Website akan otomatis diperbarui dalam waktu 1–2 menit.

### 4.3 Cara Mengatur SPMB, Fasilitas, & Data Guru
- **Pengaturan Lengkap SPMB (Buka/Tutup, Jadwal, & Syarat)**:
  1. Buka menu **Pengaturan SPMB (Penerimaan Siswa Baru)** di dashboard Pages CMS.
  2. **Buka/Tutup Pendaftaran**: Centang kotak **Status SPMB Dibuka?** untuk membuka pendaftaran, atau hapus centang untuk menutup. Jika ditutup, tombol formulir otomatis digantikan tombol WhatsApp TU dan muncul kotak pemberitahuan penutupan.
  3. **Tahun Ajaran & Banner**: Sesuaikan tahun ajaran (misal `2026/2027` atau `2027/2028`) dan teks banner notifikasi berjalan di bagian atas website.
  4. **Jadwal Gelombang**: Edit atau tambah gelombang pendaftaran (Gelombang I Inden, Gelombang II Reguler, jam operasional TU).
  5. **Syarat Berkas**: Tambah atau edit butir persyaratan dokumen yang harus dibawa calon siswa.
  6. **Alur 4 Langkah**: Perbarui penjelasan tata cara pendaftaran jika ada penyesuaian alur.
  7. **Tautan Formulir, Brosur & Kontak**: Perbarui tautan Google Forms pendaftaran, unggah file brosur PDF jika ada, dan masukkan nomor WhatsApp panitia penerimaan siswa baru.
  8. **FAQ**: Tambah atau edit tanya-jawab seputar SPMB untuk membantu orang tua murid.
  9. Klik **Save**. Perubahan akan otomatis tayang di `/spmb` dalam 1–2 menit.
- **Memperbarui Data Guru / Fasilitas**: Buka menu **Direktori Guru & Staf** atau **Fasilitas Sekolah**, tambah baris baru dengan klik tanda `+` atau edit data yang ada -> klik **Save**.
- **Mengunggah Banyak Foto Fasilitas & Ekstrakurikuler**: 
  - Pada menu **Fasilitas Sekolah** dan **Ekstrakurikuler**, setiap item memiliki kolom **Foto Sampul Utama** serta kolom **Galeri Foto Tambahan (List)**.
  - Klik tombol `+` pada kolom galeri untuk menambahkan foto ke-2, ke-3, dst.
  - Di website publik, seluruh foto kegiatan akan otomatis ditampilkan dalam slider galeri modal interaktif dengan navigasi panah, penghitung foto (misal: *Foto 1 dari 3*), dan barisan thumbnail di bawah foto.

### 4.4 Panduan Kompresi Gambar Sebelum Upload (Agar Website Cepat & Ringan)
Karena website menggunakan arsitektur GitOps di mana setiap file disimpan langsung di repositori, foto yang diunggah sebaiknya tidak melebihi **300 KB – 500 KB** per file (jangan mengunggah file foto kamera mentah berukuran 3 MB – 10 MB).

**Langkah Kompresi Cepat (Tanpa Perlu Instal Aplikasi):**
1. Buka situs kompresi gratis di browser:
   * **TinyPNG / TinyJPG** (`https://tinypng.com`) — Cukup tarik (*drag & drop*) foto, tunggu proses selesai, lalu download.
   * **Squoosh** (`https://squoosh.app`) — Milik Google. Unggah foto, pilih format **WebP** atau **MozJPEG**, atur *Quality* ke 75–80%, dan atur ukuran maksimal lebar (*resize width*) ke **1200px** atau **1600px**.
   * **ILoveIMG** (`https://www.iloveimg.com/compress-image`) — Bisa kompres banyak foto sekaligus dalam hitungan detik.
2. Gunakan format modern: **WebP** (sangat dianjurkan) atau **JPG/JPEG**.
3. Pastikan ukuran file hasil kompresi berada di bawah **500 KB** sebelum diunggah ke Pages CMS.

### 4.5 Lembar Serah Terima Akun & Catatan Perpanjangan Domain

| Item Aset Digital | Data Resmi |
| :--- | :--- |
| **Alamat Website Resmi** | `https://smpwijayasukodono.sch.id` |
| **Email Induk IT Sekolah (Gmail)** | `it.smpwijayasukodono@gmail.com` |
| **Email Operator Pengelola CMS** | `tatausaha.smpwijaya@gmail.com` |
| **Penyedia Registrar Domain .sch.id** | Rumahweb / Qwords / Jagoan Hosting |
| **Estimasi Biaya Perpanjangan** | ± Rp 55.000 – Rp 70.000 / tahun |
| **Jatuh Tempo Perpanjangan** | 1 tahun setelah tanggal pendaftaran domain |
| **Hosting & CDN** | Cloudflare Pages (Free Tier — Biaya Rp 0) |

---
*Dokumentasi ini disiapkan untuk SMP Wijaya Sukodono.*
