#!/usr/bin/env python3
"""Draw the news-image-20261122 entry: INSIDE THE DAY.
35 stories: 3 heroes + 32 numbered section stories (A WORLD, B CLIMATE &
ENERGY, C POLITICS & MARKETS, D PEOPLE). Pure PIL, deterministic output.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

INK = (20, 20, 20)
PAPER = (250, 247, 238)
RED = (178, 34, 34)
NAVY = (24, 52, 96)
GOLD = (201, 162, 39)
GREEN = (46, 125, 50)
AMBER = (176, 124, 0)
BLUE = (31, 78, 121)
PURPLE = (106, 27, 154)
ORANGE = (214, 81, 0)
GREY = (90, 90, 90)
LGREY = (120, 120, 120)
LINE = (180, 175, 165)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    """Wrap text to fit max_w; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(d, text, f, max_w, max_lines):
    """Wrap and truncate with ellipsis to max_lines."""
    lines = wrap(d, text, f, max_w)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and d.textlength(lines[-1] + " ...", font=f) > max_w:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1] + " ..."
    return lines


def chip(d, x, y, text, f, fg, bg):
    w = int(d.textlength(text, font=f)) + 10
    h = f.size + 6
    d.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=bg)
    d.text((x + 5, y + 3), text, font=f, fill=fg)
    return w


def draw_tanker(d, x, y, w, h):
    # sea
    d.rectangle([x, y + h - 12, x + w, y + h - 8], fill=(70, 130, 180))
    # hull
    d.polygon([(x + 8, y + h - 28), (x + w - 8, y + h - 28),
               (x + w - 22, y + h - 12), (x + 22, y + h - 12)], fill=(40, 40, 48))
    d.rectangle([x + 30, y + h - 44, x + 52, y + h - 28], fill=(120, 120, 120))
    # fire
    cx = x + w // 2
    d.polygon([(cx - 26, y + h - 28), (cx - 8, y + 6), (cx + 2, y + h - 28)],
              fill=(230, 120, 20))
    d.polygon([(cx - 4, y + h - 28), (cx + 10, y + 14), (cx + 24, y + h - 28)],
              fill=(245, 180, 40))
    # mine starburst
    mx, my = x + w - 26, y + 12
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line([mx, my, mx + 10 * math.cos(a), my + 10 * math.sin(a)],
               fill=(20, 20, 20), width=2)
    d.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=(20, 20, 20))


def draw_globe(d, x, y, w, h):
    cx, cy, r = x + w // 2, y + h // 2, min(w, h) // 2 - 2
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 160, 90),
              outline=(30, 90, 40), width=2)
    d.ellipse([cx - r + 8, cy - r + 6, cx - r + 22, cy - r + 18], fill=(40, 110, 50))
    d.ellipse([cx + 2, cy + 4, cx + 18, cy + 16], fill=(40, 110, 50))
    d.ellipse([cx - 14, cy + 8, cx + 2, cy + 22], fill=(40, 110, 50))
    # cracks: no deal
    d.line([cx - r + 4, cy - r + 10, cx + 6, cy + 2, cx + r - 6, cy - r + 14],
           fill=(178, 34, 34), width=3)
    d.line([cx - 10, cy + r - 4, cx + 2, cy + 8, cx + 14, cy + r - 8],
           fill=(178, 34, 34), width=3)


def draw_capitol(d, x, y, w, h):
    cx = x + w // 2
    # dome
    d.pieslice([cx - 26, y + 2, cx + 26, y + 44], 180, 360, fill=(240, 240, 240),
               outline=(60, 60, 60))
    d.rectangle([cx - 3, y, cx + 3, y + 6], fill=(60, 60, 60))
    # base + columns
    d.rectangle([cx - 34, y + h - 22, cx + 34, y + h - 8], fill=(240, 240, 240),
                outline=(60, 60, 60))
    for i in range(-2, 3):
        d.rectangle([cx + i * 13 - 3, y + h - 22, cx + i * 13 + 3, y + h - 10],
                    fill=(120, 120, 120))
    d.rectangle([x + 6, y + h - 8, x + w - 6, y + h - 4], fill=(60, 60, 60))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # top red rule
    d.rectangle([0, 0, W, 8], fill=RED)

    # ---- masthead ----
    d.text((24, 16), "THE WORLD TODAY", font=font(SERIF_B, 48), fill=INK)
    d.text((1000, 36), "SUNDAY 22 NOVEMBER 2026", font=font(SERIF_B, 22),
           fill=RED, anchor="ra")
    d.line([24, 76, 1000, 76], fill=INK, width=2)
    d.text((24, 82), "INSIDE THE DAY", font=font(SANS_B, 15), fill=RED)
    d.text((168, 83), "·  35 STORIES  ·  EVERY ITEM FIRST REPORTED 22 NOV",
           font=font(SANS, 13), fill=INK)
    # legend, right-aligned: measure first so nothing runs off-canvas
    _lf = font(SANS_B, 10)
    _chips = [("ONGOING", NAVY), ("CLAIM", AMBER), ("REPORTED", GREEN)]
    _widths = [int(d.textlength(t, font=_lf)) + 10 for t, _ in _chips]
    lx = 1000 - sum(_widths) - 12
    for (txt, bg), w in zip(_chips, _widths):
        chip(d, lx, 82, txt, _lf, (255, 255, 255), bg)
        lx += w + 6

    # ---- contents strip ----
    d.rectangle([24, 106, 1000, 132], fill=NAVY)
    d.text((36, 112), "INSIDE  →", font=font(SANS_B, 14), fill=(255, 255, 255))
    cx = 150
    for letter, name, col in [("A", "WORLD", BLUE), ("B", "CLIMATE & ENERGY", GREEN),
                              ("C", "POLITICS & MARKETS", PURPLE),
                              ("D", "PEOPLE", ORANGE)]:
        t = f"SECTION {letter}: {name}"
        f = font(SANS_B, 13)
        w = int(d.textlength(t, font=f)) + 16
        d.rounded_rectangle([cx, 110, cx + w, 128], radius=3, fill=col)
        d.text((cx + 8, 113), t, font=f, fill=(255, 255, 255))
        cx += w + 10

    # ---- heroes ----
    heroes = [
        ("CONFLICT · STRAIT OF HORMUZ · 17:13 UTC", NAVY, "2 TANKERS HIT",
         "Two supertankers hit mines east of the Strait; both on fire. "
         "First reported 17:13 UTC.", "REPORTED", "Iran navy · AP", draw_tanker),
        ("CLIMATE · ANTALYA", RED, "NO DEAL",
         "COP31 collapses; EU + ~130 parties reject text with no "
         "fossil-fuel language.", "REPORTED", "CNN · Reuters", draw_globe),
        ("POLITICS · WASHINGTON · 18:00 UTC", NAVY, "258",
         "Dems win House, largest majority since 1992; Hubbard beats "
         "Foxx by 330 in NC.", "REPORTED", "AP · Reuters", draw_capitol),
    ]
    hx, hw, hy, hh = 24, 320, 140, 158
    for i, (kick, kcol, head, body, badge, src, art) in enumerate(heroes):
        x = hx + i * (hw + 8)
        d.rectangle([x, hy, x + hw, hy + hh], outline=INK, width=2, fill=(255, 255, 255))
        d.rectangle([x, hy, x + hw, hy + 22], fill=kcol)
        d.text((x + 8, hy + 4), kick, font=font(SANS_B, 11), fill=(255, 255, 255))
        art(d, x + (hw - 84) // 2, hy + 24, 84, 40)
        d.text((x + 8, hy + 68), head, font=font(SERIF_B, 30), fill=INK)
        bl = fit_lines(d, body, font(SANS, 12), hw - 16, 2)
        by = hy + 104
        for ln in bl:
            d.text((x + 8, by), ln, font=font(SANS, 12), fill=(40, 40, 40))
            by += 16
        chip(d, x + 8, hy + hh - 24, badge, font(SANS_B, 10), (255, 255, 255), GREEN)
        d.text((x + 84, hy + hh - 22), src, font=font(SANS, 11), fill=GREY)

    # ---- numbers strip ----
    d.rectangle([24, 306, 1000, 336], fill=NAVY)
    nums = [("258", "House seats"), ("2", "tankers hit"), ("194", "COP31 parties"),
            ("330", "votes in NC"), ("36", "missing in Banten"),
            ("1,661", "Gaza toll")]
    nx = 40
    for n, lab in nums:
        d.text((nx, 310), n, font=font(SERIF_B, 20), fill=GOLD)
        w = d.textlength(n, font=font(SERIF_B, 20))
        d.text((nx + w + 6, 315), lab, font=font(SANS, 12), fill=(255, 255, 255))
        nx += int(w) + int(d.textlength(lab, font=font(SANS, 12))) + 34

    # ---- sections ----
    # (number, headline, body, source, claim?)
    A = [
        (4, "Dymer drone hits flats", "7 killed near Kyiv; boy pulled alive from rubble", "Al Jazeera", False),
        (5, "Merkury hit at Benghazi", "Russian corvette hit by sea drone, satellite images show", "France 24", True),
        (6, "Khartoum drones kill 4", "Strikes blamed on RSF; UN building damaged", "AP", True),
        (7, "Zelenskyy pleads for Patriots", "Russia fired ~2,700 drones in a week", "BBC", False),
        (8, "Iran shows missile city", "Underground base unveiled on state TV", "IRGC media", False),
        (9, "Saudis stop Houthi attack", "Drone+missile downed; Rabigh claimed", "Reuters", True),
        (10, "Bahrain blames Iran", "Industrial site struck; UAE condemns", "France 24", False),
        (11, "UAE condemns Bahrain strike", "Calls it a sovereignty violation", "WAM", False),
        (12, "Europe protests, day 3", "Cost marches; 144 held in France", "AP", False),
        (13, "Settlers burn West Bank cars", "12 vehicles torched near Ramallah", "Guardian", False),
        (14, "Benghazi depot blast", "Ammo depot explodes inside naval base", "Local auth.", False),
    ]
    B = [
        (15, "COP31: why the talks failed", "Text with no fossil-fuel language rejected by EU + ~130", "Reuters", False),
        (16, "Russian cargo ship burns", "Fire aboard vessel in the Baltic", "Al Jazeera", False),
        (17, "EU–Indonesia trade deal", "Pact signed after years of talks", "EU", False),
        (18, "Asian stocks slide", "War fears hit markets across the region", "SCMP", False),
        (19, "Fidan: war fallout hits markets", "US–Israel war burden threatens trade", "Anadolu", False),
    ]
    C = [
        (20, "Eisenkot–Likud unity talks stall", "Wide gap on unity govt", "Israeli media", False),
        (21, "Finland: war spills over", "Baltic shipping at risk as drones spread", "Finnish govt", False),
        (22, "Mongolia snap vote", "President quits; early election to follow", "Euronews", False),
        (23, "Mexico cartel boss captured", "11 killed in the operation", "Al Jazeera", False),
        (24, "Korea minister quits over AI cheat", "111 device cases found in exam", "BBC", False),
        (25, "Fidan: Israel may use Druze", "Ankara warns of Syria operation pretext", "Anadolu", True),
    ]
    D = [
        (26, "Banten factory fire", "3 dead, 36 missing after candy-plant blaze", "BBC", False),
        (27, "Gaza aid van strike", "WCK: three killed were not its team", "WCK", False),
        (28, "Gaza: 350,000 homeless", "Families displaced near Yellow Line", "Al Jazeera", False),
        (29, "Settlers attack Hebron homes", "Homes attacked; tear gas fired", "WAFA", False),
        (30, "Gaza homes blocked", "Turkey: Israel blocks container homes", "Anadolu", True),
        (31, "Germany urged to arrest soldier", "Hind Rajab Foundation files complaint", "HRF", False),
        (32, "Fred Nile dies at 92", "Died 21 Nov, announced 22 Nov", "Guardian", False),
        (33, "Gamer rescues missing girl", "Teen, 16, and mother help FBI find girl", "FBI", False),
        (34, "Gaza toll 1,661", "Death toll since Oct 2025 ceasefire", "Gaza health min.", False),
        (35, "Paolo Bulgari dies at 89", "Death announced 22 Nov; funeral Monday", "AP", False),
    ]
    sections = [("A", "WORLD", BLUE, A), ("B", "CLIMATE & ENERGY", GREEN, B),
                ("C", "POLITICS & MARKETS", PURPLE, C), ("D", "PEOPLE", ORANGE, D)]

    y = 342
    f_num = font(SANS_B, 13)
    f_head = font(SANS_B, 13)
    f_body = font(SANS, 11)
    f_src = font(SANS, 10)
    ROW = 30
    for letter, name, col, items in sections:
        d.rectangle([24, y, 1000, y + 23], fill=col)
        d.text((32, y + 4), f"SECTION {letter} — {name}",
               font=font(SANS_B, 13), fill=(255, 255, 255))
        d.text((1000, y + 5), f"{len(items)} STORIES", font=font(SANS_B, 11),
               fill=(255, 255, 255), anchor="ra")
        y += 23
        for i, (n, head, body, src, claim) in enumerate(items):
            row = i // 2
            c = i % 2
            x0 = 24 + c * 492
            ry = y + row * ROW
            d.text((x0, ry), f"{n:02d}", font=f_num, fill=RED)
            hx0 = x0 + 26
            # headline, truncated to fit with source
            src_w = d.textlength(src, font=f_src) + 8
            head_lines = fit_lines(d, head, f_head, 492 - 26 - src_w - 4, 1)
            d.text((hx0, ry), head_lines[0], font=f_head, fill=INK)
            d.text((x0 + 492 - src_w, ry + 1), src, font=f_src, fill=LGREY)
            if claim:
                hw_ = d.textlength(head_lines[0], font=f_head)
                chip(d, int(hx0 + hw_ + 6), ry, "CLAIM", font(SANS_B, 9),
                     (255, 255, 255), AMBER)
            d.text((hx0, ry + 14), body, font=f_body, fill=(60, 60, 60))
            if c == 0:
                d.line([x0 + 486, ry + 2, x0 + 486, ry + 27], fill=LINE, width=1)
        y += ((len(items) + 1) // 2) * ROW + 4

    # ---- footer ----
    d.rectangle([24, 964, 1000, 981], fill=(245, 222, 120))
    d.text((32, 967), "NOT YET — DO NOT READ AS DONE:  4 House races uncalled  ·  "
           "COP32 venue not set  ·  Gaza ceasefire talks: no deal announced",
           font=font(SANS_B, 11), fill=INK)
    d.text((24, 985),
           "DATE CHECK — Every story first reported 22 Nov.  EXCLUDED: El Chapo Isidro 20 Nov · "
           "BepiColombo 21 Nov · ICJ Myanmar 19 Nov · Wall St rout 20 Nov · FBI NCIC hack 21 Nov.",
           font=font(SANS, 10), fill=GREY)
    d.text((24, 998),
           "LEGEND: REPORTED = confirmed by 2+ sources · CLAIM = one side alleges, unverified · "
           "ONGOING = still developing.",
           font=font(SANS, 10), fill=GREY)
    d.text((24, 1011),
           "SOURCES: AP · Reuters · BBC · CNN · France 24 · Al Jazeera · Guardian · SCMP · "
           "Anadolu · WAFA · WCK · HRF · FBI",
           font=font(SANS, 10), fill=GREY)

    img.save(OUT, "PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
