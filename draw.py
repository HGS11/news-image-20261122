from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024
MARGIN = 18
CONTENT_W = WIDTH - 2 * MARGIN

BG_CREAM = (247, 243, 232)
NAVY = (19, 35, 56)
DARK_SLATE = (28, 43, 58)
INK = (20, 20, 20)
MUTED = (72, 72, 68)
RULE = (180, 174, 160)
DARK_RULE = (35, 35, 35)
RED = (178, 34, 34)
WHITE = (255, 255, 255)
OFF_WHITE = (242, 239, 230)
GOLD = (218, 165, 32)

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def load_font(path, size):
    return ImageFont.truetype(path, size)


def text_size(draw, text, font):
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw, text, font, max_width):
    words = text.split(" ")
    lines = []
    cur = ""
    for word in words:
        cand = word if not cur else cur + " " + word
        w, _ = text_size(draw, cand, font)
        if w <= max_width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, font, color, max_width, line_height, max_lines=None):
    lines = wrap_text(draw, text, font, max_width)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines[-1] and text_size(draw, lines[-1] + "...", font)[0] > max_width:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1].rstrip(" .,;:") + "..."
    cy = y
    for line in lines:
        draw.text((x, cy), line, font=font, fill=color)
        cy += line_height
    return cy


def draw_lead_illustration(draw, kind, x, y, w, h):
    if kind == "ukraine":
        draw.rectangle([x, y, x + w, y + h], fill=(17, 25, 42))
        draw.ellipse([x + 18, y + 8, x + 40, y + 30], fill=(235, 224, 185))
        draw.rectangle([x, y + h - 18, x + w, y + h], fill=(28, 34, 48))
        bx = x + 36
        bw = 96
        by = y + 20
        bh = h - 20
        draw.rectangle([bx, by, bx + bw, by + bh], fill=(74, 80, 92))
        draw.polygon([(bx + bw - 28, by), (bx + bw, by), (bx + bw, by + 26)], fill=(17, 25, 42))
        draw.polygon([(bx + bw - 26, by + 18), (bx + bw - 6, by + 6), (bx + bw - 10, by + 28)], fill=(235, 110, 35))
        for row in range(5):
            for col in range(4):
                if row < 2 and col == 3:
                    continue
                wx = bx + 8 + col * 21
                wy = by + 6 + row * 11
                lit = (row + col) % 3 == 0
                wcol = (240, 196, 84) if lit else (34, 40, 52)
                draw.rectangle([wx, wy, wx + 12, wy + 7], fill=wcol)
        for dx, dy in [(x + 175, y + 18), (x + 225, y + 12), (x + 265, y + 28)]:
            draw.polygon([(dx, dy), (dx + 14, dy + 5), (dx + 4, dy + 9)], fill=(210, 215, 225))
            draw.line([(dx + 16, dy + 6), (dx + 34, dy + 2)], fill=(200, 90, 45), width=2)
        draw.line([(x + 160, y + h - 8), (x + 218, y + 24)], fill=(115, 210, 150), width=2)
        draw.ellipse([x + 212, y + 18, x + 226, y + 32], fill=(250, 165, 55))
        draw.rectangle([x, y, x + w, y + h], outline=DARK_RULE, width=1)

    elif kind == "cop31":
        draw.rectangle([x, y, x + w, y + 26], fill=(38, 72, 102))
        draw.rectangle([x, y + 26, x + w, y + 48], fill=(118, 128, 124))
        draw.rectangle([x, y + 48, x + w, y + 66], fill=(224, 156, 86))
        draw.rectangle([x, y + 66, x + w, y + h], fill=(28, 86, 118))
        draw.chord([x + 26, y + 22, x + 152, y + 82], 180, 360, fill=(235, 232, 224))
        draw.rectangle([x + 20, y + 50, x + 158, y + 68], fill=(210, 206, 196))
        for cx in range(32, 150, 18):
            draw.rectangle([x + cx, y + 52, x + cx + 8, y + 66], fill=(55, 75, 95))
        px, py = x + 190, y + 12
        draw.rectangle([px, py, px + 54, py + 56], fill=(248, 245, 238), outline=(80, 80, 80))
        for ly in range(py + 9, py + 48, 9):
            draw.line([(px + 8, ly), (px + 46, ly)], fill=(120, 120, 120), width=2)
        draw.line([(px + 10, py + 10), (px + 44, py + 46)], fill=RED, width=4)
        draw.line([(px + 44, py + 10), (px + 10, py + 46)], fill=RED, width=4)
        draw.line([(x + 264, y + 58), (x + 282, y + 44), (x + 306, y + 18)], fill=(195, 45, 38), width=3)
        draw.line([(x + 262, y + 36), (x + 308, y + 36)], fill=(250, 245, 220), width=1)
        draw.rectangle([x, y, x + w, y + h], outline=DARK_RULE, width=1)

    elif kind == "bahrain":
        draw.rectangle([x, y, x + w, y + h], fill=(24, 28, 44))
        draw.rectangle([x, y + h - 24, x + w, y + h], fill=(138, 114, 82))
        draw.rectangle([x + 195, y + h - 20, x + w, y + h], fill=(32, 68, 98))
        for rx in [x + 36, x + 98]:
            draw.rectangle([rx, y + h - 38, rx + 24, y + h - 24], fill=(105, 110, 118))
            draw.polygon([(rx + 4, y + h - 38), (rx + 28, y + h - 58), (rx + 22, y + h - 38)], fill=(175, 180, 188))
        draw.arc([x + 35, y + 10, x + 195, y + 80], 190, 350, fill=(225, 82, 52), width=2)
        draw.arc([x + 65, y + 18, x + 225, y + 80], 200, 345, fill=(240, 145, 60), width=2)
        ix, iy = x + 148, y + 22
        draw.ellipse([ix - 9, iy - 9, ix + 9, iy + 9], fill=(250, 210, 90))
        draw.rectangle([x + 225, y + h - 42, x + 275, y + h - 20], fill=(135, 140, 145))
        draw.rectangle([x + 280, y + h - 54, x + 292, y + h - 20], fill=(110, 115, 120))
        draw.polygon([(x + 240, y + h - 42), (x + 252, y + h - 62), (x + 266, y + h - 42)], fill=(238, 105, 38))
        draw.ellipse([x + 245, y + 8, x + 275, y + 26], fill=(75, 78, 86))
        draw.rectangle([x, y, x + w, y + h], outline=DARK_RULE, width=1)


def draw_med_illustration(draw, idx, x, y, w, h):
    if idx == 4:  # HK Election
        draw.rectangle([x, y, x + w, y + h], fill=(35, 58, 84))
        for bx, bh in [(10, 28), (28, 36), (48, 24), (110, 34), (130, 26)]:
            draw.rectangle([x + bx, y + h - bh, x + bx + 14, y + h], fill=(56, 82, 112))
        draw.rectangle([x + 64, y + 14, x + 102, y + h - 2], fill=(236, 232, 224))
        draw.rectangle([x + 70, y + 17, x + 96, y + 21], fill=(30, 30, 30))
        draw.polygon([(x + 74, y + 4), (x + 94, y + 4), (x + 90, y + 19), (x + 74, y + 19)], fill=(255, 255, 255))
        draw.rectangle([x + 76, y + 26, x + 90, y + 36], fill=RED)
    elif idx == 5:  # Cricket 720/9
        draw.rectangle([x, y, x + w, y + h], fill=(58, 124, 68))
        draw.polygon([(x + 35, y + h), (x + 120, y + h), (x + 102, y + 14), (x + 52, y + 14)], fill=(208, 188, 144))
        for sx in [70, 77, 84]:
            draw.line([(x + sx, y + 16), (x + sx, y + 38)], fill=(245, 235, 200), width=2)
        draw.line([(x + 69, y + 16), (x + 85, y + 16)], fill=(245, 235, 200), width=2)
        draw.ellipse([x + 108, y + 12, x + 120, y + 24], fill=RED)
        draw.rectangle([x + 8, y + 6, x + 44, y + 22], fill=(22, 34, 48))
    elif idx == 6:  # Las Vegas GP
        draw.rectangle([x, y, x + w, y + h], fill=(16, 18, 34))
        for nx, col in [(18, (235, 55, 145)), (48, (55, 210, 235)), (95, (245, 195, 50)), (128, (235, 55, 145))]:
            draw.rectangle([x + nx, y + 6, x + nx + 10, y + 24], fill=col)
        draw.rectangle([x, y + 25, x + w, y + h], fill=(52, 54, 60))
        draw.line([(x, y + 26), (x + w, y + 26)], fill=RED, width=2)
        draw.polygon([(x + 42, y + 36), (x + 114, y + 36), (x + 126, y + 32), (x + 40, y + 30)], fill=(24, 65, 155))
        draw.ellipse([x + 48, y + 30, x + 60, y + 39], fill=(15, 15, 15))
        draw.ellipse([x + 98, y + 30, x + 110, y + 39], fill=(15, 15, 15))
    elif idx == 7:  # Wembanyama 50 pts
        draw.rectangle([x, y, x + w, y + h], fill=(42, 34, 46))
        draw.rectangle([x, y + h - 14, x + w, y + h], fill=(205, 158, 92))
        draw.rectangle([x + 110, y + 6, x + 138, y + 24], fill=(245, 245, 245), outline=RED, width=2)
        draw.ellipse([x + 100, y + 22, x + 116, y + 28], outline=(235, 110, 40), width=2)
        draw.rectangle([x + 62, y + 18, x + 70, y + 38], fill=(22, 22, 26))
        draw.ellipse([x + 62, y + 10, x + 70, y + 18], fill=(22, 22, 26))
        draw.line([(x + 70, y + 22), (x + 88, y + 12)], fill=(22, 22, 26), width=3)
        draw.ellipse([x + 86, y + 6, x + 97, y + 17], fill=(228, 112, 34))
    elif idx == 8:  # Indonesia factory fire
        draw.rectangle([x, y, x + w, y + h], fill=(64, 68, 76))
        for cx, cr in [(48, 12), (66, 14), (86, 11)]:
            draw.ellipse([x + cx, y + 2, x + cx + cr, y + 2 + cr], fill=(38, 40, 44))
        draw.polygon([(x + 24, y + h), (x + 24, y + 22), (x + 56, y + 14), (x + 88, y + 22), (x + 128, y + 22), (x + 128, y + h)], fill=(116, 108, 100))
        draw.polygon([(x + 48, y + h), (x + 64, y + 14), (x + 82, y + h)], fill=(238, 96, 32))
        draw.polygon([(x + 56, y + h), (x + 65, y + 22), (x + 75, y + h)], fill=(252, 200, 64))
    elif idx == 9:  # Sparta II ship
        draw.rectangle([x, y, x + w, y + h], fill=(166, 188, 204))
        draw.rectangle([x, y + 26, x + w, y + h], fill=(42, 86, 122))
        draw.polygon([(x + 22, y + 20), (x + 100, y + 22), (x + 92, y + 34), (x + 28, y + 32)], fill=(120, 46, 46))
        draw.rectangle([x + 32, y + 10, x + 48, y + 21], fill=(235, 235, 232))
        draw.line([(x + 100, y + 26), (x + 126, y + 28)], fill=(40, 40, 40), width=1)
        draw.polygon([(x + 124, y + 24), (x + 150, y + 24), (x + 146, y + 33), (x + 128, y + 33)], fill=(215, 115, 45))
        draw.rectangle([x + 132, y + 16, x + 142, y + 24], fill=(245, 245, 245))
    elif idx == 10:  # Iran power cuts
        draw.rectangle([x, y, x + w, y + h], fill=(26, 30, 48))
        for bx, bh, lit in [(12, 28, True), (36, 36, True), (62, 22, True), (94, 34, False), (120, 26, False), (146, 32, False)]:
            draw.rectangle([x + bx, y + h - bh, x + bx + 20, y + h], fill=(56, 60, 74) if lit else (16, 18, 28))
            if lit:
                draw.rectangle([x + bx + 4, y + h - bh + 5, x + bx + 9, y + h - bh + 10], fill=(248, 212, 84))
                draw.rectangle([x + bx + 12, y + h - bh + 13, x + bx + 17, y + h - bh + 18], fill=(248, 212, 84))
        draw.polygon([(x + 88, y + 4), (x + 98, y + 4), (x + 92, y + 16), (x + 102, y + 16), (x + 86, y + 34), (x + 91, y + 20), (x + 82, y + 20)], fill=(250, 200, 45))
        draw.line([(x + 80, y + 6), (x + 104, y + 30)], fill=RED, width=3)
    elif idx == 11:  # Bolsonaro ICU
        draw.rectangle([x, y, x + w, y + h], fill=(228, 232, 236))
        draw.rectangle([x + 16, y + 6, x + 84, y + h - 4], fill=(248, 248, 248), outline=(140, 145, 152))
        draw.rectangle([x + 44, y + 11, x + 56, y + 33], fill=RED)
        draw.rectangle([x + 39, y + 16, x + 61, y + 28], fill=RED)
        draw.rectangle([x + 96, y + 8, x + 174, y + h - 6], fill=(18, 32, 28))
        draw.line([(x + 102, y + 22), (x + 122, y + 22), (x + 128, y + 12), (x + 134, y + 32), (x + 140, y + 22), (x + 168, y + 22)], fill=(72, 232, 130), width=2)
    elif idx == 12:  # BepiColombo
        draw.rectangle([x, y, x + w, y + h], fill=(12, 18, 38))
        for sx, sy in [(20, 10), (48, 32), (82, 8), (115, 28), (168, 12)]:
            draw.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2], fill=WHITE)
        draw.ellipse([x + 128, y + 4, x + 162, y + 38], fill=(142, 136, 128))
        draw.ellipse([x + 136, y + 12, x + 144, y + 20], fill=(108, 102, 95))
        draw.ellipse([x + 148, y + 22, x + 154, y + 28], fill=(116, 110, 102))
        draw.rectangle([x + 58, y + 15, x + 76, y + 27], fill=(222, 180, 62))
        draw.rectangle([x + 30, y + 18, x + 58, y + 24], fill=(48, 110, 198))
        draw.rectangle([x + 76, y + 18, x + 104, y + 24], fill=(48, 110, 198))
    elif idx == 13:  # Pope Leo XIV lunch
        draw.rectangle([x, y, x + w, y + h], fill=(214, 198, 170))
        draw.chord([x + 28, y + 4, x + 82, y + 40], 180, 360, fill=(238, 228, 206))
        draw.chord([x + 98, y + 4, x + 152, y + 40], 180, 360, fill=(238, 228, 206))
        draw.rectangle([x + 20, y + 28, x + w - 20, y + h - 4], fill=(248, 248, 244), outline=(145, 132, 112))
        draw.ellipse([x + 84, y + 10, x + 96, y + 22], fill=(240, 212, 186))
        draw.polygon([(x + 76, y + 28), (x + 104, y + 28), (x + 98, y + 20), (x + 82, y + 20)], fill=WHITE)
        draw.polygon([(x + 86, y + 11), (x + 94, y + 11), (x + 90, y + 3)], fill=WHITE)
        for px in [36, 56, 122, 144]:
            draw.ellipse([x + px, y + 22, x + px + 8, y + 27], fill=(195, 172, 140))
    elif idx == 14:  # FBI NCIC cyber
        draw.rectangle([x, y, x + w, y + h], fill=(20, 28, 36))
        for ly, lw in [(10, 62), (18, 48), (26, 74), (34, 40)]:
            draw.rectangle([x + 14, y + ly, x + 14 + lw, y + ly + 4], fill=(54, 186, 108))
        draw.polygon([(x + 120, y + 8), (x + 150, y + 36), (x + 90, y + 36)], fill=RED)
        draw.rectangle([x + 118, y + 17, x + 122, y + 26], fill=WHITE)
        draw.rectangle([x + 118, y + 29, x + 122, y + 33], fill=WHITE)
        draw.rectangle([x + 156, y + 20, x + 176, y + 36], fill=(224, 186, 68))
        draw.arc([x + 159, y + 10, x + 173, y + 26], 180, 360, fill=(224, 186, 68), width=3)


def draw_world_map(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(214, 228, 238), outline=DARK_RULE, width=1)
    land = (196, 188, 158)
    coast = (130, 124, 102)

    def poly(pts):
        abs_pts = [(x + int(px * w), y + int(py * h)) for px, py in pts]
        draw.polygon(abs_pts, fill=land, outline=coast)

    poly([(0.06, 0.14), (0.30, 0.12), (0.33, 0.28), (0.24, 0.44), (0.18, 0.48), (0.12, 0.36)])
    poly([(0.23, 0.50), (0.34, 0.54), (0.36, 0.72), (0.28, 0.90), (0.24, 0.76)])
    poly([(0.44, 0.14), (0.60, 0.12), (0.58, 0.34), (0.45, 0.36), (0.43, 0.25)])
    poly([(0.44, 0.38), (0.59, 0.38), (0.62, 0.58), (0.54, 0.82), (0.47, 0.64), (0.42, 0.50)])
    poly([(0.59, 0.14), (0.90, 0.16), (0.92, 0.44), (0.78, 0.56), (0.66, 0.50), (0.59, 0.38)])
    poly([(0.78, 0.66), (0.91, 0.66), (0.92, 0.82), (0.79, 0.82)])
    poly([(0.94, 0.78), (0.97, 0.76), (0.96, 0.88), (0.93, 0.86)])

    dots = [
        (1, 0.55, 0.22),
        (2, 0.57, 0.33),
        (3, 0.63, 0.42),
        (4, 0.83, 0.43),
        (5, 0.95, 0.82),
        (6, 0.13, 0.31),
        (7, 0.18, 0.38),
        (8, 0.80, 0.58),
        (9, 0.53, 0.14),
        (10, 0.65, 0.36),
        (11, 0.31, 0.64),
        (12, 0.48, 0.28),
        (13, 0.50, 0.32),
        (14, 0.22, 0.26),
        (15, 0.52, 0.41),
        (16, 0.46, 0.22),
        (17, 0.75, 0.42),
        (18, 0.26, 0.33),
        (19, 0.54, 0.27),
        (20, 0.71, 0.42),
        (21, 0.69, 0.48),
        (22, 0.71, 0.37),
        (23, 0.60, 0.56),
        (24, 0.59, 0.30),
    ]
    f_dot = load_font(FONT_SANS_B, 8)
    for num, rx, ry in dots:
        dx = x + int(rx * w)
        dy = y + int(ry * h)
        r = 6 if num in (1, 2, 3) else 5
        draw.ellipse([dx - r, dy - r, dx + r, dy + r], fill=RED, outline=WHITE)
        lbl = str(num)
        tw, th = text_size(draw, lbl, f_dot)
        draw.text((dx - tw // 2, dy - th // 2 - 1), lbl, font=f_dot, fill=WHITE)


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_CREAM)
    draw = ImageDraw.Draw(img)

    f_strip_b = load_font(FONT_SANS_B, 10)
    f_strip = load_font(FONT_SANS, 10)
    f_masthead = load_font(FONT_SERIF_B, 38)
    f_standfirst = load_font(FONT_SERIF, 13)
    f_fig_num = load_font(FONT_SERIF_B, 20)
    f_fig_cap = load_font(FONT_SANS, 10)
    f_reg = load_font(FONT_SANS_B, 10)
    f_time_b = load_font(FONT_SANS_B, 10)
    f_time = load_font(FONT_SANS, 10)

    f_lead_tag = load_font(FONT_SANS_B, 10)
    f_lead_num = load_font(FONT_SERIF_B, 13)
    f_lead_head = load_font(FONT_SERIF_B, 14)
    f_lead_body = load_font(FONT_SERIF, 11)
    f_lead_src = load_font(FONT_SANS, 10)

    f_med_tag = load_font(FONT_SANS_B, 9)
    f_med_head = load_font(FONT_SERIF_B, 11)
    f_med_body = load_font(FONT_SANS, 11)
    f_med_src = load_font(FONT_SANS, 9)

    f_sec_hdr = load_font(FONT_SANS_B, 11)
    f_also = load_font(FONT_SANS, 11)
    f_box_hdr = load_font(FONT_SANS_B, 11)
    f_box_txt = load_font(FONT_SANS, 10)

    # 1. Top strip (y = 0..22)
    draw.rectangle([0, 0, WIDTH, 22], fill=NAVY)
    draw.text((MARGIN, 5), "THE WORLD DISPATCH", font=f_strip_b, fill=WHITE)
    right_txt = "24 VERIFIED STORIES  ·  7 REGIONS  ·  ALL DATED SUNDAY 22 NOVEMBER 2026"
    rw, _ = text_size(draw, right_txt, f_strip)
    draw.text((WIDTH - MARGIN - rw, 5), right_txt, font=f_strip, fill=OFF_WHITE)

    # 2. Masthead (y = 24..64)
    mast = "Sunday 22 November 2026"
    mw, _ = text_size(draw, mast, f_masthead)
    draw.text(((WIDTH - mw) // 2, 23), mast, font=f_masthead, fill=INK)
    draw.line([(MARGIN, 66), (WIDTH - MARGIN, 66)], fill=DARK_RULE, width=2)

    # 3. Standfirst (y = 68..86)
    stand = "186 drones fired at Ukraine  ·  COP31 ends with no deal  ·  Iran claims two US radars hit"
    sw, _ = text_size(draw, stand, f_standfirst)
    draw.text(((WIDTH - sw) // 2, 69), stand, font=f_standfirst, fill=RED)
    draw.line([(MARGIN, 88), (WIDTH - MARGIN, 88)], fill=RULE, width=1)

    # 4. Figures strip (y = 90..136)
    figures = [
        ("186", "drones fired at", "Ukraine overnight"),
        ("161", "downed or suppressed", "by air defence"),
        ("35%", "electricity by 2035,", "COP31 surviving goal"),
        ("$120bn", "adaptation target", "dropped from COP31"),
        ("720/9", "India record Test", "total in New Zealand"),
        ("50", "Wembanyama points", "in one NBA game"),
    ]
    col_w = CONTENT_W // 6
    for i, (num, c1, c2) in enumerate(figures):
        cx = MARGIN + i * col_w
        if i > 0:
            draw.line([(cx, 92), (cx, 134)], fill=RULE, width=1)
        nw, _ = text_size(draw, num, f_fig_num)
        draw.text((cx + (col_w - nw) // 2, 90), num, font=f_fig_num, fill=RED)
        c1w, _ = text_size(draw, c1, f_fig_cap)
        c2w, _ = text_size(draw, c2, f_fig_cap)
        draw.text((cx + (col_w - c1w) // 2, 113), c1, font=f_fig_cap, fill=INK)
        draw.text((cx + (col_w - c2w) // 2, 124), c2, font=f_fig_cap, fill=INK)
    draw.line([(MARGIN, 138), (WIDTH - MARGIN, 138)], fill=RULE, width=1)

    # 5. Region bar (y = 141..161)
    regions = [
        ("Europe 5", 200, (44, 86, 136)),
        ("Middle East 3", 120, (166, 78, 42)),
        ("Asia-Pacific 6", 236, (48, 118, 92)),
        ("Americas 4", 145, (124, 68, 126)),
        ("Africa 1", 68, (182, 126, 36)),
        ("Oceania 1", 74, (38, 122, 140)),
        ("World 4", 145, (74, 82, 94)),
    ]
    rx = MARGIN
    for label, rw_px, col in regions:
        draw.rectangle([rx, 141, rx + rw_px - 1, 161], fill=col)
        lw, lh = text_size(draw, label, f_reg)
        draw.text((rx + (rw_px - lw) // 2, 141 + (20 - lh) // 2 - 1), label, font=f_reg, fill=WHITE)
        rx += rw_px

    # 6. UTC Timeline strip (y = 164..196)
    draw.rectangle([MARGIN, 164, WIDTH - MARGIN, 196], fill=DARK_SLATE)
    timeline = [
        ("02:00 Antalya local", "COP31 releases final text"),
        ("03:00 GMT", "COP31 text objection deadline"),
        ("08:07 UTC", "Ukraine: 186 drones, 161 hit"),
        ("11:00 Hong Kong time", "HK turnout passes 68%"),
        ("15:56 UTC", "Manipur liquor toll at 17"),
    ]
    tw_col = CONTENT_W // 5
    for i, (t_lbl, ev) in enumerate(timeline):
        tx = MARGIN + i * tw_col + 8
        if i > 0:
            draw.line([(MARGIN + i * tw_col, 168), (MARGIN + i * tw_col, 192)], fill=(70, 90, 110), width=1)
        draw.ellipse([tx, 170, tx + 5, 175], fill=GOLD)
        draw.text((tx + 9, 166), t_lbl, font=f_time_b, fill=GOLD)
        draw.text((tx + 9, 180), ev, font=f_time, fill=OFF_WHITE)

    # 7. Three large lead stories (y = 202..424)
    leads = [
        {
            "num": "1",
            "kind": "ukraine",
            "loc": "EUROPE / WAR",
            "tag": "REPORTED",
            "head": "Russia fires 186 drones at Ukraine overnight; 161 downed",
            "body": "A five-storey block in Dymer, Kyiv region, is destroyed; two dead on the day, 14 unaccounted for, nine evacuated. Strikes hit 18 locations.",
            "src": "Sources: Ukrainian Air Force, Reuters, AP",
        },
        {
            "num": "2",
            "kind": "cop31",
            "loc": "WORLD / CLIMATE",
            "tag": "REPORTED",
            "head": "COP31 ends with no deal after dawn text",
            "body": "Final Antalya text drops the $120bn adaptation target, names no fossil fuels, keeps a 35% by 2035 power goal and admits 1.5C overshoot. EU, UK, Norway, Panama and islands reject it; COP32 in Addis Ababa Nov 2027.",
            "src": "Sources: Reuters, Al Jazeera, diplomacy.edu",
        },
        {
            "num": "3",
            "kind": "bahrain",
            "loc": "MIDDLE EAST / WAR",
            "tag": "CLAIM",
            "head": "Iran claims two US radars hit; Bahrain denies it",
            "body": "IRGC claims strikes hit Patriot radars at Al-Riffa and Awali in Bahrain. Bahrain says defences intercepted the attack; a Sitra Island facility fire injures two. US says no damage.",
            "src": "Sources: Sepah News/IRIB, Reuters, Bahrain Interior Ministry, CBS",
        },
    ]
    lead_gap = 14
    lead_w = (CONTENT_W - 2 * lead_gap) // 3
    for i, lead in enumerate(leads):
        lx = MARGIN + i * (lead_w + lead_gap)
        ly = 202
        draw_lead_illustration(draw, lead["kind"], lx, ly, lead_w, 84)
        ty = ly + 88
        draw.text((lx, ty - 1), lead["num"], font=f_lead_num, fill=RED)
        tag_str = lead["loc"] + "  ·  " + lead["tag"]
        tag_col = RED if lead["tag"] == "CLAIM" else NAVY
        draw.text((lx + 14, ty + 1), tag_str, font=f_lead_tag, fill=tag_col)
        cy = ty + 16
        cy = draw_wrapped(draw, lx, cy, lead["head"], f_lead_head, INK, lead_w, 16, max_lines=2)
        cy += 2
        cy = draw_wrapped(draw, lx, cy, lead["body"], f_lead_body, INK, lead_w, 13, max_lines=5)
        draw_wrapped(draw, lx, 412, lead["src"], f_lead_src, MUTED, lead_w, 11, max_lines=1)

    draw.line([(MARGIN, 427), (WIDTH - MARGIN, 427)], fill=DARK_RULE, width=1)

    # 8. Two rows of smaller illustrated stories (stories 4..14)
    row1 = [
        (4, "ASIA-PAC / ELECT", "REPORTED", "HK Election Committee vote",
         "856 candidates contest 723 seats; record 98.79% turnout (5,640).", "HK gov, China Daily"),
        (5, "OCEANIA / CRICKET", "REPORTED", "India 720/9 in Wellington",
         "Highest NZ Test total: Rahul 136, Pant 128, Gill 98; NZ 119/2.", "AP, Cricinfo"),
        (6, "AMERICAS / SPORT", "REPORTED", "Verstappen wins Vegas GP",
         "Verstappen tops Norris and Piastri; Russell hits wall, ninth.", "wires"),
        (7, "AMERICAS / SPORT", "REPORTED", "Wembanyama scores 50",
         "50 pts, 19 reb, 5 blk, 4 stl as San Antonio win 114-91.", "AP, ESPN"),
        (8, "ASIA-PAC / DISAST", "REPORTED", "Indonesia factory fire toll",
         "Milkita plant in Cikande: 3 dead Sunday, 36 missing, 15 saved.", "Reuters, AP, SAR"),
        (9, "EUROPE / SEA", "REPORTED", "Sparta II towed out",
         "Struck Sat; 16 rescued; fire out Sunday, no leak, towed out.", "Reuters, BBC"),
    ]
    r1_gap = 10
    r1_w = (CONTENT_W - 5 * r1_gap) // 6
    for i, (num, loc, tag, head, body, src) in enumerate(row1):
        mx = MARGIN + i * (r1_w + r1_gap)
        my = 432
        draw_med_illustration(draw, num, mx, my, r1_w, 40)
        draw.text((mx, my + 43), str(num) + " " + loc + " · " + tag, font=f_med_tag, fill=NAVY)
        cy = draw_wrapped(draw, mx, my + 55, head, f_med_head, INK, r1_w, 13, max_lines=2)
        draw_wrapped(draw, mx, cy + 2, body, f_med_body, INK, r1_w, 12, max_lines=3)
        draw.text((mx, 560), src, font=f_med_src, fill=MUTED)

    draw.line([(MARGIN, 574), (WIDTH - MARGIN, 574)], fill=RULE, width=1)

    row2 = [
        (10, "M.EAST / ENERGY", "REPORTED", "Iran starts rolling power cuts",
         "Up to 2 hrs every 2 days after gas strikes; Pezeshkian warns of winter.", "RFE/RL, Reuters, Tavanir"),
        (11, "AMERICAS / HEALTH", "REPORTED", "Bolsonaro stays in ICU",
         "Clinically stable in Brasilia with bowel obstruction, no discharge.", "DF Star, Reuters"),
        (12, "WORLD / SPACE", "REPORTED", "BepiColombo reaches Mercury",
         "ESA reports software thruster glitch; safe, orbiters split 9-10 Dec.", "Reuters, ESA"),
        (13, "EUROPE / FAITH", "REPORTED", "Pope feeds 1,300 poor",
         "World Day of the Poor lunch in Paul VI Hall: we are all one family.", "Vatican News, EWTN"),
        (14, "AMERICAS / CYBER", "REPORTED", "FBI probes NCIC breach",
         "Reported Friday; Sunday WA pauses gun-dealer background checks.", "CNN, AP, WSP"),
    ]
    r2_gap = 12
    r2_w = (CONTENT_W - 4 * r2_gap) // 5
    for i, (num, loc, tag, head, body, src) in enumerate(row2):
        mx = MARGIN + i * (r2_w + r2_gap)
        my = 579
        draw_med_illustration(draw, num, mx, my, r2_w, 40)
        draw.text((mx, my + 43), str(num) + " " + loc + " · " + tag, font=f_med_tag, fill=NAVY)
        cy = draw_wrapped(draw, mx, my + 55, head, f_med_head, INK, r2_w, 13, max_lines=2)
        draw_wrapped(draw, mx, cy + 2, body, f_med_body, INK, r2_w, 12, max_lines=3)
        draw.text((mx, 706), src, font=f_med_src, fill=MUTED)

    draw.line([(MARGIN, 720), (WIDTH - MARGIN, 720)], fill=DARK_RULE, width=1)

    # 9 & 10. Also on Sunday (left 624px) + World Map (right 350px)
    also_w = 624
    map_x = MARGIN + also_w + 14
    map_w = WIDTH - MARGIN - map_x

    draw.text((MARGIN, 725), "ALSO ON SUNDAY 22 NOVEMBER", font=f_sec_hdr, fill=NAVY)
    also_items = [
        ("15.", "AFRICA/WAR · REPORTED", "Benghazi blast hits Russian corvette; sea-drone hits ship; UN seeks probe (wires)"),
        ("16.", "EUROPE/TRAVEL · FORECAST", "Belgian ATC join Mon strike; 429 Brussels flights, 59,500 flyers hit (skeyes)"),
        ("17.", "ASIA-PAC/HEALTH · REPORTED", "Manipur liquor toll 17 (16 Chandel, 1 Kakching); 228 hospital, 6 held (gov)"),
        ("18.", "M.EAST/DIPL · REPORTED", "Trump wants permanent deal with Tehran in Fox News interview (RFE/RL)"),
        ("19.", "EUROPE/WAR · REPORTED", "Russian strikes hit Odesa grid; jet drone crosses Moldova twice (wires)"),
        ("20.", "ASIA-PAC/INDIA · REPORTED", "Four cheetah cubs are born at Kuno National Park (day roundup)"),
        ("21.", "ASIA-PAC/INDIA · REPORTED", "Indian Navy inducts diving support craft DSC A21 in Mumbai (roundup)"),
        ("22.", "ASIA-PAC/INDIA · REPORTED", "First SCO Civilisational Dialogue Forum concludes in New Delhi (roundup)"),
        ("23.", "WORLD/ECONOMY · REPORTED", "BRICS sets a $300bn bioeconomy target for 2030 (day roundup)"),
        ("24.", "WORLD/CLIMATE · REPORTED", "More than 90 countries sign COP31 side electrification pledge (Reuters)"),
    ]
    ay = 741
    for num_s, tag_s, desc_s in also_items:
        draw.text((MARGIN, ay), num_s, font=f_strip_b, fill=RED)
        draw.text((MARGIN + 22, ay), tag_s + " — " + desc_s, font=f_also, fill=INK)
        ay += 15

    draw.text((map_x, 725), "WHERE IT HAPPENED (STORIES 1-24)", font=f_sec_hdr, fill=NAVY)
    draw_world_map(draw, map_x, 741, map_w, 152)

    # 11. Red-bordered Date Check box (y = 900..972)
    draw.rectangle([MARGIN, 900, WIDTH - MARGIN, 972], fill=(252, 248, 240), outline=RED, width=2)
    draw.text((MARGIN + 8, 904), "DATE CHECK — EVERY STORY IS FROM SUNDAY 22 NOVEMBER 2026. LEFT OUT ON PURPOSE:", font=f_box_hdr, fill=RED)
    dc_line1 = (
        "All 24 stories occurred on, or were first reported on, Sun 22 Nov 2026. Excluded earlier items: "
        "Russia 400-drone/110-missile barrage (Thu 19-Fri 20 Nov); El Chapo Isidro captured in Sinaloa, 11 dead (Fri 20-Sat 21 Nov);"
    )
    dc_line2 = (
        "Peru quake (Fri 20 Nov); Kryvyi Rih missile strike (Sat 21 Nov); Sparta II struck Sat 21 Nov "
        "(Sunday news: fire out, tow-out, no leak); Cikande fire started Sat 21 Nov 5pm (Sunday news: toll & search); "
        "NCIC breach first reported Fri 20 Nov (Sunday news: WA check pause)."
    )
    cy = draw_wrapped(draw, MARGIN + 8, 919, dc_line1, f_box_txt, INK, CONTENT_W - 16, 12, max_lines=2)
    draw_wrapped(draw, MARGIN + 8, cy + 1, dc_line2, f_box_txt, INK, CONTENT_W - 16, 12, max_lines=2)

    # 12. Sources line & Certainty legend (y = 975..1000)
    src_line = "SOURCES: Reuters, AP, AFP, Al Jazeera, BBC, The Guardian, Ukrainian Air Force, Hong Kong government, DF Star hospital, ESA, Vatican News."
    leg_line = "CERTAINTY TAGS: REPORTED = confirmed by wires; CLAIM = one side account, unconfirmed; FORECAST = still to happen when drawn; PENDING = not settled yet."
    draw.text((MARGIN, 976), src_line, font=f_box_txt, fill=MUTED)
    draw.text((MARGIN, 988), leg_line, font=f_box_txt, fill=INK)

    # 13. Bottom strip (y = 1004..1024)
    draw.rectangle([0, 1004, WIDTH, HEIGHT], fill=NAVY)
    draw.text((MARGIN, 1009), "THE WORLD DISPATCH", font=f_strip_b, fill=WHITE)
    bot_r = "SUNDAY 22 NOVEMBER 2026  ·  ONE PAGE"
    bw, _ = text_size(draw, bot_r, f_strip)
    draw.text((WIDTH - MARGIN - bw, 1009), bot_r, font=f_strip, fill=OFF_WHITE)

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
