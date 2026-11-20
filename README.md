# Soedirman Strava Challenge 2026 — Dashboard Interaktif

Update data: 20 November 2026

## Perbaikan pada versi ini
- Nama peserta pada leaderboard menggunakan navigasi Next.js `Link` menuju halaman profil.
- Parameter `generateStaticParams()` menggunakan nama peserta asli sebagai slug, bukan slug yang sudah di-URL-encode. Ini menghindari ketidakcocokan URL pada halaman profil hasil static generation.
- Halaman profil menampilkan ringkasan mingguan Week 1, Week 2, dan Week 3 serta grafik jarak, estimasi durasi, average pace, dan elevation dibandingkan rata-rata peserta.

## Deploy
1. Ekstrak ZIP.
2. Ganti file project di repository GitHub dengan seluruh isi ZIP.
3. Commit dan push ke branch yang terhubung ke Vercel.
4. Tunggu deployment selesai, lalu buka leaderboard dan klik nama peserta.

Catatan: build belum dapat diverifikasi di lingkungan ini karena proses `npm install` mengalami timeout. Setelah deployment, jika halaman profil masih belum terbuka, kirimkan URL halaman yang muncul atau screenshot error agar bisa ditelusuri lebih lanjut.
