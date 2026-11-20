import Link from "next/link";
import leaderboard from "../../../public/leaderboard.json";
import week1 from "../../../public/data/week1.json";
import week2 from "../../../public/data/week2_latest.json";
import week3 from "../../../public/data/week3_latest.json";

type WeekRow={name:string;distance_km:number;activities:number;longest_km:number;pace_sec:number|null;elevation_m:number};
const weeks:{label:string;rows:WeekRow[]}[]=[
 {label:"Week 1",rows:week1 as WeekRow[]},
 {label:"Week 2",rows:week2 as WeekRow[]},
 {label:"Week 3",rows:week3 as WeekRow[]}
];
const key=(s:string)=>s.trim().replace(/\s+/g," ").toLocaleLowerCase("id-ID");
const fmtPace=(s:number|null)=>s===null||!Number.isFinite(s)?"—":`${Math.floor(s/60)}:${String(Math.round(s%60)).padStart(2,"0")}`;
const fmtTime=(s:number)=>{if(!Number.isFinite(s)||s<=0)return "—";const h=Math.floor(s/3600),m=Math.floor(s%3600/60),sec=Math.round(s%60);return `${h}j ${m}m ${sec}d`};
function MiniChart({title,unit,values,average,lowerIsBetter=false}:{title:string;unit:string;values:number[];average:number[];lowerIsBetter?:boolean}){
 const valid=[...values,...average].filter(Number.isFinite);
 const max=Math.max(1,...valid);
 const min=lowerIsBetter?Math.min(0,...valid):0;
 const span=Math.max(1,max-min);
 const y=(v:number)=>lowerIsBetter?18+((v-min)/span)*72:90-((v-min)/span)*72;
 const pts=(a:number[])=>a.map((v,i)=>Number.isFinite(v)?`${28+i*132},${y(v)}`:null).filter(Boolean).join(" ");
 return <section className="chartCard">
  <div className="chartTitle"><b>{title}</b><small>{unit}</small></div>
  <svg viewBox="0 0 300 116" role="img" aria-label={`${title} per minggu dibanding rata-rata`}>
   {[18,54,90].map(v=><line key={v} x1="24" x2="292" y1={v} y2={v} stroke="#26352b" strokeDasharray="3 4"/>)}
   <polyline points={pts(average)} fill="none" stroke="#89958c" strokeWidth="2" strokeDasharray="5 4"/>
   <polyline points={pts(values)} fill="none" stroke="#b7f34a" strokeWidth="3" strokeLinejoin="round" strokeLinecap="round"/>
   {values.map((v,i)=>Number.isFinite(v)?<circle key={i} cx={28+i*132} cy={y(v)} r="4" fill="#b7f34a"/>:null)}
   {["W1","W2","W3"].map((w,i)=><text key={w} x={28+i*132} y="108" textAnchor="middle" fill="#9aa69e" fontSize="9">{w}</text>)}
  </svg>
  <div className="chartLegend"><span><i className="youDot"/> Peserta</span><span><i className="avgDot"/> Rata-rata peserta</span></div>
 </section>
}
export function generateStaticParams(){return leaderboard.participants.map(p=>({slug:encodeURIComponent(p.name)}))}
export default async function AthletePage({params}:{params:Promise<{slug:string}>}){
 const {slug}=await params;
 const name=decodeURIComponent(slug);
 const person=leaderboard.participants.find(p=>key(p.name)===key(name));
 if(!person)return <main className="shell"><Link href="/">← Kembali ke leaderboard</Link><p>Peserta tidak ditemukan.</p></main>;
 const weekly=weeks.map(w=>{
  const row=w.rows.find(r=>key(r.name)===key(person.name));
  const pace=row?.pace_sec??null;
  const duration=row&&pace!==null?row.distance_km*pace:0;
  return {label:w.label,distance:row?.distance_km??0,activities:row?.activities??0,longest:row?.longest_km??0,pace,duration,elevation:row?.elevation_m??0,has:!!row};
 });
 const averages=weeks.map(w=>{
  const total=leaderboard.participants.reduce((s,p)=>s+(w.rows.find(r=>key(r.name)===key(p.name))?.distance_km??0),0);
  const paceRows=w.rows.filter(r=>r.pace_sec!==null&&r.distance_km>0);
  const pace=paceRows.length?paceRows.reduce((s,r)=>s+(r.pace_sec??0)*r.distance_km,0)/paceRows.reduce((s,r)=>s+r.distance_km,0):0;
  const duration=w.rows.reduce((s,r)=>s+(r.pace_sec===null?0:r.distance_km*r.pace_sec),0);
  const elev=w.rows.reduce((s,r)=>s+r.elevation_m,0);
  return {distance:total/leaderboard.participants.length,pace,duration:duration/leaderboard.participants.length,elevation:elev/leaderboard.participants.length};
 });
 const totalTime=weekly.reduce((s,w)=>s+w.duration,0);
 const paceValues=weekly.map(w=>w.pace===null?Number.NaN:w.pace);
 return <main className="shell detailShell">
  <Link className="backLink" href="/">← KEMBALI KE LEADERBOARD</Link>
  <header className="detailHero">
   <p className="eyebrow">ATHLETE PERFORMANCE PROFILE</p>
   <h1>{person.name}</h1>
   <p className="muted">Soedirman Strava Challenge · 2–30 November 2026</p>
   <div className="detailStats">
    <article><small>TOTAL DISTANCE</small><strong>{person.distance_km.toFixed(1)} km</strong></article>
    <article><small>TOTAL ACTIVITIES</small><strong>{person.activities}</strong></article>
    <article><small>AVG PACE</small><strong>{person.avg_pace}/km</strong></article>
    <article><small>TOTAL ELEVATION</small><strong>{person.elevation_m} m</strong></article>
   </div>
  </header>
  <section className="board detailBoard">
   <div className="boardHead"><div><p className="eyebrow">WEEKLY BREAKDOWN</p><h2>PERFORMA MINGGUAN</h2><p className="muted">Durasi merupakan estimasi dari jarak × average pace mingguan.</p></div></div>
   <div className="tableWrap"><table><thead><tr><th>MINGGU</th><th>JARAK</th><th>AKTIVITAS</th><th>LONGEST RUN</th><th>AVG PACE</th><th>EST. DURASI</th><th>ELEVATION</th></tr></thead><tbody>
    {weekly.map(w=><tr key={w.label}><td className="rank">{w.label}</td><td className="distance">{w.distance.toFixed(1)} km</td><td>{w.activities}</td><td>{w.longest.toFixed(1)} km</td><td>{fmtPace(w.pace)} /km</td><td>{fmtTime(w.duration)}</td><td>{w.elevation} m</td></tr>)}
   </tbody></table></div>
   <div className="boardFoot"><span>Total estimasi durasi: {fmtTime(totalTime)}</span><span>Rata-rata jarak dihitung dari seluruh {leaderboard.participants.length} peserta, termasuk 0 km bila tidak ada aktivitas.</span></div>
  </section>
  <section className="chartGrid">
   <MiniChart title="JARAK MINGGUAN" unit="km" values={weekly.map(w=>w.distance)} average={averages.map(a=>a.distance)}/>
   <MiniChart title="DURASI MINGGUAN" unit="jam" values={weekly.map(w=>w.duration/3600)} average={averages.map(a=>a.duration/3600)}/>
   <MiniChart title="AVERAGE PACE" unit="menit/km · lebih rendah lebih cepat" values={paceValues.map(v=>v/60)} average={averages.map(a=>a.pace/60)} lowerIsBetter/>
   <MiniChart title="ELEVATION GAIN" unit="meter" values={weekly.map(w=>w.elevation)} average={averages.map(a=>a.elevation)}/>
  </section>
  <p className="detailNote">Garis hijau menunjukkan performa peserta. Garis putus-putus menunjukkan rata-rata seluruh peserta per minggu. Data pace dan durasi merupakan estimasi berdasarkan ringkasan mingguan yang tersedia, bukan data aktivitas per aktivitas.</p>
 </main>
}
