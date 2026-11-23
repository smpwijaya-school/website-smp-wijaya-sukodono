# Bagian 2: Arsitektur & Detail Implementasi Teknis

> **Website Resmi SMP Wijaya Sukodono**  
> Navigasi: [Kembali ke Bagian 1: PRD](01-prd.md) | [Indeks Dokumentasi](README.md) | [Lanjut ke Bagian 3: Design System](03-design-system.md)

---

## 2.1 Alur Kerja Sistem (GitOps Static Architecture)

Sistem mengadopsi pola arsitektur **GitOps Static Site**. Seluruh konten, konfigurasi, dan aset visual disimpan langsung di repositori Git sebagai *Single Source of Truth*.

```
[Guru / Operator TU]
       │
       │  1. Login ke https://app.pagescms.org (via tautan Email / Magic Link)
       ▼
  [Pages CMS]  (Membaca skema formulir dari file .pages.yml di root repositori)
       │
       │  2. Klik Save -> otomatis membuat Git Commit berisi file .md / .json / foto
       ▼
[GitHub Repository]  (Single Source of Truth: kode sumber Astro + konten sekolah)
       │
       ├─► [GitHub Actions: Auto-Optimize] (Mendeteksi foto baru di public/images/uploads/)
       │      └─► Menjalankan `sharp`: Resize maks 1600px & kompres 80%
       │      └─► Commit kembali foto terkompres ke repo [skip ci]
       │
       │  3. Trigger Webhook otomatis setiap ada push ke branch main
       ▼
[Cloudflare Pages]  (Menjalankan `npm run build` -> didahului `prebuild` optimasi foto)
       │
       │  4. Distribusi ke Edge CDN Global + HTTPS otomatis
       ▼
[https://smpwijayasukodono.sch.id]  (Perubahan tayang secara publik dalam 30–60 detik)
```

### Keunggulan Arsitektur:
1. **Kecepatan Maksimal**: Halaman telah di-*render* menjadi HTML statis saat fase build, disajikan melalui edge network Cloudflare dengan latensi sangat rendah.
2. **Keamanan Ekstrem**: Tidak ada database SQL runtime di server yang rentan injeksi, dan tidak ada runtime PHP/server-side code yang dapat dieksploitasi.
3. **Pencadangan Otomatis**: Riwayat setiap perubahan teks, berita, dan pengaturan tersimpan rapi dalam *commit history* Git.

---

## 2.2 Struktur Direktori Proyek

```
website-smp-wijaya-sukodono/
├── .github/                      # Otomatisasi CI/CD & GitHub Actions
│   └── workflows/
│       ├── ci.yml                # Validasi type check & build static site
│       └── optimize-images.yml   # Workflow kompresi & resize foto otomatis
├── .pages.yml                    # Konfigurasi dashboard admin Pages CMS & Actions
├── astro.config.mjs              # Konfigurasi Astro + Tailwind v4 + Sitemap
├── package.json                  # Dependensi, build scripts, & prebuild hook
├── wrangler.jsonc                # Konfigurasi Cloudflare Workers Static Assets & Routing
├── wrangler.toml                 # Alternatif konfigurasi Wrangler deployment
├── docs/                         # Dokumentasi terstruktur proyek
│   ├── README.md                 # Indeks & peta dokumentasi
│   ├── 01-prd.md                 # Product Requirements Document
│   ├── 02-arsitektur.md          # Arsitektur & alur GitOps
│   ├── 03-design-system.md       # Spesifikasi desain & visual
│   ├── 04-sop-operator.md        # SOP pengelolaan & panduan operator TU
│   └── 05-panduan-qr-code.md     # Panduan aset QR code resmi sekolah
├── scripts/                      # Skrip utilitas internal
│   ├── optimize-uploads.mjs      # Skrip optimasi & kompresi foto (Sharp)
│   ├── generate_docx.py          # Generator dokumen Word .docx resmi
│   └── generate_ekskul_images.cjs # Generator visual kegiatan ekskul
├── public/
│   ├── favicon.svg               # Favicon vektor resmi
│   ├── robots.txt                # Petunjuk spider mesin pencari
│   ├── _headers                  # Konfigurasi HTTP Security Headers Cloudflare Pages
│   ├── _redirects                # Edge Redirects (/ppdb -> /spmb, /ekskul -> /ekstrakurikuler)
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

## 2.3 Konfigurasi Deployment & Cloudflare Pages

### Redirects Edge (`public/_redirects`)
Menjamin URL lawas atau alias mudah diingat tetap mengarah ke halaman yang benar secara otomatis:
```text
/ppdb    /spmb             301
/ekskul  /ekstrakurikuler  301
```

### Security Headers (`public/_headers`)
Mengamankan pengiriman aset dari ancaman clickjacking, sniffing tipe konten, dan XSS:
```text
/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
```

---

## 2.4 Perintah Operasional Teknis (Developer)

```bash
# Menjalankan server pengembangan lokal (Astro dev)
npm run dev

# Memeriksa validasi tipe data TypeScript & skema konten
npm run check

# Menjalankan kompresi dan optimasi gambar secara mandiri
npm run optimize:images

# Melakukan kompilasi produksi statis (otomatis menjalankan prebuild kompresi)
npm run build

# Menjalankan preview lokal dari folder dist/
npm run preview
```

---

## 2.5 Arsitektur Kompresi & Optimasi Media Otomatis

Untuk menjaga ukuran repositori Git tetap ramping dan memastikan website dapat dimuat dalam < 1.5 detik pada koneksi seluler wali murid, diterapkan sistem optimasi gambar multi-lapis:

1. **Trigger Otomatis di Latar Belakang (GitHub Actions)**:
   - File alur kerja: `.github/workflows/optimize-images.yml`.
   - Terpicu setiap ada *push* baru ke `main` yang menyertakan perubahan di folder `public/images/uploads/**`.
   - Menggunakan pustaka performa tinggi **Sharp** via `node scripts/optimize-uploads.mjs`.
   - Menghasilkan *commit* otomatis dengan pesan `chore(media): otomatis kompres foto upload [skip ci]` sehingga tidak memicu perulangan build tak terbatas (*infinite loop*).

2. **Hook Pra-Kompilasi (`prebuild`)**:
   - Didefinisikan di `package.json` (`"prebuild": "node scripts/optimize-uploads.mjs"`).
   - Menjamin seluruh foto yang masuk ke bundel `dist/` sudah teroptimasi dengan sempurna bahkan jika proses build dijalankan secara manual di server Cloudflare atau lokal.

3. **Spesifikasi Teknis Kompresi**:
   - **Maksimal Resolusi**: Lebar dan tinggi dibatasi maksimal **1600 px** (`fit: inside`, tidak memperbesar gambar kecil). Resolusi ini sangat ideal untuk layar Retina/High-DPI namun menjaga ukuran berkas sangat kecil.
   - **Tingkat Kualitas Visual**: `80%` (kualitas visual tajam tanpa artefak kompresi yang mengganggu).
   - **Metode Format**:
     - **JPEG/JPG**: Dikompresi menggunakan modul `mozjpeg` dengan mode progresif (`progressive: true`).
     - **PNG**: Dikompresi dengan level kompresi 9 dan `effort: 8`.
     - **WebP**: Dikompresi dengan `effort: 6`.
   - **In-place Overwrite**: Nama berkas dan ekstensinya tetap dipertahankan persis seperti aslinya. Hal ini menjamin bahwa seluruh tautan di artikel Markdown (`src/content/berita/*.md`) dan JSON tidak akan pernah terputus (*broken link*).
   - **Proteksi Ukuran**: Berkas hanya ditimpa jika hasil kompresi menghasilkan ukuran yang lebih kecil dari aslinya. Jika berkas sudah optimal, proses penulisan dilewati.

4. **Integrasi Tombol Aksi di Pages CMS**:
   - Dikonfigurasikan pada `.pages.yml` melalui blok `actions`.
   - Operator sekolah dapat memicu kompresi kapan pun secara langsung melalui tombol **"⚡ Kompres Foto Upload"** di dalam antarmuka Pages CMS.
