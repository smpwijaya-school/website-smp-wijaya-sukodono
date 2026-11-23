import fs from 'node:fs';
import path from 'node:path';
import sharp from 'sharp';

const UPLOADS_DIR = path.resolve('public/images/uploads');
const MAX_DIMENSION = 1600; // Maksimal lebar / tinggi (px) untuk web retina
const QUALITY = 80; // Kualitas kompresi visual ideal (ringan tapi tetap tajam)

const SUPPORTED_EXTENSIONS = new Set(['.jpg', '.jpeg', '.png', '.webp']);

function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  const kb = bytes / 1024;
  if (kb < 1024) return kb.toFixed(1) + ' KB';
  const mb = kb / 1024;
  return mb.toFixed(2) + ' MB';
}

async function getAllFiles(dir) {
  if (!fs.existsSync(dir)) return [];
  const entries = await fs.promises.readdir(dir, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await getAllFiles(fullPath)));
    } else if (entry.isFile()) {
      files.push(fullPath);
    }
  }

  return files;
}

async function optimizeImage(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  if (!SUPPORTED_EXTENSIONS.has(ext)) {
    return null;
  }

  try {
    const originalBuffer = await fs.promises.readFile(filePath);
    const originalSize = originalBuffer.length;

    // Setup transformer dengan resize (fit inside, jangan perbesar foto kecil)
    let pipeline = sharp(originalBuffer).resize({
      width: MAX_DIMENSION,
      height: MAX_DIMENSION,
      fit: 'inside',
      withoutEnlargement: true,
    });

    // Optimasi sesuai ekstensi asli agar tautan konten tidak rusak
    if (ext === '.jpg' || ext === '.jpeg') {
      pipeline = pipeline.jpeg({
        quality: QUALITY,
        progressive: true,
        mozjpeg: true,
      });
    } else if (ext === '.png') {
      pipeline = pipeline.png({
        quality: QUALITY,
        compressionLevel: 9,
        effort: 8,
      });
    } else if (ext === '.webp') {
      pipeline = pipeline.webp({
        quality: QUALITY,
        effort: 6,
      });
    }

    const optimizedBuffer = await pipeline.toBuffer();
    const newSize = optimizedBuffer.length;

    // Simpan hanya jika ukuran lebih kecil
    if (newSize < originalSize) {
      await fs.promises.writeFile(filePath, optimizedBuffer);
      const savedBytes = originalSize - newSize;
      const percent = ((savedBytes / originalSize) * 100).toFixed(1);
      return {
        file: path.relative(process.cwd(), filePath),
        originalSize,
        newSize,
        percent,
      };
    } else {
      return {
        file: path.relative(process.cwd(), filePath),
        skipped: true,
        reason: 'Sudah optimal',
      };
    }
  } catch (err) {
    console.error(`⚠️ Gagal memproses ${filePath}:`, err.message);
    return null;
  }
}

async function main() {
  console.log(`🔍 Memindai foto di folder: ${UPLOADS_DIR}`);
  const files = await getAllFiles(UPLOADS_DIR);
  const imageFiles = files.filter((f) =>
    SUPPORTED_EXTENSIONS.has(path.extname(f).toLowerCase())
  );

  if (imageFiles.length === 0) {
    console.log('ℹ️ Tidak ada foto yang perlu diproses di public/images/uploads.');
    return;
  }

  let totalSaved = 0;
  let optimizedCount = 0;

  for (const file of imageFiles) {
    const result = await optimizeImage(file);
    if (result && !result.skipped) {
      optimizedCount++;
      totalSaved += result.originalSize - result.newSize;
      console.log(
        `✅ ${result.file}: ${formatBytes(result.originalSize)} -> ${formatBytes(result.newSize)} (Hemat ${result.percent}%)`
      );
    }
  }

  if (optimizedCount > 0) {
    console.log(
      `🎉 Selesai! ${optimizedCount} foto berhasil dikompres. Total hemat: ${formatBytes(totalSaved)}.`
    );
  } else {
    console.log('✨ Semua foto sudah dalam kondisi terkompres optimal.');
  }
}

main().catch((err) => {
  console.error('Fatal error saat kompresi:', err);
  process.exit(1);
});
