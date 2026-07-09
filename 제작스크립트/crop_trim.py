# -*- coding: utf-8 -*-
"""킬러 크롭 스마트 트리밍: 세로 괘선 무시, 하단 푸터/확인사항 클러스터 제거"""
import os
from PIL import Image

SCR = r"C:\Users\User\AppData\Local\Temp\claude\C--Users-User-Desktop\a7952b55-f76e-40aa-87ec-73ed3f618c4f\scratchpad"
SRC = os.path.join(SCR, "mathcrops")
DST = os.path.join(SCR, "mathcrops_t")
os.makedirs(DST, exist_ok=True)

FILES = ["g1_p5L","g1_p5R","g1_p6L","g1_p6R","g2_p5L","g2_p5R","g2_p6L","g2_p6R",
         "h1_17","h1_18","h1_19","h1_20","h1_d4"]

def trim(name):
    im = Image.open(os.path.join(SRC, name + ".png")).convert("L")
    w, h = im.size
    px = im.load()
    dark_cols = []
    for x in range(w):
        cnt = sum(1 for y in range(0, h, 4) if px[x, y] < 175)
        dark_cols.append(cnt / (h // 4 + 1) > 0.5)
    row_content = []
    for y in range(h):
        cnt = 0
        for x in range(int(w*0.02), int(w*0.98), 2):
            if not dark_cols[x] and px[x, y] < 175:
                cnt += 1
                if cnt > 4:
                    break
        row_content.append(cnt > 4)
    # 클러스터화 (간격 < 4%h 이면 병합)
    gap_merge = int(h * 0.04)
    clusters = []
    y = 0
    while y < h:
        if row_content[y]:
            start = y
            end = y
            while y < h:
                if row_content[y]:
                    end = y; y += 1
                else:
                    nxt = y
                    while nxt < h and not row_content[nxt]:
                        nxt += 1
                    if nxt < h and nxt - y <= gap_merge:
                        y = nxt
                    else:
                        break
            clusters.append((start, end))
        y += 1
    if not clusters:
        print(name, "no content?"); return
    # 아래에서부터: 직전 클러스터와 간격 > 8%h 이면 푸터로 보고 제거
    drop_gap = int(h * 0.08)
    while len(clusters) > 1 and clusters[-1][0] - clusters[-2][1] > drop_gap:
        clusters.pop()
    top = max(0, clusters[0][0] - int(h * 0.02))
    bot = min(h, clusters[-1][1] + int(h * 0.025))
    out = Image.open(os.path.join(SRC, name + ".png")).crop((0, top, w, bot))
    out.save(os.path.join(DST, name + ".png"))
    print(f"{name}: {h} -> {bot-top}  (top {top}, bot {bot})")

for f in FILES:
    trim(f)
