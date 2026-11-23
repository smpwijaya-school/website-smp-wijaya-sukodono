# Bagian 3: Spesifikasi Sistem Desain (Design System)

> **Website Resmi SMP Wijaya Sukodono**  
> Navigasi: [Kembali ke Bagian 2: Arsitektur](02-arsitektur.md) | [Indeks Dokumentasi](README.md) | [Lanjut ke Bagian 4: SOP Operator](04-sop-operator.md)

---

## 3.1 Filosofi & Palet Warna Resmi

Seluruh identitas warna digital diturunkan langsung dari lambang resmi **SMP Wijaya Sukodono** untuk menjaga kesinambungan visual dan kebanggaan almamater.

```
       [Gapura Candi Emas] ──────> Candi Gold (#FACC15 / #CA8A04)
     [Perisai Cyan & Pena Biru] ──> Wijaya Cerulean (#0284C7) & Cyan (#06B6D4)
      [Jangkar Gelap Tepi Logo] ──> Deep Ocean (#082F49 / #0C4A6E)
       [Buku Terbuka Putih] ─────> Surface White (#FFFFFF)
```

### Tabel Token Warna Resmi

| Nama Token | Nilai Hex | Asal Elemen Lambang | Aturan & Peruntukan Penggunaan |
| :--- | :--- | :--- | :--- |
| **Deep Ocean 950** | `#082F49` | Jangkar gelap tepi logo | Latar belakang Hero, Footer, Banner pengumuman gelap, Heading utama |
| **Deep Ocean 900** | `#0C4A6E` | Gradasi jangkar | Permukaan kartu di area gelap, state hover tombol gelap |
| **Wijaya Cerulean 600** | `#0284C7` | Pena biru vertikal di tengah | Tombol Primary CTA, tautan aktif, aksen ikon utama, focus ring |
| **Wijaya Cyan 500** | `#06B6D4` | Perisai pelindung cyan | Garis aksen tipis, badge sekunder pada latar gelap |
| **Cyan Tint 50** | `#ECFEFF` | Tint perisai cyan | Latar badge kategori, wadah ikon program & avatar fallback |
| **Candi Gold 400** | `#FACC15` | Gapura candi bertingkat kuning emas | Highlight prestise pada area gelap, angka Experience Card, tombol CTA SPMB |
| **Candi Gold 600** | `#CA8A04` | Kontras tinggi emas candi | Aksen teks atau ikon emas di atas latar belakang putih/terang |
| **Surface White** | `#FFFFFF` | Buku terbuka putih | Background kanvas utama dan permukaan kartu konten |
| **Surface Muted** | `#F8FAFC` | Tint netral bersih | Zebra-banding antar bagian seksi agar halaman lapang dan nyaman dibaca |
| **Ink Primary** | `#0F172A` | Tipografi hitam tegas lambang | Teks judul utama dan paragraf pada latar terang |
| **Ink Secondary** | `#475569` | Netral abu-abu terkalibrasi | Teks subjudul, metadata tanggal/penulis berita, deskripsi bantuan |

---

## 3.2 Tipografi

1. **Font Utama**: **Plus Jakarta Sans**
   - Karakter: Modern, bersih, tingkat keterbacaan (*legibility*) tinggi di layar ponsel berukuran kecil.
   - Digunakan untuk: Judul halaman, teks paragraf, tombol menu, dan kartu informasi.
2. **Font Aksen Data**: **JetBrains Mono**
   - Karakter: Monospace teknis, rapi, terstruktur.
   - Digunakan untuk: Nomor Pokok Sekolah Nasional (NPSN), label eyebrow/kategori, tanggal berita, dan statistik data.

---

## 3.3 Standar Rasio Gambar & Format

Untuk menjaga tata letak tetap simetris dan rapi saat ditampilkan di berbagai perangkat:

| Elemen Visual | Aspek Rasio | Format Rekomendasi | Catatan Khusus |
| :--- | :---: | :---: | :--- |
| **Hero Cover** | `16:9` | WebP | Resolusi optimal 1600×900 px |
| **Foto Kepala Sekolah** | `4:5` | WebP | Penyelarasan `object-top` |
| **Thumbnail Berita** | `16:9` (`aspect-video`) | WebP / JPG | Resolusi optimal 1200×675 px |
| **Foto Sarana Fasilitas** | `4:3` | WebP / JPG | Resolusi optimal 1200×900 px |
| **Direktori Guru & Staf** | `1:1` (Persegi) | WebP / JPG | Wajah di tengah, resolusi 600×600 px |
| **Logo Sekolah** | Vektor | SVG | Menggunakan `public/images/logo-smp-wijaya.svg` |

---

## 3.4 Standar Aksesibilitas & Interaksi (UI Guidelines)

- **Focus Ring Aksesibel**: Seluruh elemen interaktif (tombol, input, tautan) dilengkapi *focus ring* kontras tinggi (`outline-offset-2`).
- **Focus Trap pada Modal**: Komponen `FacilityModal` dan `EkskulModal` mengunci fokus tombol `Tab` di dalam kotak dialog saat modal terbuka, dan dapat ditutup menggunakan tombol `Esc`.
- **Target Sentuh Ramah Ponsel**: Seluruh tombol dan navigasi memiliki area sentuh minimal **44×44 px** untuk mempermudah navigasi pada layar sentuh.
