# Website Resmi SMP Wijaya Sukodono (NPSN: 20540036)

> Website resmi lembaga pendidikan menengah pertama SMP Wijaya Sukodono, Desa Pekarungan, Kec. Sukodono, Kab. Sidoarjo, Jawa Timur.

Dibangun dengan arsitektur **GitOps Static Site** berbasis **Astro + Tailwind CSS v4 + Pages CMS + Cloudflare Pages**.

## Fitur Utama

- **Ultra Low-Maintenance & Zero-Cost Hosting**: Hosting di Cloudflare Pages (Rp 0), penyimpanan di GitHub (Rp 0), CMS via Pages CMS (Rp 0). Biaya rutin hanya domain resmi `.sch.id` (± Rp 60rb/tahun).
- **Rute Halaman Lengkap**:
  1. `/` — Beranda (Hero, Sambutan Kepsek, Program Unggulan, Pimpinan Sekolah, Pratinjau Fasilitas, Berita Terbaru, CTA SPMB)
  2. `/profil` — Profil, Visi Misi Dinamis dari CMS, Data Kemdikbud, & Filosofi Lambang Sekolah
  3. `/fasilitas` — Katalog Sarana Prasarana dengan Filter Kategori & Lightbox Modal Aksesibel
  4. `/ekstrakurikuler` — Katalog Ekstrakurikuler & Minat Bakat (Auto-redirect dari `/ekskul` via HTTP 301)
  5. `/guru` — Direktori Guru & Tenaga Kependidikan dengan Filter Bidang & Live Search
  6. `/berita` — Arsip Berita, Prestasi & Pengumuman dengan Filter & Live Search
  7. `/berita/[id]` — Halaman Baca Berita Lengkap, Share WhatsApp & Berita Terkait
  8. `/spmb` — Informasi SPMB 2026/2027, Alur 4 Langkah, Syarat, Jadwal & FAQ (Auto-redirect dari `/ppdb` via HTTP 301)
  9. `/kontak` — Alamat, Telepon, WhatsApp Tata Usaha & Google Maps Interaktif
- **Pages CMS Ready**: File konfigurasi `.pages.yml` siap pakai di root repositori.
- **Standar Desain Modern**: Mengadaptasi ritme layout terstruktur ala SMK YPM 8 Sarirogo dan menurunkan palet warna resmi langsung dari lambang SMP Wijaya Sukodono.

## Perintah Pengembangan

```bash
# Menjalankan server lokal (development)
npm run dev

# Memvalidasi tipe data dan skema (type check)
npm run check

# Membangun output statis untuk produksi
npm run build

# Meninjau output build statis
npm run preview
```

## Dokumentasi Proyek & SOP Operator

Seluruh dokumentasi telah dipisahkan secara modular ke dalam direktori [`docs/`](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/README.md):

- 📚 [**Indeks Dokumentasi**](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/README.md) — Gambaran umum dan ringkasan institusi
- 📄 [**01. Product Requirements Document (PRD)**](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/01-prd.md) — Persona, ruang lingkup 9 halaman, dan efisiensi biaya
- 🏗️ [**02. Arsitektur & GitOps**](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/02-arsitektur.md) — Diagram alur sistem, struktur folder, Cloudflare Pages & redirects
- 🎨 [**03. Spesifikasi Sistem Desain**](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/03-design-system.md) — Palet warna resmi, tipografi, dan standar rasio gambar
- 📋 [**04. SOP Operator & Pengelolaan Website**](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/04-sop-operator.md) — Panduan login CMS, publikasi berita, pengaturan SPMB, dan kompresi gambar *(Tersedia format [Word .docx](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/04-sop-operator.docx))*
- 📱 [**05. Panduan Paket Aset QR Code Resmi**](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/05-panduan-qr-code.md) — Spesifikasi teknis dan panduan penempelan QR code pada materi promosi *(Tersedia format [Word .docx](file:///Users/adit/Projects/website-smp-wijaya-sukodono/docs/05-panduan-qr-code.docx))*
