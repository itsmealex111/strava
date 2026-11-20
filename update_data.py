import json,re,collections,zipfile,os
base='/mnt/data/newbuild'
week2='''
Viandra Diarsa Viandra Diarsa|65.1|9|15.1|7:06|84
Dep Fr Dep Fr|51.5|11|11.0|6:56|98
Leonarsa Friendly Hutapea|46.4|7|11.6|7:18|80
Ilham Ubed|44.4|6|13.0|6:36|8
Lukas Limbong Lukas Limbong|37.5|6|9.3|6:52|29
ahmad zaki ahmad zaki|36.6|8|10.0|7:35|48
Hafizh R. Hafizh R.|31.9|6|7.2|5:17|--
Christophorus Gerard Marvin Christophorus Gerard Marvin|31.0|7|10.1|7:18|52
Sigi Sitepu|28.6|7|6.1|5:36|11
Savero Ananda Savero Ananda|24.2|5|9.8|7:35|46
Anggit D|23.4|4|10.0|6:54|27
Barran Maulana|22.0|3|10.0|6:52|21
Naufal Argy Naufal Argy|20.1|3|7.6|5:23|23
Riska NA Riska NA|19.7|4|7.0|6:46|56
Dhio Novansyah Dhio Novansyah|18.9|7|2.7|8:13|58
Anom Wibisono Anom Wibisono|18.5|4|5.0|8:06|--
Kurotsuchi Mayuri Kurotsuchi Mayuri|18.1|3|8.0|6:28|38
Gema A. Putra|17.6|3|10.1|6:26|22
Alif belajar lari Alif belajar lari|17.5|5|6.0|5:55|8
Rakha Lagi Cidera Rakha Lagi Cidera|17.3|4|6.0|6:17|6
Farhan Fadil Farhan Fadil|16.7|4|5.1|9:28|15
Nyoman Wiyana|15.9|5|4.0|6:36|15
Azka G Azka G|15.6|4|7.2|7:49|19
Zildjian Axa|15.4|5|3.3|6:54|8
Andika Alamsyah|15.0|5|3.0|9:51|23
Iqbal Nurpasha|14.7|4|5.4|7:24|42
Ahmad Choirul Muna Ahmad Choirul Muna|14.4|3|6.0|7:34|10
Rizky Zaidan Rizky Zaidan|12.8|4|3.7|8:29|22
Rais Mahdi Rais Mahdi|12.3|5|3.4|8:29|9
Marvel Adam Marvel Adam|11.8|4|3.2|6:19|3
Axa Daffaxa Axa Daffaxa|11.7|3|5.3|6:16|8
Yusuf Wibowo Yusuf Wibowo|11.6|2|6.5|7:19|--
zein nurrahman zein nurrahman|10.9|3|5.0|6:40|--
Mario Sendy Irawan Mario Sendy Irawan|10.0|2|5.0|8:29|--
Muhammad Riziq Muttaqin Muhammad Riziq Muttaqin|10.0|2|5.0|6:42|23
Anggito Satya Anggito Satya|9.9|1|9.9|9:15|14
Andrean Dicky Octafilianus Andrean Dicky Octafilianus|9.7|3|3.5|5:43|--
Arif Satrio Budiman Arif Satrio Budiman|9.6|3|5.0|7:17|23
adhiyasa satya adhiyasa satya|9.3|2|5.0|5:48|--
Ivan Bakara Ivan Bakara|9.1|4|3.0|6:44|6
Aizna S Aizna S|9.0|2|7.0|20:34|319
Much Fazrin Much Fazrin|8.5|2|5.0|6:41|9
Luthfi Ridanta Luthfi Ridanta|8.2|2|5.0|6:26|7
Adrian Axel|8.0|3|4.0|7:39|4
Calvin Putra Calvin Putra|8.0|2|4.0|5:59|79
Cahya Farhan Muhammad Cahya Farhan Muhammad|7.8|2|4.5|8:17|2
Kristian Leonardo Pandiangan|7.5|2|4.0|7:08|5
Ilham E3 Ilham E3|7.3|2|5.0|7:09|6
M Hasan F N M Hasan F N|6.9|3|3.0|5:37|--
wira ardi wira ardi|6.1|2|4.1|7:13|12
Rizal Fadhilah Kamal Rizal Fadhilah Kamal|6.1|2|3.1|8:08|--
Hafis Ilham Hafis Ilham|5.5|3|2.0|5:29|7
Arief Syaifudin Arief Syaifudin|5.5|2|3.4|7:28|--
Rifad H Rifad H|5.4|2|5.0|7:14|--
Azhar Rais Azhar Rais|5.4|2|3.0|6:43|--
Abdullah Syahid Abdullah Syahid|5.0|1|5.0|7:02|8
Ananda Sembiring Ananda Sembiring|5.0|1|5.0|6:09|--
Abim . Abim .|5.0|1|5.0|5:53|--
M. Nadhir Al Ghifary M. Nadhir Al Ghifary|5.0|1|5.0|7:05|--
Nadia Akilah Nadia Akilah|4.0|1|4.0|6:42|13
Havergal Samosir Havergal Samosir|4.0|1|4.0|11:34|17
P. Komarudin P. Komarudin|3.7|1|3.7|6:29|2
Fauzan Ikromi Fauzan Ikromi|3.4|1|3.4|7:37|--
erlin shfn erlin shfn|3.3|1|3.3|7:18|--
Rifki Pasha Rifki Pasha|3.0|1|3.0|8:16|--
Muhammad Syairozy Syauqi Muhammad Syairozy Syauqi|2.9|1|2.9|6:44|7
Ratnasari Murprayana Ratnasari Murprayana|2.2|1|2.2|8:14|--
Ananda Fadhil Ananda Fadhil|2.0|2|1.8|6:50|--
Muhamad Rizky Prima Muhamad Rizky Prima|2.0|1|2.0|5:40|8
ihsanudin halim Fajrian ihsanudin halim Fajrian|1.6|1|1.6|7:29|--
Daffa Tsany Daffa Tsany|1.5|1|1.5|8:16|6
Irene Sembiring|0.6|1|0.6|7:47|--
'''
week3='''
Dep Fr Dep Fr|50.4|9|7.0|6:40|56
Viandra Diarsa Viandra Diarsa|43.9|7|10.2|7:35|55
Leonarsa Friendly Hutapea|38.2|8|6.8|7:36|70
Sigi Sitepu|33.7|6|10.0|5:27|--
Ilham Ubed|32.6|6|6.5|6:12|21
Anggit D|28.1|8|5.3|6:32|32
zein nurrahman zein nurrahman|27.1|7|5.1|6:43|--
Hafizh R. Hafizh R.|26.5|5|6.7|5:21|--
Rizky Zaidan Rizky Zaidan|24.8|7|5.8|6:21|324
Kristian Leonardo Pandiangan|23.4|5|6.4|6:24|11
Christophorus Gerard Marvin Christophorus Gerard Marvin|21.6|5|6.0|6:49|25
Ahmad Choirul Muna Ahmad Choirul Muna|20.0|4|7.0|6:28|5
Andrean Dicky Octafilianus Andrean Dicky Octafilianus|20.0|5|5.2|6:39|--
Jabalnur Jabalnur Jabalnur Jabalnur|19.2|5|6.4|7:25|14
Nadia Akilah Nadia Akilah|18.5|4|6.1|6:38|29
ihsanudin halim Fajrian ihsanudin halim Fajrian|16.5|4|5.0|7:41|--
Calvin Putra Calvin Putra|16.5|3|6.5|6:11|74
Farhan Fadil Farhan Fadil|16.3|5|3.6|8:38|--
Naufal . Naufal .|16.3|3|6.0|5:22|--
Rifki Pasha Rifki Pasha|16.1|4|5.0|8:42|--
ahmad zaki ahmad zaki|16.1|5|5.0|7:39|33
Alif belajar lari Alif belajar lari|14.5|4|5.0|6:26|7
Dhio Novansyah Dhio Novansyah|13.5|5|2.7|8:02|8
Yusuf Wibowo Yusuf Wibowo|12.4|3|5.2|6:59|--
Muhammad Riziq Muttaqin Muhammad Riziq Muttaqin|12.2|2|7.2|6:23|21
Savero Ananda Savero Ananda|12.2|4|5.0|6:48|42
Riska NA Riska NA|12.0|3|4.5|6:53|5
Naufal Argy Naufal Argy|12.0|2|7.0|5:10|14
Ananda Fadhil Ananda Fadhil|11.9|4|4.2|6:52|6
M. Nadhir Al Ghifary M. Nadhir Al Ghifary|11.3|3|5.0|7:11|--
Nyoman Wiyana|11.0|3|5.0|6:15|7
Azhar Rais Azhar Rais|10.0|2|5.0|6:52|--
Barran Maulana|9.6|2|5.0|5:56|16
Marvel Adam Marvel Adam|9.0|3|3.0|6:13|7
Hafis Ilham Hafis Ilham|8.6|2|5.0|5:42|8
Azka G Azka G|8.3|2|4.2|7:16|5
M Hasan F N M Hasan F N|8.3|2|5.0|6:00|--
Andika Alamsyah|8.3|3|3.0|10:04|4
Zildjian Axa|8.0|5|1.6|6:00|--
Axa Daffaxa Axa Daffaxa|7.2|2|5.0|5:45|9
Rakha Lagi Cidera Rakha Lagi Cidera|7.2|2|6.1|5:45|--
Syahrindra Rif'at Syahrindra Rif'at|7.1|2|3.8|7:46|--
rivanya noer rivanya noer|7.0|3|3.1|7:08|--
Kurotsuchi Mayuri Kurotsuchi Mayuri|7.0|1|7.0|6:08|--
erlin shfn erlin shfn|6.5|2|3.4|6:56|--
Abim . Abim .|6.4|2|5.0|6:30|--
Rizal Fadhilah Kamal Rizal Fadhilah Kamal|6.4|2|3.4|7:05|--
wira ardi wira ardi|6.2|2|4.0|7:33|10
Iqbal Nurpasha|6.0|2|3.3|8:07|19
Gema A. Putra|5.1|1|5.1|6:47|1
Rizal Mld Rizal Mld|5.1|1|5.1|7:18|--
Luthfi Ridanta Luthfi Ridanta|5.0|1|5.0|6:51|--
Anom Wibisono Anom Wibisono|5.0|1|5.0|7:47|--
Ghazian Milzam Ghazian Milzam|5.0|1|5.0|7:08|7
Adrian Axel|5.0|2|2.6|7:00|2
Mario Sendy Irawan Mario Sendy Irawan|3.9|2|3.0|6:23|--
Ivan Bakara Ivan Bakara|3.8|2|2.0|6:30|--
Rifad H Rifad H|3.6|2|3.3|15:52|--
Winda Ayu L Winda Ayu L|3.6|2|2.0|8:12|--
Gafirat Wira Gafirat Wira|3.5|2|2.0|6:29|--
Ilham E3 Ilham E3|3.4|1|3.4|7:17|--
Aminah Arla|3.3|1|3.3|7:34|--
Rais Mahdi Rais Mahdi|3.2|2|1.7|6:41|--
Cindy M Cindy M|3.0|1|3.0|7:57|--
Arif Satrio Budiman Arif Satrio Budiman|3.0|1|3.0|7:02|--
Muhamad Rizky Prima Muhamad Rizky Prima|3.0|1|3.0|5:48|--
Daffa Tsany Daffa Tsany|2.5|1|2.5|8:12|--
Much Fazrin Much Fazrin|2.5|1|2.5|5:47|--
Andrew . Andrew .|2.1|1|2.1|8:10|--
Cahya Farhan Muhammad Cahya Farhan Muhammad|2.1|1|2.1|7:08|1
Lukas Limbong Lukas Limbong|2.0|1|2.0|7:42|--
Anggito Satya Anggito Satya|2.0|1|2.0|6:37|--
Havergal Samosir Havergal Samosir|1.7|1|1.7|9:34|--
Aizna S Aizna S|1.6|1|1.6|7:06|--
Farhan Aly Farhan Aly|1.4|1|1.4|8:45|--
Ananda Sembiring Ananda Sembiring|1.1|1|1.1|7:40|--
Daniel Parsaoran Daniel Parsaoran|1.0|1|1.0|7:00|--
Kevin Rehuel Kevin Rehuel|1.0|1|1.0|5:42|--
Nazwa Adlina Nazwa Adlina|0.0|1|0.0|4:45|--
'''
def norm(s):
 s=' '.join(s.strip().split())
 parts=s.split()
 if len(parts)%2==0 and parts[:len(parts)//2]==parts[len(parts)//2:]:
  s=' '.join(parts[:len(parts)//2])
 return s

def parse(txt):
 out=[]
 for line in txt.strip().splitlines():
  n,d,a,l,p,e=line.split('|')
  m,sec=map(int,p.split(':'))
  out.append({'name':norm(n),'distance_km':float(d),'activities':int(a),'longest_km':float(l),'pace_sec':m*60+sec,'elevation_m':0 if e=='--' else int(e)})
 return out
w2=parse(week2); w3=parse(week3)
print('rows',len(w2),len(w3),'unique',len(set(x['name'] for x in w2)),len(set(x['name'] for x in w3)))
json.dump(w2,open(base+'/public/data/week2_latest.json','w'),ensure_ascii=False,indent=2)
json.dump(w3,open(base+'/public/data/week3_latest.json','w'),ensure_ascii=False,indent=2)
# aggregate all 3 weeks by normalized participant name
w1=json.load(open(base+'/public/data/week1.json'))
allrows=collections.defaultdict(list)
for rows in (w1,w2,w3):
 for r in rows: allrows[norm(r['name'])].append(r)
females={'Aizna S','Amelia Rizky','Azka G','Bulan Fahada','Irene Sembiring','Nadia Akilah','Nazwa Adlina','Riska NA','Ratnasari Murprayana','rivanya noer'}
participants=[]
for name,rs in allrows.items():
 dist=sum(r['distance_km'] for r in rs)
 runs=sum(r['activities'] for r in rs)
 longest=max(r['longest_km'] for r in rs)
 elev=sum(r['elevation_m'] for r in rs)
 pace=sum(r['distance_km']*r['pace_sec'] for r in rs)/dist if dist>0 else 0
 participants.append({'name':name,'distance_km':round(dist,1),'activities':runs,'longest_km':round(longest,1),'elevation_m':elev,'gender':'female' if name in females else 'male','avg_pace':f'{int(pace//60)}:{int(round(pace%60)):02d}'})
participants.sort(key=lambda p:(-p['distance_km'],p['name'].lower()))
obj={'updated_at':'2026-11-20','week_label':'Week 1 final + Week 2 snapshot terbaru + Week 3 snapshot terbaru (20 November 2026)','event_start':'2026-11-02','event_end':'2026-11-30','aggregation_note':'Overall = Week 1 final + Week 2 snapshot yang dikirim 20 Nov + Week 3 snapshot yang dikirim 20 Nov. Snapshot tiap minggu menggantikan snapshot sebelumnya, tidak dijumlahkan antar-snapshot dalam minggu yang sama. Nama ganda identik dinormalisasi; Naufal . dan Naufal Argy tetap terpisah. Pace dihitung berbobot jarak; elevasi -- dianggap 0 m.','participants':participants}
json.dump(obj,open(base+'/public/leaderboard.json','w'),ensure_ascii=False,indent=2)
# update visible update line
p=base+'/app/page.tsx'; s=open(p).read().replace('Week 1 final + Week 2 final + Week 3 sampai 20 November 2026','Week 1 final + Week 2 & Week 3 snapshot terbaru · 20 November 2026'); open(p,'w').write(s)
# summary stats
print('overall participants',len(participants),'km',round(sum(p['distance_km'] for p in participants),1),'runs',sum(p['activities'] for p in participants),'eligible',sum(p['distance_km']>=30 for p in participants))
print('top5',[(p['name'],p['distance_km']) for p in participants[:5]])
print('week2/3 km',sum(x['distance_km'] for x in w2),sum(x['distance_km'] for x in w3))
# write readme
open(base+'/README.md','w').write('''# Soedirman Strava Challenge Dashboard\n\nUpdate data 20 November 2026. Week 1 remains fixed; Week 2 and Week 3 have been replaced with the latest cumulative snapshots supplied on 20 November. Overall totals are recalculated as Week 1 + latest Week 2 + latest Week 3.\n\nDeploy: replace repository files with this ZIP, commit and push to main; Vercel deploys automatically.\n''')
# zip fresh
out='/mnt/data/Soedirman_Strava_Dashboard_Update_20Nov2026.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for root,dirs,files in os.walk(base):
  dirs[:]=[d for d in dirs if d not in ['.next','node_modules','.git']]
  for fn in files:
   path=os.path.join(root,fn)
   arc=os.path.relpath(path,base)
   z.write(path,arc)
print(out,os.path.getsize(out))
