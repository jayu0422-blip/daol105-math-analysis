# -*- coding: utf-8 -*-
"""다올105 수학 기출분석 랜딩페이지 생성 (Toss 스타일, GitHub Pages용)"""
import os, sys, shutil
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mp_data import SCHOOLS, PHONE, BRAND

OUT = r"F:\작업\다올105_수학기출분석_랜딩"
ASSETS = os.path.join(OUT, "assets")
os.makedirs(ASSETS, exist_ok=True)

def to_jpg(src, dst, maxw=1400, q=82):
    im = Image.open(src).convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(dst, "JPEG", quality=q, optimize=True)

# 에셋 변환
for s in SCHOOLS:
    for i in range(1, s["scan_n"] + 1):
        to_jpg(os.path.join(s["scan_dir"], f"{s['scan_prefix']}{i}.png"),
               os.path.join(ASSETS, f"{s['key']}_p{i}.jpg"))
    for j, (img, *_rest) in enumerate(s["killers"], 1):
        to_jpg(img, os.path.join(ASSETS, f"{s['key']}_k{j}.jpg"), maxw=1100, q=85)

CSS = """
:root{--blue:#3182F6;--blue-l:#EBF3FF;--ink:#191F28;--g6:#4E5968;--g5:#6B7684;--g4:#8B95A1;--g1:#F2F4F6;--g0:#F9FAFB;}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Pretendard Variable',Pretendard,-apple-system,'Noto Sans KR',sans-serif;color:var(--ink);background:#fff;word-break:keep-all;-webkit-font-smoothing:antialiased;}
.w{max-width:1040px;margin:0 auto;padding:0 24px;}
header{position:sticky;top:0;background:rgba(255,255,255,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--g1);z-index:50;}
header .w{display:flex;align-items:center;justify-content:space-between;height:64px;}
.logo{font-weight:800;font-size:18px;letter-spacing:-0.3px;}
.logo span{color:var(--blue);}
.hcall{background:var(--blue);color:#fff;text-decoration:none;font-weight:700;font-size:14px;padding:10px 18px;border-radius:12px;}
.hero{padding:96px 0 72px;text-align:center;}
.badge{display:inline-block;background:var(--blue-l);color:var(--blue);font-weight:700;font-size:14.5px;padding:8px 16px;border-radius:999px;}
h1{font-size:52px;font-weight:800;letter-spacing:-1.5px;line-height:1.28;margin-top:22px;}
h1 em{font-style:normal;color:var(--blue);}
.hero p{font-size:19px;color:var(--g6);line-height:1.7;margin-top:20px;}
.jump{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:36px;}
.jump a{display:block;text-decoration:none;color:var(--ink);background:var(--g0);border:1px solid var(--g1);border-radius:16px;padding:18px 26px;font-weight:700;font-size:16px;transition:.15s;}
.jump a:hover{border-color:var(--blue);color:var(--blue);}
.jump a small{display:block;font-weight:500;color:var(--g4);font-size:13px;margin-top:4px;}
.school{padding:88px 0 72px;border-top:8px solid var(--g0);}
.slabel{color:var(--blue);font-size:15px;font-weight:800;letter-spacing:.5px;}
h2{font-size:38px;font-weight:800;letter-spacing:-1px;line-height:1.32;margin-top:10px;}
h2 em{font-style:normal;color:var(--blue);}
.sinfo{font-size:15px;color:var(--g4);margin-top:14px;}
.band{background:var(--g1);border-radius:18px;padding:24px 30px;font-size:17px;line-height:1.65;color:#333D4B;margin-top:26px;}
.band b{color:var(--blue);}
h3{font-size:24px;font-weight:800;letter-spacing:-0.5px;margin:56px 0 20px;}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}
.stat{background:var(--g0);border:1px solid var(--g1);border-radius:18px;padding:24px 22px;}
.stat .n{font-size:30px;font-weight:800;color:var(--blue);letter-spacing:-0.5px;}
.stat .l{font-size:14.5px;font-weight:700;margin-top:8px;}
.stat .t{font-size:13px;color:var(--g5);line-height:1.55;margin-top:6px;}
details.scans{border:1px solid var(--g1);border-radius:18px;overflow:hidden;}
details.scans summary{cursor:pointer;list-style:none;padding:22px 28px;font-weight:700;font-size:16.5px;display:flex;align-items:center;justify-content:space-between;background:var(--g0);}
details.scans summary::after{content:'펼치기 +';color:var(--blue);font-size:14px;}
details.scans[open] summary::after{content:'접기 −';}
.sgrid{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:24px;}
.sgrid figure img{width:100%;border:1px solid #E5E8EB;border-radius:10px;display:block;}
.sgrid figcaption{font-size:13px;color:var(--g4);text-align:center;margin-top:8px;}
.twrap{overflow-x:auto;border:1px solid var(--g1);border-radius:18px;}
table{width:100%;border-collapse:collapse;min-width:720px;}
th{font-size:13px;color:var(--g4);font-weight:600;text-align:left;padding:12px 14px;border-bottom:1px solid #E5E8EB;background:var(--g0);white-space:nowrap;}
td{font-size:14px;padding:11px 14px;border-bottom:1px solid var(--g1);line-height:1.5;vertical-align:middle;}
td.no{font-weight:800;white-space:nowrap;}td.pt{font-weight:700;color:var(--blue);white-space:nowrap;}
.pill{display:inline-block;font-size:12px;font-weight:700;padding:4px 10px;border-radius:999px;white-space:nowrap;}
.pA{background:var(--g1);color:var(--g5);}.pB{background:var(--blue-l);color:var(--blue);}
.pC{background:#FFF3E0;color:#E67E00;}.pD{background:#FDEBED;color:#F04452;}
.note{font-size:14px;color:var(--g5);margin:14px 2px 0;line-height:1.6;}
.sum{background:var(--g0);border-radius:14px;padding:20px 24px;margin-top:12px;}
.sum .t{font-size:14px;font-weight:800;color:var(--blue);margin-bottom:6px;}
.sum .d{font-size:14.5px;color:var(--g6);line-height:1.6;}
.kgrid{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start;}
.k{border:1px solid #E5E8EB;border-radius:18px;overflow:hidden;}
.k .im{background:var(--g0);padding:16px;border-bottom:1px solid var(--g1);}
.k .im img{width:100%;display:block;border-radius:8px;}
.k .bd{padding:22px 24px 26px;}
.k .tg{font-size:13px;font-weight:800;color:var(--blue);margin-bottom:8px;}
.k .h{font-size:18px;font-weight:800;letter-spacing:-0.3px;line-height:1.45;margin-bottom:8px;}
.k .p{font-size:14.5px;color:var(--g6);line-height:1.65;}
.bl{background:var(--g0);border-radius:16px;padding:24px 28px;display:flex;gap:18px;margin-bottom:14px;}
.bl .n{flex:0 0 38px;width:38px;height:38px;border-radius:12px;background:var(--blue);color:#fff;font-weight:800;font-size:17px;display:flex;align-items:center;justify-content:center;}
.bl .h{font-size:17px;font-weight:800;margin-bottom:6px;line-height:1.4;}
.bl .p{font-size:14.5px;color:var(--g6);line-height:1.65;}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px;}
.rc{border:1px solid var(--g1);border-radius:16px;padding:22px 24px;}
.rc .t{font-size:16px;font-weight:800;margin-bottom:6px;}
.rc .d{font-size:14px;color:var(--g5);line-height:1.6;}
.tt{border-top:1px solid var(--g1);}
.tr{display:flex;gap:18px;padding:18px 4px;border-bottom:1px solid var(--g1);align-items:baseline;flex-wrap:wrap;}
.tr .nm{flex:0 0 240px;font-weight:800;font-size:15.5px;}
.tr .tm{flex:0 0 280px;font-size:13.5px;color:var(--blue);font-weight:700;}
.tr .ds{flex:1;min-width:200px;font-size:13.5px;color:var(--g5);line-height:1.55;}
.cta{background:var(--blue);border-radius:22px;padding:44px 40px;text-align:center;color:#fff;margin-top:56px;}
.cta .h{font-size:22px;font-weight:800;line-height:1.55;}
.cta a{display:inline-block;background:#fff;color:var(--blue);text-decoration:none;font-weight:800;font-size:17px;padding:14px 30px;border-radius:14px;margin-top:22px;}
.cta .s{font-size:14px;margin-top:14px;color:rgba(255,255,255,.8);}
footer{padding:56px 0 72px;text-align:center;color:var(--g4);font-size:14px;line-height:1.8;border-top:8px solid var(--g0);}
footer b{color:var(--g6);}
@media(max-width:860px){
 h1{font-size:34px;}h2{font-size:27px;}
 .stats{grid-template-columns:1fr 1fr;}
 .kgrid,.two,.sgrid{grid-template-columns:1fr;}
 .hero{padding:64px 0 48px;}
 .tr .nm,.tr .tm{flex:1 1 100%;}
}
"""

PCLS = {"기본": "pA", "표준": "pB", "까다로움": "pC", "까다로움+": "pC", "킬러": "pD"}

def school_html(s):
    st = "".join(f"<div class='stat'><div class='n'>{n}</div><div class='l'>{l}</div><div class='t'>{t}</div></div>"
                 for n, l, t in s["stats"])
    figs = "".join(f"<figure><img loading='lazy' src='assets/{s['key']}_p{i}.jpg' alt='{s['school']} 시험지 {i}페이지'>"
                   f"<figcaption>{i}페이지</figcaption></figure>" for i in range(1, s["scan_n"] + 1))
    rows = "".join(f"<tr><td class='no'>{no}</td><td class='pt'>{pt}</td>"
                   f"<td><span class='pill {PCLS[dif]}'>{dif}</span></td><td style='white-space:nowrap'>{area}</td>"
                   f"<td>{key}</td><td style='color:var(--g5);font-size:13px'>{src}</td></tr>"
                   for no, pt, dif, area, key, src in s["table"])
    sums = "".join(f"<div class='sum'><div class='t'>{t}</div><div class='d'>{d}</div></div>" for t, d in s["table_sum"])
    ks = "".join(f"<div class='k'><div class='im'><img loading='lazy' src='assets/{s['key']}_k{j}.jpg' alt='{tag}'></div>"
                 f"<div class='bd'><div class='tg'>{tag}</div><div class='h'>{h}</div><div class='p'>{p}</div></div></div>"
                 for j, (_img, tag, h, p) in enumerate(s["killers"], 1))
    bl = "".join(f"<div class='bl'><div class='n'>{i}</div><div><div class='h'>{t}</div><div class='p'>{p}</div></div></div>"
                 for i, (t, p) in enumerate(s["blocked"], 1))
    rc = "".join(f"<div class='rc'><div class='t'>✓ {t}</div><div class='d'>{d}</div></div>" for t, d in s["remedies"])
    tt = "".join(f"<div class='tr'><div class='nm'>{n}</div><div class='tm'>{m}</div><div class='ds'>{d}</div></div>"
                 for n, m, d in s["timetable"])
    return f"""
<section class='school' id='{s['key']}'><div class='w'>
 <div class='slabel'>{s['school']} · {s['exam']}</div>
 <h2>{s['hero_h1']}</h2>
 <p class='note' style='font-size:16px;color:var(--g6)'>{s['hero_sub']}</p>
 <div class='sinfo'>{s['hero_info']}</div>
 <div class='band'>{s['hero_band']}</div>
 <h3>숫자로 먼저 보겠습니다</h3>
 <div class='stats'>{st}</div>
 <h3>실제 시험지 전문</h3>
 <details class='scans'><summary>저희가 확보해 분석한 시험지 {s['scan_n']}페이지 전체 보기</summary><div class='sgrid'>{figs}</div></details>
 <h3>문항별 분석표</h3>
 <p class='note' style='margin:0 2px 14px'>{s['table_note']}</p>
 <div class='twrap'><table><thead><tr><th>번호</th><th>배점</th><th>체감 난이도</th><th>영역</th><th>이 문제의 관건</th><th>어디서 왔나</th></tr></thead><tbody>{rows}</tbody></table></div>
 {sums}
 <h3>{s['killer_title']}</h3>
 <div class='kgrid'>{ks}</div>
 <h3>아이들이 실제로 어디서 막혔나</h3>
 {bl}
 <h3>저희는 이렇게 잡습니다</h3>
 <p class='note' style='margin:0 2px 16px'>{s['remedy_lead']}</p>
 <div class='two'>{rc}</div>
 <h3>여름 시간표</h3>
 <div class='tt'>{tt}</div>
 <div class='cta'><div class='h'>{s['cta']}</div>
  <a href='tel:0317948158'>상담 전화 031-794-8158</a>
  <div class='s'>{PHONE} · {BRAND}</div></div>
</div></section>"""

jump = "".join(f"<a href='#{s['key']}'>{s['school']} {s['exam'].split('·')[-1].strip()}<small>{s['exam'].split('·')[0].strip()}</small></a>"
               for s in SCHOOLS)
html = f"""<!doctype html><html lang='ko'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>2026 1학기 기말 수학 기출분석 — 다올105 · 대치더올 수학과학전문관</title>
<meta name='description' content='미사고 1·2학년, 하남고 1학년 기말 수학 시험지를 문항 단위로 전수 분석했습니다. 실제 시험지 전문과 문항별 분석표.'>
<link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css'>
<style>{CSS}</style></head><body>
<header><div class='w'><div class='logo'>다올105 <span>·</span> 대치더올 수학과학전문관</div>
<a class='hcall' href='tel:0317948158'>상담 문의</a></div></header>
<section class='hero'><div class='w'>
 <div class='badge'>2026 1학기 기말 · 수학 기출분석</div>
 <h1>세 학교의 기말 수학 시험지,<br><em>문항 단위로 전부</em> 분석했습니다.</h1>
 <p>미사고 1학년 · 미사고 2학년 · 하남고 1학년.<br>시험지를 직접 확보해 문항 하나하나 출처를 확인하고, 배점 구조까지 검산한 기록입니다.</p>
 <div class='jump'>{jump}</div>
</div></section>
{''.join(school_html(s) for s in SCHOOLS)}
<footer><div class='w'><b>{BRAND}</b><br>상담 {PHONE}<br>
본 페이지의 분석 내용은 학원이 직접 확보한 시험지를 기반으로 하며, 배점·출처는 자체 교차 검산을 거쳤습니다.</div></footer>
</body></html>"""

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
tot = sum(os.path.getsize(os.path.join(ASSETS, f)) for f in os.listdir(ASSETS))
print("index.html written,", len(os.listdir(ASSETS)), "assets,", tot // 1024, "KB total")
