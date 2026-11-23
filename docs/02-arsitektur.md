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

### Keunggulan Arsitektur:
1. **Kecepatan Maksimal**: Halaman telah di-*render* menjadi HTML statis saat fase build, disajikan melalui edge network Cloudflare dengan latensi sangat rendah.
2. **Keamanan Ekstrem**: Tidak ada database SQL runtime di server yang rentan injeksi, dan tidak ada runtime PHP/server-side code yang dapat dieksploitasi.
3. **Pencadangan Otomatis**: Riwayat setiap perubahan teks, berita, dan pengaturan tersimpan rapi dalam *commit history* Git.

---

## 2.2 Struktur Direktori Proyek

```
website-smp-wijaya-sukodono/
├── .pages.yml                    # Konfigurasi dashboard admin Pages CMS
├── astro.config.mjs              # Konfigurasi Astro + Tailwind v4 + Sitemap
├── package.json                  # Dependensi dan build scripts
├── wrangler.jsonc                # Konfigurasi Cloudflare Workers Static Assets & Routing
├── wrangler.toml                 # Alternatif konfigurasi Wrangler deployment
├── docs/                         # Dokumentasi terstruktur proyek
│   ├── README.md                 # Indeks & peta dokumentasi
│   ├── 01-prd.md                 # Product Requirements Document
│   ├── 02-arsitektur.md          # Arsitektur & alur GitOps
│   ├── 03-design-system.md       # Spesifikasi desain & visual
│   ├── 04-sop-operator.md        # SOP pengelolaan & panduan operator TU
│   └── 05-panduan-qr-code.md     # Panduan aset QR code resmi sekolah
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

# Melakukan kompilasi produksi statis
npm run build

# Menjalankan preview lokal dari folder dist/
npm run preview
```
