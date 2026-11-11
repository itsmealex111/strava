# Soedirman Strava Challenge 2026

Website leaderboard publik menggunakan Next.js, siap dihubungkan ke repository GitHub baru dan Vercel.

## Data saat ini
- Week 1 final: 67 peserta
- Week 2 cumulative snapshot sampai 11 November 2026: 37 peserta
- Total gabungan: 70 peserta
- Lucky Finisher threshold: 30 km
- Tidak ada podium Top 3 di halaman.

## Deploy
1. Upload seluruh isi folder ini ke repository GitHub baru (jangan upload folder pembungkus).
2. Import repository di Vercel.
3. Framework: Next.js; Root Directory: `./`; Build Command default.
4. Deploy.

## Update leaderboard berikutnya
Ganti `public/data/week2_latest.json` dengan snapshot Week 2 terbaru, lalu hitung ulang `public/leaderboard.json` dari Week 1 + snapshot Week 2 terbaru. Jangan menambahkan snapshot Week 2 lama ke snapshot baru.
