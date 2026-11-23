import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

export const BeritaSchema = z.object({
  title: z.string(),
  tanggal: z.coerce.date(),
  kategori: z.enum(['Kegiatan', 'Prestasi', 'Pengumuman', 'Akademik']),
  thumbnail: z.string().optional(),
  ringkasan: z.string(),
  draft: z.boolean().default(false),
});

export const HeroHomeSchema = z.object({
  foto: z.string().optional(),
  badge: z.string().optional(),
  judul: z.string().optional(),
  judul_sorot: z.string().optional(),
  judul_akhiran: z.string().optional(),
  deskripsi: z.string().optional(),
  tombol_utama_teks: z.string().optional(),
  tombol_utama_link: z.string().optional(),
  tombol_sekunder_teks: z.string().optional(),
  tombol_sekunder_link: z.string().optional(),
});

export const ProgramUnggulanItemSchema = z.object({
  nomor: z.string(),
  judul: z.string(),
  deskripsi: z.string(),
});

export const HeroPagesSchema = z.object({
  profil: z.string().optional(),
  fasilitas: z.string().optional(),
  ekskul: z.string().optional(),
  guru: z.string().optional(),
  berita: z.string().optional(),
  kontak: z.string().optional(),
});

export const PengaturanSchema = z.object({
  nama_sekolah: z.string(),
  npsn: z.string(),
  akreditasi: z.string(),
  hero: HeroHomeSchema.optional(),
  sambutan_kepsek: z.object({
    judul: z.string().optional(),
    nama: z.string(),
    foto: z.string().optional(),
    pesan: z.string(),
  }),
  kontak: z.object({
    alamat: z.string(),
    telepon: z.string(),
    whatsapp: z.string(),
    email: z.string(),
    instagram: z.string().optional(),
    jam_layanan: z.string().optional(),
    maps_url: z.string().optional(),
  }),
  program_unggulan: z.array(ProgramUnggulanItemSchema).optional(),
  hero_pages: HeroPagesSchema.optional(),
});

export const GuruItemSchema = z.object({
  nama: z.string(),
  jabatan: z.string(),
  bidang: z.enum(['Pimpinan', 'Guru Mapel', 'Staf TU']),
  inisial: z.string().optional(),
  foto: z.string().optional(),
});

export const GuruSchema = z.object({
  daftar: z.array(GuruItemSchema),
});

export const FasilitasItemSchema = z.object({
  id: z.number(),
  nama: z.string(),
  kategori: z.enum(['Akademik', 'Laboratorium', 'Olahraga & Ibadah']),
  deskripsi: z.string(),
  foto: z.string().optional(),
  galeri: z.array(z.string()).optional(),
});

export const FasilitasSchema = z.object({
  daftar: z.array(FasilitasItemSchema),
});

export const EkstrakurikulerItemSchema = z.object({
  id: z.number(),
  nama: z.string(),
  kategori: z.enum(['Olahraga', 'Seni & Budaya', 'Kepemimpinan', 'Keagamaan', 'Minat & Bakat']),
  deskripsi: z.string(),
  prestasi: z.string().optional(),
  jadwal: z.string().optional(),
  lokasi: z.string().optional(),
  pembina: z.string().optional(),
  badge: z.string().optional(),
  foto: z.string().optional(),
  galeri: z.array(z.string()).optional(),
});

export const EkstrakurikulerSchema = z.object({
  daftar: z.array(EkstrakurikulerItemSchema),
});

export const SpmbSchema = z.object({
  aktif: z.boolean(),
  tahun_ajaran: z.string(),
  banner: z.object({
    label: z.string().optional(),
    teks: z.string().optional(),
  }).optional(),
  hero: z.object({
    judul: z.string(),
    deskripsi: z.string(),
    foto: z.string().optional(),
  }),
  pesan_tutup: z.object({
    judul: z.string().optional(),
    keterangan: z.string().optional(),
  }).optional(),
  pendaftaran: z.object({
    link_formulir: z.string().optional(),
    label_tombol: z.string().optional(),
    brosur_pdf: z.string().optional(),
    kontak_wa: z.string().optional(),
    pesan_wa: z.string().optional(),
  }),
  jadwal: z.array(z.object({
    gelombang: z.string(),
    waktu: z.string(),
    badge: z.string().optional(),
  })),
  alur: z.array(z.object({
    langkah: z.string(),
    judul: z.string(),
    deskripsi: z.string(),
  })),
  syarat_berkas: z.array(z.string()),
  beasiswa_kip: z.object({
    judul: z.string().optional(),
    keterangan: z.string().optional(),
  }).optional(),
  faq: z.array(z.object({
    pertanyaan: z.string(),
    jawaban: z.string(),
  })),
});

export type Pengaturan = z.infer<typeof PengaturanSchema>;
export type GuruItem = z.infer<typeof GuruItemSchema>;
export type FasilitasItem = z.infer<typeof FasilitasItemSchema>;
export type EkstrakurikulerItem = z.infer<typeof EkstrakurikulerItemSchema>;
export type Spmb = z.infer<typeof SpmbSchema>;

const berita = defineCollection({
  loader: glob({ base: './src/content/berita', pattern: '**/*.md' }),
  schema: BeritaSchema,
});

export const collections = { berita };
