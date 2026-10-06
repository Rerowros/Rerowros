"""Renders the static profile SVGs (dark + light) into assets/. Run: python scripts/render_assets.py"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "Geist,Inter,-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "'Geist Mono',ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# Monochrome, Vercel-like: one ink colour, greys for everything else, red/green only where they carry meaning.
THEMES = {
    "dark": dict(card="#0a0a0a", panel="#111111", border="#2e2e2e", text="#ededed", muted="#a1a1a1",
                 faint="#707070", grid="#1c1c1c", weak="#3d3d3d", ok="#4cc38a", bad="#ff6369"),
    "light": dict(card="#ffffff", panel="#fafafa", border="#e5e5e5", text="#171717", muted="#5c5c5c",
                  faint="#8f8f8f", grid="#f0f0f0", weak="#d4d4d4", ok="#18794e", bad="#cd2b31"),
}
HAIR = 1.4  # ~1 px once GitHub scales a 1200-wide image down to the README column


def t(x, y, s, size=16, fill=None, weight=400, anchor="start", font=SANS, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def kick(x, y, s, c, anchor="start", fill=None):
    return t(x, y, s.upper(), 14, fill or c["faint"], 500, anchor, MONO, 'letter-spacing="1.2"')


def svg(w, h, body, title, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            f'<defs>{defs}</defs>{body}</svg>\n')


def frame(w, h, c):
    return (f'<rect x="{HAIR / 2}" y="{HAIR / 2}" width="{w - HAIR}" height="{h - HAIR}" rx="14" '
            f'fill="{c["card"]}" stroke="{c["border"]}" stroke-width="{HAIR}"/>')


def hline(x1, x2, y, c, color=None):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color or c["border"]}" stroke-width="{HAIR}"/>'


def vline(x, y1, y2, c, color=None):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color or c["border"]}" stroke-width="{HAIR}"/>'


def title_block(c, title, subtitle):
    return t(40, 58, title, 28, c["text"], 600, extra='letter-spacing="-0.6"') + t(40, 88, subtitle, 17, c["muted"])


# ---------------------------------------------------------------- header
def header(c):
    W, H = 1200, 270
    defs = (f'<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">'
            f'<path d="M48,0 V48 M0,48 H48" fill="none" stroke="{c["grid"]}" stroke-width="{HAIR}"/></pattern>'
            '<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity="1"/>'
            '</linearGradient><mask id="m"><rect width="1200" height="270" fill="url(#fade)"/></mask>')
    b = [frame(W, H, c), f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#grid)" mask="url(#m)"/>']
    b.append(kick(56, 70, "Rerowros", c))
    b.append(t(54, 136, "Iaroslav", 64, c["text"], 600, extra='letter-spacing="-2.4"'))
    b.append(t(56, 182, "I build BPN — a VPN service with its own Android and", 20, c["muted"]))
    b.append(t(56, 210, "Windows apps and a patched mihomo core under them.", 20, c["muted"]))

    x0, x1, y = 700, 1144, 56
    rows = [("focus", "VPN clients, proxy cores, networking"), ("languages", "Rust · Kotlin · Go · Python · TypeScript"),
            ("shipping", "Android · Windows · Telegram bot"), ("based in", "Georgia · UTC+4")]
    b.append(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{len(rows) * 40}" rx="10" fill="{c["card"]}" '
             f'stroke="{c["border"]}" stroke-width="{HAIR}"/>')
    for i, (k, v) in enumerate(rows):
        yy = y + i * 40
        if i:
            b.append(hline(x0, x1, yy, c))
        b.append(t(x0 + 20, yy + 26, k, 14, c["faint"], 500, font=MONO))
        b.append(t(x0 + 128, yy + 26, v, 15, c["text"], 500))
    return svg(W, H, "".join(b), "Iaroslav · Rerowros — I build BPN, a VPN service with Android and Windows apps", defs)


# ---------------------------------------------------------------- glyphs
def glyph(kind, c, sw=3):
    """Line icons drawn around (0, 0), roughly 56 px across."""
    st = f'fill="none" stroke="{c["text"]}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'
    dot = c["text"]
    if kind == "phone":
        return f'<rect x="-14" y="-23" width="28" height="46" rx="6" {st}/><line x1="-4" y1="15" x2="4" y2="15" {st}/>'
    if kind == "laptop":
        return f'<rect x="-22" y="-17" width="44" height="28" rx="3" {st}/><line x1="-28" y1="18" x2="28" y2="18" {st}/>'
    if kind == "stack":
        return "".join(f'<rect x="-22" y="{-22 + k * 16}" width="44" height="11" rx="3" {st}/>'
                       f'<circle cx="13" cy="{-16.5 + k * 16}" r="1.6" fill="{dot}"/>' for k in range(3))
    if kind == "fork":
        return (f'<circle cx="-12" cy="-17" r="5" {st}/><circle cx="-12" cy="17" r="5" {st}/><circle cx="13" cy="-17" r="5" {st}/>'
                f'<line x1="-12" y1="-12" x2="-12" y2="12" {st}/><path d="M13,-12 C13,2 -12,-2 -12,10" {st}/>')
    if kind == "pr":
        return (f'<circle cx="-13" cy="-17" r="5" {st}/><circle cx="-13" cy="17" r="5" {st}/><circle cx="13" cy="17" r="5" {st}/>'
                f'<line x1="-13" y1="-12" x2="-13" y2="12" {st}/><path d="M13,12 V-8 Q13,-17 4,-17 H-2" {st}/>'
                f'<path d="M3,-23 L-3,-17 L3,-11" {st}/>')
    if kind == "chat":
        return (f'<path d="M-22,-16 H22 V10 H-6 L-16,20 V10 H-22 Z" {st}/>'
                + "".join(f'<circle cx="{dx}" cy="-3" r="2.4" fill="{dot}"/>' for dx in (-10, 0, 10)))
    if kind == "panel":
        return (f'<rect x="-24" y="-20" width="48" height="40" rx="5" {st}/><line x1="-24" y1="-9" x2="24" y2="-9" {st}/>'
                f'<line x1="-13" y1="12" x2="-13" y2="4" {st}/><line x1="0" y1="12" x2="0" y2="-1" {st}/>'
                f'<line x1="13" y1="12" x2="13" y2="7" {st}/>')
    if kind == "globe":
        return (f'<circle cx="0" cy="0" r="18" {st}/><ellipse cx="0" cy="0" rx="8" ry="18" {st}/>'
                f'<line x1="-18" y1="0" x2="18" y2="0" {st}/>')
    raise ValueError(kind)


# ---------------------------------------------------------------- section banners
def banner(kind, kicker, title, subtitle, stats, c, link=True):
    W, H = 1200, 136
    b = [frame(W, H, c)]
    b.append(f'<rect x="32" y="32" width="72" height="72" rx="14" fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="{HAIR}"/>')
    b.append(f'<g transform="translate(68 68) scale(.62)">{glyph(kind, c, 2.6)}</g>')
    b.append(kick(132, 46, kicker, c))
    b.append(t(130, 84, title, 30, c["text"], 600, extra='letter-spacing="-0.6"'))
    b.append(t(132, 112, subtitle, 18, c["muted"]))
    b.append(vline(690, 0, H, c))
    for k, (num, lab) in enumerate(stats):
        x = 690 + k * 170
        if k:
            b.append(vline(x, 0, H, c))
        b.append(t(x + 24, 66, num, 30 if len(num) <= 6 else 26, c["text"], 600, extra='letter-spacing="-0.6"'))
        for j, line in enumerate(lab.split("\n")):
            b.append(t(x + 24, 92 + j * 20, line, 15, c["muted"]))
    if link:
        b.append(t(1176, 30, "↗", 16, c["faint"], 500, "end", MONO))
    return svg(W, H, "".join(b), f"{title} — {subtitle}")


BANNERS = {
    "android": ("phone", {
        "en": ("Android app", "BadVPN for Android", "VPN client on my mihomo fork, Android 6+",
               [("0.85 s", "tap → first\nrequest via VPN"), ("0.2 s", "cold start\nto home screen"),
                ("1 key", "every APK signed,\nSHA-256 published")]),
        "ru": ("Android-приложение", "BadVPN для Android", "VPN-клиент на моём форке mihomo",
               [("0.85 с", "от нажатия до\nпервого запроса"), ("0.2 с", "холодный старт\nдо главной"),
                ("1 ключ", "все APK подписаны,\nSHA-256 в релизе")]),
    }),
    "windows": ("laptop", {
        "en": ("Windows app", "BPN for Windows", "Tauri UI + privileged Rust service",
               [("25k", "lines of Rust"), ("158", "tests"), ("3", "components\nchecked by hash")]),
        "ru": ("Приложение для Windows", "BPN для Windows", "Tauri + привилегированный сервис на Rust",
               [("25k", "строк Rust"), ("158", "тестов"), ("3", "компонента\nсверяются по хешу")]),
    }),
    "product": ("stack", {
        "en": ("The product · private", "BPN / BadVPN", "Bot, backend, panel, nodes, two apps",
               [("~190k", "lines of code"), ("1.8k", "commits"), ("160+", "test files")]),
        "ru": ("Сам продукт · приватный", "BPN / BadVPN", "Бот, бэкенд, панель, ноды, два приложения",
               [("~190k", "строк кода"), ("1.8k", "коммитов"), ("160+", "тестовых файлов")]),
    }),
    "mihomo": ("fork", {
        "en": ("Proxy core · fork", "Rerowros/mihomo", "Upstream tag + 5 patches, rebased per release",
               [("×5–8", "faster XHTTP\nupload"), ("3 / 3", "Xray versions\nconnect"), ("5", "patches with\ninterop tests")]),
        "ru": ("Ядро · форк", "Rerowros/mihomo", "Тег upstream + 5 патчей, ребейз на релиз",
               [("×5–8", "быстрее отправка\nпо XHTTP"), ("3 / 3", "версии Xray\nподключаются"), ("5", "патчей с\ninterop-тестами")]),
    }),
    "clashfest": ("pr", {
        "en": ("Open source · core contributor", "Nemu-x/ClashFest", "Android client on mihomo · 222★",
               [("30", "merged PRs"), ("+19.6k", "lines"), ("~15%", "of the codebase")]),
        "ru": ("Open source · core contributor", "Nemu-x/ClashFest", "Android-клиент на mihomo · 222★",
               [("30", "смёрженных PR"), ("+19.6k", "строк"), ("~15%", "текущего кода")]),
    }),
    "tg-recall": ("chat", {
        "en": ("Project · Python · MCP", "tg-recall", "Local-first Telegram archive for AI agents",
               [("300+", "tests"), ("15k", "lines of Python"), ("2 OS", "CI on Windows\nand Linux")]),
        "ru": ("Проект · Python · MCP", "tg-recall", "Локальный архив Telegram для AI-агентов",
               [("300+", "тестов"), ("15k", "строк Python"), ("2 ОС", "CI на Windows\nи Linux")]),
    }),
    "pasarguard": ("panel", {
        "en": ("Open source · contributor", "PasarGuard", "VPN panel + node · 2.6k★",
               [("4", "merged PRs"), ("4", "in review"), ("3", "repos: panel,\nnode, scripts")]),
        "ru": ("Open source · контрибьютор", "PasarGuard", "VPN-панель + нода · 2.6k★",
               [("4", "смёржено"), ("4", "на ревью"), ("3", "репо: panel,\nnode, scripts")]),
    }),
}


# ---------------------------------------------------------------- architecture
def box(x, y, w, h, title, lines, c, hl=False, sub=None):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["panel"]}" '
           f'stroke="{c["text"] if hl else c["border"]}" stroke-width="{HAIR}"/>',
           t(x + 20, y + 36, title, 20, c["text"], 600, extra='letter-spacing="-0.3"')]
    yy = y + 60
    if sub:
        out.append(t(x + 20, yy, sub, 14, c["faint"], 500, font=MONO))
        yy += 28
    for ln in lines:
        indent = ln.startswith("  ")
        out.append(t(x + (34 if indent else 20), yy, ln.strip(), 16, c["faint"] if indent else c["muted"]))
        yy += 23
    return "".join(out)


def arrow_defs(c):
    return (f'<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c["faint"]}"/></marker>'
            f'<marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c["text"]}"/></marker>')


def label(x, y, s, c, anchor="middle"):
    return t(x, y, s, 13, c["faint"], 500, anchor, MONO)


def arrow(x1, y1, x2, y2, c, dashed=False, strong=False):
    dash = ' stroke-dasharray="5 5"' if dashed else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c["text"] if strong else c["faint"]}" '
            f'stroke-width="{HAIR + (0.6 if strong else 0)}"{dash} marker-end="url(#{"ahs" if strong else "ah"})"/>')


def architecture(c):
    W, H = 1200, 600
    b = [frame(W, H, c), title_block(c, "How BPN fits together", "Private code · ~190k lines · 1.8k commits")]
    b.append(box(40, 116, 290, 200, "Telegram bot · Mini App", [
        "sign-up, plans, payments", "support, referrals", "several brands, one backend"], c, sub="Python · aiogram"))
    b.append(box(410, 116, 400, 200, "Backend", [
        "• traffic ledger with rollover", "  shadow-validated, staged rollout",
        "• payments reconciled, not webhook-trusted", "• idempotent admin actions via outbox"], c,
        sub="Next.js · Prisma · PostgreSQL"))
    b.append(box(890, 116, 270, 200, "VPN panel", ["users, limits, traffic", "node configs, rollout"], c,
                 sub="Xray · REALITY · XHTTP"))
    b.append(arrow(330, 196, 406, 196, c) + label(368, 184, "orders", c))
    b.append(arrow(810, 196, 886, 196, c) + label(848, 184, "users", c))
    b.append(arrow(886, 240, 814, 240, c) + label(848, 262, "traffic", c))

    b.append(f'<path d="M470,316 V376 H185 V424" fill="none" stroke="{c["faint"]}" stroke-width="{HAIR}" '
             f'stroke-dasharray="5 5" marker-end="url(#ah)"/>')
    b.append(label(330, 368, "subscription link", c))
    b.append(f'<path d="M1025,316 V376 H525" fill="none" stroke="{c["faint"]}" stroke-width="{HAIR}" stroke-dasharray="5 5"/>')
    for x in (525, 795):
        b.append(arrow(x, 376, x, 424, c, dashed=True))
    b.append(label(1015, 368, "node configs", c, "end"))

    b.append(box(40, 428, 290, 140, "Clients", ["Windows · Tauri + Rust", "Android · Kotlin"], c, hl=True,
                 sub="core: mihomo, my fork"))
    b.append(box(410, 428, 230, 140, "Front node", ["entry point for mobile", "networks on whitelists"], c))
    b.append(box(680, 428, 230, 140, "Exit node", ["abroad, clean IP", "for the traffic"], c))
    b.append(f'<rect x="950" y="428" width="210" height="140" rx="10" fill="none" stroke="{c["border"]}" '
             f'stroke-width="{HAIR}" stroke-dasharray="4 5"/>')
    b.append(f'<g transform="translate(1055 480) scale(.8)">{glyph("globe", c, 2.4)}</g>')
    b.append(t(1055, 534, "Internet", 20, c["text"], 600, "middle"))
    for x1, x2 in ((330, 406), (640, 676), (910, 946)):
        b.append(arrow(x1, 498, x2, 498, c, strong=True))
    return svg(W, H, "".join(b), "How BPN fits together: Telegram bot, backend, VPN panel, clients, front and exit nodes",
               arrow_defs(c))


# ---------------------------------------------------------------- REALITY matrix
def reality(c):
    W, H = 1200, 400
    b = [frame(W, H, c), title_block(c, "REALITY that still connects to current Xray",
                                     "mihomo client ↔ real Xray REALITY server on 127.0.0.1 · VLESS over TCP · interop test in the fork")]
    cols = ["Xray 26.3.27", "Xray 26.7.28", "Xray 26.9.9"]
    cx0, cw, rh, top = 660, 170, 52, 128
    b.append(hline(40, 1160, top + 14, c))
    for i, col in enumerate(cols):
        b.append(t(cx0 + i * cw + cw / 2, top, col, 14, c["faint"], 500, "middle", MONO))
    rows = [("upstream mihomo · chrome", "", "ynn", False),
            ("upstream mihomo · firefox", "ML-KEM on", "ynn", False),
            ("upstream mihomo · no fingerprint", "", "nnn", False),
            ("my fork · chrome / firefox / safari", "ML-KEM on", "yyy", True)]
    for r, (name, note, res, hl) in enumerate(rows):
        y = top + 14 + r * rh
        if hl:
            b.append(f'<rect x="40" y="{y}" width="1120" height="{rh}" fill="{c["panel"]}"/>')
        b.append(t(56, y + 33, name, 17, c["text"], 600 if hl else 400))
        if note:
            b.append(t(410, y + 33, note, 13, c["faint"], 500, font=MONO))
        for i, ch in enumerate(res):
            ok = ch == "y"
            b.append(t(cx0 + i * cw + cw / 2, y + 33, "✓ connects" if ok else "✕ fails", 16,
                       c["ok"] if ok else c["bad"], 500, "middle"))
        b.append(hline(40, 1160, y + rh, c))
    b.append(t(40, 376, "Patches: current Xray client version in the session ID, Firefox 148 / Safari 26.3 uTLS "
                        "fingerprints, opt-in X25519MLKEM768", 14, c["faint"]))
    return svg(W, H, "".join(b), "REALITY compatibility: upstream mihomo vs my fork across Xray versions")


# ---------------------------------------------------------------- XHTTP upload chart
def xhttp(c):
    W, H = 1200, 470
    b = [frame(W, H, c), title_block(c, "Parallel XHTTP uploads: 5–8× faster upload",
                                     "Upload, Mbit/s · 150 ms RTT · mihomo ↔ real Xray 26.3.27 · packet-up, used for CDN-fronted lines")]
    b.append(f'<rect x="40" y="114" width="12" height="12" rx="2" fill="{c["weak"]}"/>')
    b.append(t(60, 125, "upstream: 1 request in flight", 14, c["muted"]))
    b.append(f'<rect x="300" y="114" width="12" height="12" rx="2" fill="{c["text"]}"/>')
    b.append(t(320, 125, "my fork: up to 8 in flight, Xray-style pipelining", 14, c["muted"]))
    x0, scale, top = 300, 50.0, 156
    for v in (0, 5, 10, 15):
        x = x0 + v * scale
        b.append(vline(x, top - 6, top + 4 * 64 - 8, c, c["grid"]))
        b.append(t(x, top + 4 * 64 + 12, str(v), 12, c["faint"], 500, "middle", MONO))
    rows = [("POST · HTTP/2", 2.3, 12.3), ("GET + headers · HTTP/2", 1.8, 12.9),
            ("POST · HTTP/1.1", 1.8, 13.8), ("GET + headers · HTTP/1.1", 2.4, 11.5)]
    for i, (name, a, n8) in enumerate(rows):
        y = top + i * 64
        b.append(t(x0 - 20, y + 25, name, 15, c["text"], 400, "end"))
        b.append(f'<rect x="{x0}" y="{y}" width="{a * scale:.1f}" height="16" rx="2" fill="{c["weak"]}"/>')
        b.append(t(x0 + a * scale + 8, y + 13, f"{a}", 13, c["faint"], 500, font=MONO))
        b.append(f'<rect x="{x0}" y="{y + 21}" width="{n8 * scale:.1f}" height="16" rx="2" fill="{c["text"]}"/>')
        b.append(t(x0 + n8 * scale + 8, y + 34, f"{n8}", 13, c["text"], 600, font=MONO))
        b.append(t(1160, y + 30, f"×{n8 / a:.1f}", 24, c["text"], 600, "end", extra='letter-spacing="-0.5"'))
    b.append(t(40, 448, "16 MiB transfers sha256-checked both ways on Xray 26.3.27, 26.7.28 and 26.9.9 · "
                        "upstream ceiling ≈ request size / RTT", 14, c["faint"]))
    return svg(W, H, "".join(b), "XHTTP packet-up upload throughput: upstream mihomo vs my fork")


# ---------------------------------------------------------------- Android: tap to first request
def android_connect(c):
    W, H = 1200, 400
    b = [frame(W, H, c), title_block(c, "Tap “connect” → first request through the VPN",
                                     "Seconds, lower is better · realme RMX8899, Android 16, Wi-Fi · measured over adb")]
    rows = [("BadVPN 1.1.5", 0.85, "median of 5", c["text"]), ("BadVPN 1.1.4", 1.35, "3 runs", c["muted"]),
            ("ClashFest", 1.56, "3 runs", c["weak"]), ("INCY 3.7.0", 1.56, "3 runs", c["weak"])]
    x0, scale, top = 260, 460.0, 124
    for v in (0, 0.5, 1.0, 1.5):
        x = x0 + v * scale
        b.append(vline(x, top - 6, top + 4 * 50, c, c["grid"]))
        b.append(t(x, top + 4 * 50 + 18, f"{v:g} s", 12, c["faint"], 500, "middle", MONO))
    for i, (name, v, note, fill) in enumerate(rows):
        y = top + i * 50
        b.append(t(x0 - 20, y + 23, name, 17, c["text"], 600 if i == 0 else 400, "end"))
        b.append(f'<rect x="{x0}" y="{y + 6}" width="{v * scale:.1f}" height="24" rx="2" fill="{fill}"/>')
        b.append(t(x0 + v * scale + 10, y + 24, f"{v:.2f} s", 15, c["text"] if i == 0 else c["muted"], 600, font=MONO))
        b.append(t(x0 + v * scale + 88, y + 24, note, 13, c["faint"], 500, font=MONO))
    b.append(t(40, 360, "1.1.4 vs ClashFest vs INCY: one rough session on 29.09.2026, 3 runs each, different exit servers.",
               14, c["faint"]))
    b.append(t(40, 382, "1.1.5 (no 500 ms wait, no second config pass): separate session, 5 runs vs 1.1.4 median 1.41 s.",
               14, c["faint"]))
    return svg(W, H, "".join(b), "Time from tap to first request through the VPN: BadVPN 1.1.5 0.85 s, ClashFest and INCY 1.56 s")


def main():
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.svg"):
        old.unlink()
    for name, fn in (("header", header), ("bpn-architecture", architecture), ("mihomo-reality", reality),
                     ("mihomo-xhttp", xhttp), ("android-connect", android_connect)):
        for theme, c in THEMES.items():
            (OUT / f"{name}-{theme}.svg").write_text(fn(c), encoding="utf-8")
    for name, (kind, langs) in BANNERS.items():
        for lang, args in langs.items():
            suffix = "" if lang == "en" else "-ru"
            for theme, c in THEMES.items():
                (OUT / f"banner-{name}{suffix}-{theme}.svg").write_text(
                    banner(kind, *args, c, link=name != "product"), encoding="utf-8")
    print(len(list(OUT.iterdir())), "files in", OUT)


if __name__ == "__main__":
    main()
