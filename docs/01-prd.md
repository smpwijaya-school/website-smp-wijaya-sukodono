# Bagian 1: Product Requirements Document (PRD)

> **Website Resmi SMP Wijaya Sukodono**  
> NPSN: 20540036 • Akreditasi B • Desa Pekarungan, Kec. Sukodono, Kab. Sidoarjo  
> Navigasi: [Indeks Dokumentasi](README.md) | [Lanjut ke Bagian 2: Arsitektur](02-arsitektur.md)

---

## 1.1 Ringkasan Proyek & Tujuan

Proyek ini bertujuan membangun website resmi berdomain `.sch.id` bagi **SMP Wijaya Sukodono** yang:
- **Kredibel & Informatif**: Menjadi wajah digital resmi sekolah untuk masyarakat, calon wali murid, siswa, dan Dinas Pendidikan.
- **Cepat & Mobile-First**: Dioptimalkan untuk perangkat ponsel pintar (*smartphone*) dengan waktu muat instan tanpa beban komputasi server.
- **Aman**: Kebal dari risiko peretasan, malware, dan spam injeksi database yang sering menimpa CMS tradisional (misal: WordPress tanpa update berkala).
- **Mudah Dikelola**: Memiliki dashboard admin sederhana layaknya pengolah kata bagi bapak/ibu guru dan operator Tata Usaha tanpa perlu memahami pemrograman.
- **Ultra Low-Maintenance & Zero-Cost Hosting**: Biaya operasional tahunan sangat terjangkau, hanya berkisar **± Rp 55.000 – Rp 70.000 / tahun** khusus untuk perpanjangan domain resmi `.sch.id` (hosting, database statis, SSL, dan CMS sepenuhnya **Rp 0**).

---

## 1.2 Persona Pengguna

1. **Pengunjung Publik (Orang Tua Murid, Calon Siswa, Masyarakat, Dinas Pendidikan)**
   - **Kebutuhan**: Mencari informasi profil sekolah, status akreditasi, sarana prasarana, program unggulan, kegiatan ekstrakurikuler, berita terkini, dan prosedur pendaftaran SPMB.
   - **Karakteristik**: Mayoritas mengakses menggunakan peramban ponsel (*mobile browser*) dengan jaringan seluler beragam.
2. **Editor Konten (Guru, Operator Tata Usaha, Pembina OSIS)**
   - **Kebutuhan**: Memperbarui agenda berita, mengunggah foto kegiatan/fasilitas, mengubah informasi guru, serta membuka/menutup gelombang pendaftaran SPMB.
   - **Karakteristik**: Pengguna non-teknis yang memerlukan antarmuka web berbahasa Indonesia, simpel, dan aman.
3. **Maintainer Teknis (Alumni / Web Developer Pro Bono)**
   - **Kebutuhan**: Memelihara fondasi kode sumber, skema data, konfigurasi domain, dan memastikan keandalan pipeline GitOps.
   - **Karakteristik**: Menargetkan waktu pemeliharaan pasca-peluncuran kurang dari 2 jam per tahun.

---

## 1.3 Ruang Lingkup & Peta Situs (9 Halaman Utama)

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

### Di Luar Ruang Lingkup (Out of Scope)
Sistem Informasi Akademik (SIAKAD), login siswa/wali murid, e-rapor, ujian daring (CBT/LMS), serta penyimpanan database pendaftar internal berada di luar cakupan website profil ini. Pengumpulan data pendaftaran SPMB dialihkan ke Google Forms resmi sekolah atau kontak WhatsApp Tata Usaha demi menjaga kesederhanaan sistem dan nol biaya server.

---

## 1.4 Kebutuhan Non-Fungsional & Estimasi Biaya

| Komponen | Layanan / Keterangan | Estimasi Biaya |
| :--- | :--- | :--- |
| **Domain Resmi Sekolah** | `.sch.id` (Registrar resmi PANDI: Rumahweb / Qwords / Jagoan Hosting) | ± Rp 55.000 – Rp 70.000 / tahun |
| **Hosting, CDN & SSL** | Cloudflare Pages (Free Tier — Unlimited Bandwidth & Requests) | Rp 0 |
| **Repositori Kode & Konten** | GitHub (Private Repository — Single Source of Truth) | Rp 0 |
| **Dashboard Admin (CMS)** | Pages CMS (`app.pagescms.org` — fitur Email Collaborators) | Rp 0 |
| **Email Resmi Sekolah** | Cloudflare Email Routing (`info@smpwijayasukodono.sch.id` -> Gmail TU) | Rp 0 |
| **Formulir & Analitik** | Google Forms (SPMB) + Cloudflare Web Analytics (Privacy-friendly) | Rp 0 |
| **TOTAL BIAYA OPERASIONAL** | Beban rutin tahunan sekolah | **± Rp 55.000 – Rp 70.000 / tahun** |
