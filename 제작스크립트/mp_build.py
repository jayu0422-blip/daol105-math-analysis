# -*- coding: utf-8 -*-
"""3개교 수학 기출분석 블로그 상세페이지 — Toss 스타일 섹션 PNG 빌더"""
import os, subprocess, sys, pathlib
from PIL import Image, ImageChops
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mp_data import SCHOOLS, PHONE, BRAND

SCR = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
GM_B = pathlib.Path(r"C:\Users\User\AppData\Local\Microsoft\Windows\Fonts\GmarketSansTTFBold.ttf").as_uri()
GM_M = pathlib.Path(r"C:\Users\User\AppData\Local\Microsoft\Windows\Fonts\GmarketSansTTFMedium.ttf").as_uri()
NOTO = pathlib.Path(r"C:\Windows\Fonts\NotoSansKR-VF.ttf").as_uri()

CSS = f"""
@font-face {{ font-family:'GmB'; src:url('{GM_B}'); }}
@font-face {{ font-family:'GmM'; src:url('{GM_M}'); }}
@font-face {{ font-family:'NotoKR'; src:url('{NOTO}'); font-weight:100 900; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:1240px; background:#FFFFFF; color:#191F28; font-family:'NotoKR',sans-serif;
       -webkit-font-smoothing:antialiased; word-break:keep-all; }}
.wrap {{ width:1240px; padding:72px 80px 64px; }}
.gb {{ font-family:'GmB'; }} .gm {{ font-family:'GmM'; }}
.badge {{ display:inline-block; background:#EBF3FF; color:#3182F6; font-weight:700;
          font-size:16px; padding:9px 18px; border-radius:999px; letter-spacing:-0.2px; }}
.slabel {{ color:#3182F6; font-size:17px; font-weight:800; letter-spacing:0.5px; margin-bottom:14px; }}
h1 {{ font-family:'GmB'; font-size:62px; line-height:1.24; letter-spacing:-1.5px; font-weight:400; }}
h1 em {{ font-style:normal; color:#3182F6; }}
h2 {{ font-family:'GmB'; font-size:40px; line-height:1.3; letter-spacing:-1px; font-weight:400; }}
.sub {{ font-size:20px; color:#4E5968; line-height:1.68; }}
.info {{ font-size:15.5px; color:#8B95A1; }}
.band {{ background:#F2F4F6; border-radius:20px; padding:30px 38px; font-size:19.5px;
         line-height:1.62; color:#333D4B; }}
.band b {{ color:#3182F6; }}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; }}
.stat {{ background:#F9FAFB; border:1px solid #F2F4F6; border-radius:24px; padding:36px 34px; }}
.stat .num {{ font-family:'GmB'; font-size:50px; color:#3182F6; letter-spacing:-1px; }}
.stat .lb {{ font-size:19px; font-weight:700; margin-top:12px; }}
.stat .nt {{ font-size:15.5px; color:#6B7684; line-height:1.58; margin-top:8px; }}
figure {{ text-align:center; }}
figure img {{ width:100%; border:1px solid #E5E8EB; border-radius:12px;
              box-shadow:0 4px 16px rgba(25,31,40,.07); display:block; }}
figcaption {{ font-size:14.5px; color:#8B95A1; margin-top:10px; }}
table {{ width:100%; border-collapse:collapse; }}
th {{ font-size:14.5px; color:#8B95A1; font-weight:600; text-align:left;
      padding:12px 13px; border-bottom:1px solid #E5E8EB; white-space:nowrap; }}
td {{ font-size:15.5px; padding:12px 13px; border-bottom:1px solid #F2F4F6;
      line-height:1.45; vertical-align:middle; }}
td.no {{ font-weight:800; white-space:nowrap; }} td.pt {{ font-weight:700; color:#3182F6; white-space:nowrap; }}
.pill {{ display:inline-block; font-size:13.5px; font-weight:700; padding:5px 12px;
         border-radius:999px; white-space:nowrap; }}
.p기본 {{ background:#F2F4F6; color:#6B7684; }} .p표준 {{ background:#EBF3FF; color:#3182F6; }}
.p까다로움, .pplus {{ background:#FFF3E0; color:#E67E00; }} .p킬러 {{ background:#FDEBED; color:#F04452; }}
.sumcard {{ background:#F9FAFB; border-radius:18px; padding:26px 32px; margin-top:16px; }}
.sumcard .t {{ font-size:16px; font-weight:800; color:#3182F6; margin-bottom:8px; }}
.sumcard .d {{ font-size:16.5px; color:#4E5968; line-height:1.62; }}
.kcard {{ border:1px solid #E5E8EB; border-radius:24px; overflow:hidden; background:#fff; }}
.kimg {{ background:#F9FAFB; padding:22px; border-bottom:1px solid #F2F4F6; }}
.kimg img {{ width:100%; display:block; border-radius:8px; }}
.kbody {{ padding:30px 32px 34px; }}
.ktag {{ font-size:14.5px; font-weight:800; color:#3182F6; margin-bottom:12px; }}
.kh {{ font-family:'GmB'; font-size:23px; line-height:1.4; letter-spacing:-0.5px; margin-bottom:12px; }}
.kp {{ font-size:16px; color:#4E5968; line-height:1.66; }}
.bcard {{ background:#F9FAFB; border-radius:20px; padding:34px 38px; display:flex; gap:26px; }}
.bnum {{ flex:0 0 52px; width:52px; height:52px; border-radius:16px; background:#3182F6; color:#fff;
         font-family:'GmB'; font-size:24px; display:flex; align-items:center; justify-content:center; }}
.bh {{ font-family:'GmB'; font-size:23px; letter-spacing:-0.5px; margin-bottom:10px; line-height:1.4; }}
.bp {{ font-size:16.5px; color:#4E5968; line-height:1.66; }}
.rlead {{ background:#F2F4F6; border-radius:20px; padding:30px 38px; font-size:18px;
          color:#333D4B; line-height:1.66; }}
.rcard {{ border:1px solid #E5E8EB; border-radius:20px; padding:30px 32px; }}
.rcard .ck {{ width:34px; height:34px; border-radius:50%; background:#EBF3FF; color:#3182F6;
              font-weight:900; font-size:18px; display:flex; align-items:center; justify-content:center; margin-bottom:16px; }}
.rcard .t {{ font-family:'GmB'; font-size:20px; letter-spacing:-0.5px; margin-bottom:10px; }}
.rcard .d {{ font-size:15.5px; color:#6B7684; line-height:1.6; }}
.trow {{ display:flex; align-items:flex-start; gap:24px; padding:26px 8px; border-bottom:1px solid #F2F4F6; }}
.trow .nm {{ flex:0 0 300px; font-family:'GmB'; font-size:20px; letter-spacing:-0.5px; line-height:1.4; }}
.trow .tm {{ flex:0 0 330px; font-size:15.5px; color:#3182F6; font-weight:700; line-height:1.55; }}
.trow .ds {{ font-size:15.5px; color:#6B7684; line-height:1.6; }}
.cta {{ background:#3182F6; border-radius:28px; padding:60px 64px; text-align:center; color:#fff; }}
.cta .h {{ font-family:'GmB'; font-size:32px; line-height:1.5; letter-spacing:-0.5px; }}
.cta .ph {{ font-family:'GmB'; font-size:30px; margin-top:30px; letter-spacing:0.5px; }}
.cta .br {{ font-size:16px; margin-top:12px; color:rgba(255,255,255,.75); }}
"""

def page(body):
    return ("<!doctype html><html><head><meta charset='utf-8'><style>" + CSS +
            "</style></head><body><div class='wrap'>" + body + "</div></body></html>")

def shead(label, title):
    return f"<div class='slabel'>{label}</div><h2>{title}</h2>"

def sec_hero(s):
    return page(
        f"<div class='badge'>{s['badge']}</div>"
        f"<div class='info' style='margin-top:26px;font-weight:700;color:#4E5968;font-size:18px'>{s['school']} · {s['exam']}</div>"
        f"<h1 style='margin-top:16px'>{s['hero_h1']}</h1>"
        f"<div class='sub' style='margin-top:26px'>{s['hero_sub']}</div>"
        f"<div class='info' style='margin-top:22px'>{s['hero_info']}</div>"
        f"<div class='band' style='margin-top:34px'>{s['hero_band']}</div>")

def sec_stats(s):
    cards = "".join(f"<div class='stat'><div class='num'>{n}</div><div class='lb'>{l}</div><div class='nt'>{t}</div></div>"
                    for n, l, t in s["stats"])
    return page(shead("숫자로 먼저 보겠습니다", "이번 시험의 성격, 네 개의 숫자에 다 있습니다")
                + f"<div class='grid2' style='margin-top:36px'>{cards}</div>")

def sec_scans(s):
    figs = "".join(
        f"<figure><img src='{pathlib.Path(os.path.join(s['scan_dir'], s['scan_prefix'] + str(i) + '.png')).as_uri()}'>"
        f"<figcaption>{s['school']} 기말 수학 · {i}페이지</figcaption></figure>"
        for i in range(1, s["scan_n"] + 1))
    return page(shead("실제 시험지", "저희가 확보해 분석한 시험지 전문입니다")
                + "<div class='sub' style='margin-top:14px;font-size:17px'>직접 확인하실 수 있도록 실물 전 페이지를 그대로 싣습니다.</div>"
                + f"<div class='grid2' style='margin-top:34px'>{figs}</div>")

def sec_table(s):
    rows = ""
    for no, pt, dif, area, key, src in s["table"]:
        pcls = "pplus" if dif == "까다로움+" else "p" + dif
        rows += (f"<tr><td class='no'>{no}</td><td class='pt'>{pt}</td>"
                 f"<td><span class='pill {pcls}'>{dif}</span></td><td style='white-space:nowrap'>{area}</td>"
                 f"<td>{key}</td><td style='color:#6B7684;font-size:14.5px'>{src}</td></tr>")
    sums = "".join(f"<div class='sumcard'><div class='t'>{t}</div><div class='d'>{d}</div></div>"
                   for t, d in s["table_sum"])
    return page(shead("문항별 분석표", "전 문항, 출처까지 하나씩 확인했습니다")
                + f"<div class='sub' style='margin-top:14px;font-size:17px'>{s['table_note']}</div>"
                + "<table style='margin-top:30px'><thead><tr><th>번호</th><th>배점</th><th>체감 난이도</th>"
                  "<th>영역</th><th>이 문제의 관건</th><th>어디서 왔나</th></tr></thead>"
                + f"<tbody>{rows}</tbody></table>" + sums)

def sec_killers(s):
    cards = "".join(
        f"<div class='kcard'><div class='kimg'><img src='{pathlib.Path(img).as_uri()}'></div>"
        f"<div class='kbody'><div class='ktag'>{tag}</div><div class='kh'>{h}</div><div class='kp'>{p}</div></div></div>"
        for img, tag, h, p in s["killers"])
    return page(shead("문제 실물", s["killer_title"])
                + "<div class='sub' style='margin-top:14px;font-size:17px'>실제 시험지에서 그대로 잘라 왔습니다.</div>"
                + f"<div class='grid2' style='margin-top:34px;align-items:start'>{cards}</div>")

def sec_blocked(s):
    cards = "".join(
        f"<div class='bcard'><div class='bnum'>{i}</div><div><div class='bh'>{t}</div><div class='bp'>{p}</div></div></div>"
        for i, (t, p) in enumerate(s["blocked"], 1))
    return page(shead("채점 후 기록", "아이들이 실제로 어디서 막혔나")
                + f"<div style='display:flex;flex-direction:column;gap:20px;margin-top:36px'>{cards}</div>")

def sec_remedy(s):
    rc = "".join(f"<div class='rcard'><div class='ck'>✓</div><div class='t'>{t}</div><div class='d'>{d}</div></div>"
                 for t, d in s["remedies"])
    tt = "".join(f"<div class='trow'><div class='nm'>{n}</div><div class='tm'>{m}</div><div class='ds'>{d}</div></div>"
                 for n, m, d in s["timetable"])
    return page(shead("저희는 이렇게 잡습니다", "이번 시험이 요구한 걸 그대로 훈련합니다")
                + f"<div class='rlead' style='margin-top:30px'>{s['remedy_lead']}</div>"
                + f"<div class='grid2' style='margin-top:26px'>{rc}</div>"
                + "<h2 style='margin-top:64px;font-size:32px'>여름 시간표</h2>"
                + f"<div style='margin-top:12px'>{tt}</div>"
                + f"<div class='cta' style='margin-top:56px'><div class='h'>{s['cta']}</div>"
                + f"<div class='ph'>{PHONE}</div><div class='br'>{BRAND}</div></div>")

SECTIONS = [("01_표지", sec_hero, 1500), ("02_핵심숫자", sec_stats, 1900),
            ("03_시험지_전문", sec_scans, 3900), ("04_분석표", sec_table, 3400),
            ("05_문제실물", sec_killers, 6600), ("06_어디서_막혔나", sec_blocked, 2400),
            ("07_공부방향_시간표", sec_remedy, 3400)]

WHITE_T = 250
def trim_save(src_png, dst_png, pad=110):
    im = Image.open(src_png).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bbox = ImageChops.difference(im, bg).getbbox()
    bottom = min(im.height, (bbox[3] if bbox else im.height) + pad)
    im.crop((0, 0, im.width, bottom)).save(dst_png, optimize=True)

def render(html_path, out_png, h):
    tmp = html_path[:-5] + "_raw.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--force-device-scale-factor=2",
                    f"--window-size=1240,{h}", f"--screenshot={tmp}",
                    pathlib.Path(html_path).as_uri()],
                   check=True, capture_output=True, timeout=120)
    trim_save(tmp, out_png)
    os.remove(tmp)

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    sec = sys.argv[2] if len(sys.argv) > 2 else None
    for s in SCHOOLS:
        if only and only != "all" and s["key"] != only:
            continue
        os.makedirs(s["out"], exist_ok=True)
        hdir = os.path.join(SCR, s["key"])
        os.makedirs(hdir, exist_ok=True)
        for name, fn, h in SECTIONS:
            if sec and sec not in name:
                continue
            hp = os.path.join(hdir, name + ".html")
            with open(hp, "w", encoding="utf-8") as f:
                f.write(fn(s))
            out = os.path.join(s["out"], name + ".png")
            render(hp, out, h)
            im = Image.open(out)
            print(f"{s['key']}/{name}.png  {im.size[0]}x{im.size[1]}  {os.path.getsize(out)//1024}KB")

if __name__ == "__main__":
    main()
