"use client";
import { useMemo, useState } from "react";
import data from "../public/leaderboard.json";

type Participant = typeof data.participants[number];
const paceToSeconds=(pace:string)=>{const [m,s]=pace.split(":").map(Number);return Number.isFinite(m)&&Number.isFinite(s)?m*60+s:Number.MAX_SAFE_INTEGER};
const totalSeconds=(p:Participant)=>p.distance_km*paceToSeconds(p.avg_pace);
export default function Home() {
 const [query,setQuery]=useState("");
 const [filter,setFilter]=useState("all");
 const [sort,setSort]=useState("distance");
 const participants = useMemo(()=>{
  let list=[...data.participants] as Participant[];
  if(query.trim()) list=list.filter(p=>p.name.toLowerCase().includes(query.toLowerCase()));
  if(filter==="eligible") list=list.filter(p=>p.distance_km>=30);
  if(filter==="under") list=list.filter(p=>p.distance_km<30);
  if(sort==="activities") list.sort((a,b)=>b.activities-a.activities);
  else if(sort==="pace") list.sort((a,b)=>paceToSeconds(a.avg_pace)-paceToSeconds(b.avg_pace));
  else if(sort==="time") list.sort((a,b)=>totalSeconds(b)-totalSeconds(a));
  else if(sort==="elevation") list.sort((a,b)=>b.elevation_m-a.elevation_m);
  else list.sort((a,b)=>b.distance_km-a.distance_km);
  return list;
 },[query,filter,sort]);
 const totalKm=data.participants.reduce((s,p)=>s+p.distance_km,0);
 const totalRuns=data.participants.reduce((s,p)=>s+p.activities,0);
 const eligible=data.participants.filter(p=>p.distance_km>=30).length;
 return <main className="shell">
  <header className="hero">
   <img className="heroBanner" src="/images/dashboard-banner.png" alt="Soedirman Strava Challenge 2026 dengan Eliud Kipchoge dan Jakob Ingebrigtsen"/>
  </header>
  <section className="stats">
   <article><span>TOTAL PESERTA</span><strong>{data.participants.length}</strong><small>athletes</small></article>
   <article><span>TOTAL JARAK</span><strong>{totalKm.toLocaleString("id-ID",{maximumFractionDigits:1})}<i> km</i></strong><small>akumulasi challenge</small></article>
   <article><span>TOTAL AKTIVITAS</span><strong>{totalRuns}</strong><small>running activities</small></article>
   <article><span>LUCKY FINISHER</span><strong>{eligible}</strong><small>minimal 30 km</small></article>
  </section>
  <section className="board">
   <div className="boardHead"><div><p className="eyebrow">THE RACE NEVER STOPS</p><h2>FULL LEADERBOARD</h2><p className="muted">Week 1 final + Week 2 final + Week 3 sampai 20 November 2026</p></div><span className="liveDot">● UPDATED</span></div>
   <div className="controls"><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Cari nama peserta..."/><select value={filter} onChange={e=>setFilter(e.target.value)}><option value="all">Semua peserta</option><option value="eligible">Lucky Finisher ≥30 km</option><option value="under">Belum mencapai 30 km</option></select><select value={sort} onChange={e=>setSort(e.target.value)}><option value="distance">Urutkan: Jarak</option><option value="activities">Urutkan: Aktivitas</option><option value="pace">Urutkan: Average pace (tercepat)</option><option value="time">Urutkan: Total time (estimasi)</option><option value="elevation">Urutkan: Total elevation</option></select></div>
   <div className="tableWrap"><table><thead><tr><th>RANK</th><th>ATHLETE</th><th>DISTANCE</th><th>RUNS</th><th>LONGEST</th><th>AVG PACE</th><th>ELEVATION</th><th>STATUS</th></tr></thead><tbody>
   {participants.map((p,i)=><tr key={p.name}><td className="rank">{String(i+1).padStart(2,"0")}</td><td className="athlete">{p.name}</td><td className="distance">{p.distance_km.toFixed(1)} <small>km</small></td><td>{p.activities}</td><td>{p.longest_km.toFixed(1)} km</td><td>{p.avg_pace} /km</td><td>{p.elevation_m} m</td><td>{p.distance_km>=30?<span className="eligible">ELIGIBLE</span>:<span className="pending">IN PROGRESS</span>}</td></tr>)}
   </tbody></table>{participants.length===0&&<p className="empty">Peserta tidak ditemukan.</p>}</div>
   <div className="boardFoot"><span>Menampilkan {participants.length} dari {data.participants.length} peserta</span><span>Lucky Finisher: akumulasi minimal 30 km*</span></div>
  </section>
  <footer><div className="footerBrand"><img src="/images/soedirman-runners.png" alt="Soedirman Runners"/><img src="/images/p3mdi.png" alt="P3MDI"/></div><span>*Top 3 putra dan putri akan dikecualikan dari grand prize draw setelah kategori gender diverifikasi.</span></footer>
 </main>;
}
