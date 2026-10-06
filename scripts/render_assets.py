"""Renders the static profile SVGs (dark + light) into assets/. Run: python scripts/render_assets.py

Everything is drawn at 880 px wide, the width of the profile README column, so text renders at its real size.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
W = 880

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# GitHub's own greys plus one calm accent; red/green only where they mean pass/fail.
THEMES = {
    "dark": dict(card="#0d1117", panel="#151b23", border="#30363d", text="#e6edf3", muted="#9198a1",
                 faint="#6e7681", grid="#21262d", weak="#3d444d", accent="#8c9bff", accent2="#4d5799",
                 ok="#3fb950", bad="#f85149"),
    "light": dict(card="#ffffff", panel="#f6f8fa", border="#d1d9e0", text="#1f2328", muted="#59636e",
                  faint="#818b98", grid="#eff2f5", weak="#d1d9e0", accent="#4c5bd4", accent2="#b4bcf0",
                  ok="#1a7f37", bad="#cf222e"),
}


def t(x, y, s, size=14, fill=None, weight=400, anchor="start", font=SANS, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def svg(w, h, body, title, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            f'<defs>{defs}</defs>{body}</svg>\n')


def frame(w, h, c):
    return f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="10" fill="{c["card"]}" stroke="{c["border"]}"/>'


def hline(x1, x2, y, c, color=None):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color or c["border"]}"/>'


def vline(x, y1, y2, c, color=None):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color or c["border"]}"/>'


def heading(c, title, subtitle):
    return t(20, 34, title, 18, c["text"], 600) + t(20, 56, subtitle, 13, c["muted"])


# ---------------------------------------------------------------- header
def header(c):
    H = 84
    b = [frame(W, H, c)]
    b.append(t(24, 46, "Rerowros", 28, c["text"], 600, extra='letter-spacing="-0.5"'))
    b.append(t(25, 68, "Iaroslav · software engineer", 13, c["muted"]))
    b.append(t(W - 24, 46, "Rust · Kotlin · Go · Python · TypeScript", 13, c["muted"], 400, "end", MONO))
    b.append(t(W - 24, 68, "Android · Windows · backend · tooling", 13, c["faint"], 400, "end", MONO))
    return svg(W, H, "".join(b), "Rerowros — Iaroslav, software engineer: Rust, Kotlin, Go, Python, TypeScript")


# ---------------------------------------------------------------- glyphs
def glyph(kind, c):
    """Line icons drawn around (0, 0), about 56 px across; callers scale them down."""
    st = f'fill="none" stroke="{c["accent"]}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"'
    dot = c["accent"]
    if kind == "phone":
        return f'<rect x="-14" y="-23" width="28" height="46" rx="6" {st}/><line x1="-4" y1="15" x2="4" y2="15" {st}/>'
    if kind == "laptop":
        return f'<rect x="-22" y="-17" width="44" height="28" rx="3" {st}/><line x1="-28" y1="18" x2="28" y2="18" {st}/>'
    if kind == "stack":
        return "".join(f'<rect x="-22" y="{-22 + k * 16}" width="44" height="11" rx="3" {st}/>'
                       f'<circle cx="13" cy="{-16.5 + k * 16}" r="2" fill="{dot}"/>' for k in range(3))
    if kind == "fork":
        return (f'<circle cx="-12" cy="-17" r="5" {st}/><circle cx="-12" cy="17" r="5" {st}/><circle cx="13" cy="-17" r="5" {st}/>'
                f'<line x1="-12" y1="-12" x2="-12" y2="12" {st}/><path d="M13,-12 C13,2 -12,-2 -12,10" {st}/>')
    if kind == "pr":
        return (f'<circle cx="-13" cy="-17" r="5" {st}/><circle cx="-13" cy="17" r="5" {st}/><circle cx="13" cy="17" r="5" {st}/>'
                f'<line x1="-13" y1="-12" x2="-13" y2="12" {st}/><path d="M13,12 V-8 Q13,-17 4,-17 H-2" {st}/>'
                f'<path d="M3,-23 L-3,-17 L3,-11" {st}/>')
    if kind == "chat":
        return (f'<path d="M-22,-16 H22 V10 H-6 L-16,20 V10 H-22 Z" {st}/>'
                + "".join(f'<circle cx="{dx}" cy="-3" r="2.6" fill="{dot}"/>' for dx in (-10, 0, 10)))
    if kind == "panel":
        return (f'<rect x="-24" y="-20" width="48" height="40" rx="5" {st}/><line x1="-24" y1="-9" x2="24" y2="-9" {st}/>'
                f'<line x1="-13" y1="12" x2="-13" y2="4" {st}/><line x1="0" y1="12" x2="0" y2="-1" {st}/>'
                f'<line x1="13" y1="12" x2="13" y2="7" {st}/>')
    if kind == "globe":
        return (f'<circle cx="0" cy="0" r="18" {st}/><ellipse cx="0" cy="0" rx="8" ry="18" {st}/>'
                f'<line x1="-18" y1="0" x2="18" y2="0" {st}/>')
    raise ValueError(kind)


# ---------------------------------------------------------------- one-line section banners
def banner(kind, title, subtitle, stats, c):
    H = 68
    b = [frame(W, H, c)]
    b.append(f'<rect x="14" y="14" width="40" height="40" rx="8" fill="{c["panel"]}" stroke="{c["border"]}"/>')
    b.append(f'<g transform="translate(34 34) scale(.42)">{glyph(kind, c)}</g>')
    b.append(t(68, 31, title, 16, c["text"], 600))
    b.append(t(68, 51, subtitle, 13, c["muted"]))
    cw, x0 = 112, W - 3 * 112
    for k, (num, lab) in enumerate(stats):
        x = x0 + k * cw
        b.append(vline(x, 14, H - 14, c))
        b.append(t(x + 16, 33, num, 17, c["accent"], 600))
        b.append(t(x + 16, 51, lab, 12, c["muted"]))
    return svg(W, H, "".join(b), f"{title} — {subtitle}")


BANNERS = {
    "android": ("phone", {
        "en": ("BadVPN for Android", "VPN client on my mihomo fork · Android 6+",
               [("0.85 s", "tap → VPN up"), ("0.2 s", "cold start"), ("1 key", "signs every APK")]),
        "ru": ("BadVPN для Android", "VPN-клиент на моём форке mihomo · Android 6+",
               [("0.85 с", "нажатие → VPN"), ("0.2 с", "холодный старт"), ("1 ключ", "подпись APK")]),
    }),
    "windows": ("laptop", {
        "en": ("BPN for Windows", "Tauri UI + privileged Rust service · Mihomo TUN",
               [("25k", "lines of Rust"), ("158", "tests"), ("3", "deps by hash")]),
        "ru": ("BPN для Windows", "Tauri + привилегированный сервис на Rust · Mihomo TUN",
               [("25k", "строк Rust"), ("158", "тестов"), ("3", "сверка хешей")]),
    }),
    "product": ("stack", {
        "en": ("BPN / BadVPN", "Private · Telegram bot, backend, panel, nodes",
               [("~190k", "lines of code"), ("1.8k", "commits"), ("160+", "test files")]),
        "ru": ("BPN / BadVPN", "Приватный · Telegram-бот, бэкенд, панель, ноды",
               [("~190k", "строк кода"), ("1.8k", "коммитов"), ("160+", "файлов тестов")]),
    }),
    "mihomo": ("fork", {
        "en": ("Rerowros/mihomo", "Proxy core fork · upstream tag + 5 patches",
               [("×5–8", "XHTTP upload"), ("3 / 3", "Xray versions OK"), ("5", "patches")]),
        "ru": ("Rerowros/mihomo", "Форк ядра · тег upstream + 5 патчей",
               [("×5–8", "отправка XHTTP"), ("3 / 3", "версии Xray"), ("5", "патчей")]),
    }),
    "clashfest": ("pr", {
        "en": ("Nemu-x/ClashFest", "Core contributor · Android client on mihomo · 222★",
               [("30", "merged PRs"), ("+19.6k", "lines"), ("~15%", "of codebase")]),
        "ru": ("Nemu-x/ClashFest", "Core contributor · Android-клиент на mihomo · 222★",
               [("30", "PR смёржено"), ("+19.6k", "строк"), ("~15%", "всего кода")]),
    }),
    "tg-recall": ("chat", {
        "en": ("tg-recall", "Local-first Telegram archive for AI agents · Python",
               [("300+", "tests"), ("15k", "lines"), ("MCP", "tg:// citations")]),
        "ru": ("tg-recall", "Локальный архив Telegram для AI-агентов · Python",
               [("300+", "тестов"), ("15k", "строк"), ("MCP", "ссылки tg://")]),
    }),
    "pasarguard": ("panel", {
        "en": ("PasarGuard", "Contributor · VPN panel + node · 2.6k★",
               [("4", "merged PRs"), ("4", "in review"), ("3", "repos")]),
        "ru": ("PasarGuard", "Контрибьютор · VPN-панель + нода · 2.6k★",
               [("4", "смёржено"), ("4", "на ревью"), ("3", "репо")]),
    }),
}


# ---------------------------------------------------------------- architecture
def box(x, y, w, h, title, lines, c, sub=None, hl=False):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c["panel"]}" '
           f'stroke="{c["accent"] if hl else c["border"]}"/>',
           t(x + 14, y + 25, title, 15, c["text"], 600)]
    yy = y + 44
    if sub:
        out.append(t(x + 14, yy, sub, 12, c["accent"] if hl else c["faint"], 400, font=MONO))
        yy += 21
    for ln in lines:
        out.append(t(x + 14, yy, ln, 13, c["muted"]))
        yy += 19
    return "".join(out)


def arrow_defs(c):
    return "".join(f'<marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
                   f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>'
                   for i, col in (("ah", c["faint"]), ("ahs", c["accent"])))


def label(x, y, s, c, anchor="middle"):
    return t(x, y, s, 11, c["faint"], 400, anchor, MONO)


def arrow(x1, y1, x2, y2, c, dashed=False, strong=False):
    dash = ' stroke-dasharray="4 4"' if dashed else ""
    col, m = (c["accent"], "ahs") if strong else (c["faint"], "ah")
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{1.6 if strong else 1}"'
            f'{dash} marker-end="url(#{m})"/>')


def architecture(c):
    H = 430
    b = [frame(W, H, c), heading(c, "How BPN fits together", "Private code · ~190k lines · 1.8k commits")]
    b.append(box(20, 80, 220, 150, "Telegram bot · Mini App", ["sign-up, payments", "support, referrals",
                                                                "several brands"], c, sub="Python · aiogram"))
    b.append(box(290, 80, 300, 150, "Backend", ["traffic ledger with rollover", "payments reconciled, not trusted",
                                                "idempotent admin via outbox"], c, sub="Next.js · Prisma · Postgres"))
    b.append(box(640, 80, 220, 150, "VPN panel", ["users, limits, traffic", "node configs, rollout"], c,
                 sub="Xray · REALITY · XHTTP"))
    b.append(arrow(240, 150, 287, 150, c) + label(264, 142, "orders", c))
    b.append(arrow(590, 140, 637, 140, c) + label(614, 132, "users", c))
    b.append(arrow(640, 178, 593, 178, c) + label(616, 194, "traffic", c))

    b.append(f'<path d="M380,230 V258 H130 V296" fill="none" stroke="{c["faint"]}" stroke-dasharray="4 4" marker-end="url(#ah)"/>')
    b.append(label(255, 252, "subscription link", c))
    b.append(f'<path d="M750,230 V274 H372" fill="none" stroke="{c["faint"]}" stroke-dasharray="4 4"/>')
    for x in (372, 577):
        b.append(arrow(x, 274, x, 296, c, dashed=True))
    b.append(label(742, 268, "node configs", c, "end"))

    b.append(box(20, 300, 220, 110, "Clients", ["Windows · Tauri + Rust", "Android · Kotlin"], c,
                 sub="mihomo core, my fork", hl=True))
    b.append(box(290, 300, 165, 110, "Front node", ["entry for mobile", "whitelist networks"], c))
    b.append(box(495, 300, 165, 110, "Exit node", ["abroad, clean IP"], c))
    b.append(f'<rect x="700" y="300" width="160" height="110" rx="8" fill="none" stroke="{c["border"]}" stroke-dasharray="4 4"/>')
    b.append(f'<g transform="translate(780 342) scale(.6)">{glyph("globe", c)}</g>')
    b.append(t(780, 386, "Internet", 15, c["text"], 600, "middle"))
    for x1, x2 in ((240, 287), (455, 492), (660, 697)):
        b.append(arrow(x1, 355, x2, 355, c, strong=True))
    return svg(W, H, "".join(b), "How BPN fits together: Telegram bot, backend, VPN panel, clients, front and exit nodes",
               arrow_defs(c))


# ---------------------------------------------------------------- REALITY matrix
def reality(c):
    H = 300
    b = [frame(W, H, c), heading(c, "REALITY that still connects to current Xray",
                                 "mihomo ↔ real Xray REALITY server on 127.0.0.1 · VLESS over TCP · interop test")]
    cols, cx0, cw, rh, top = ["Xray 26.3.27", "26.7.28", "26.9.9"], 470, 130, 40, 92
    for i, col in enumerate(cols):
        b.append(t(cx0 + i * cw + cw / 2, top, col, 12, c["faint"], 400, "middle", MONO))
    b.append(hline(20, W - 20, top + 10, c))
    rows = [("upstream · chrome", "", "ynn", False), ("upstream · firefox", "ML-KEM on", "ynn", False),
            ("upstream · no fingerprint", "", "nnn", False), ("my fork · chrome/firefox/safari", "ML-KEM on", "yyy", True)]
    for r, (name, note, res, hl) in enumerate(rows):
        y = top + 10 + r * rh
        if hl:
            b.append(f'<rect x="20" y="{y}" width="{W - 40}" height="{rh}" fill="{c["panel"]}"/>')
        b.append(t(32, y + 25, name, 14, c["text"], 600 if hl else 400))
        if note:
            b.append(t(290, y + 25, note, 11, c["faint"], 400, font=MONO))
        for i, ch in enumerate(res):
            ok = ch == "y"
            b.append(t(cx0 + i * cw + cw / 2, y + 25, "✓ connects" if ok else "✕ fails", 13,
                       c["ok"] if ok else c["bad"], 500, "middle"))
        b.append(hline(20, W - 20, y + rh, c))
    b.append(t(20, 280, "Patches: current Xray client version, Firefox 148 / Safari 26.3 uTLS fingerprints, "
                        "opt-in X25519MLKEM768", 12, c["faint"]))
    return svg(W, H, "".join(b), "REALITY compatibility: upstream mihomo vs my fork across Xray versions")


# ---------------------------------------------------------------- XHTTP upload chart
def xhttp(c):
    H = 330
    b = [frame(W, H, c), heading(c, "Parallel XHTTP uploads: 5–8× faster upload",
                                 "Upload, Mbit/s · 150 ms RTT · mihomo ↔ real Xray 26.3.27 · packet-up (CDN lines)")]
    b.append(f'<rect x="20" y="76" width="10" height="10" rx="2" fill="{c["weak"]}"/>')
    b.append(t(36, 85, "upstream: 1 request in flight", 12, c["muted"]))
    b.append(f'<rect x="230" y="76" width="10" height="10" rx="2" fill="{c["accent"]}"/>')
    b.append(t(246, 85, "my fork: up to 8 in flight", 12, c["muted"]))
    x0, scale, top = 190, 36.0, 108
    for v in (0, 5, 10, 15):
        x = x0 + v * scale
        b.append(vline(x, top - 4, top + 4 * 46 - 6, c, c["grid"]))
        b.append(t(x, top + 4 * 46 + 8, str(v), 11, c["faint"], 400, "middle", MONO))
    rows = [("POST · HTTP/2", 2.3, 12.3), ("GET + headers · HTTP/2", 1.8, 12.9),
            ("POST · HTTP/1.1", 1.8, 13.8), ("GET + headers · HTTP/1.1", 2.4, 11.5)]
    for i, (name, a, n8) in enumerate(rows):
        y = top + i * 46
        b.append(t(x0 - 12, y + 18, name, 13, c["text"], 400, "end"))
        b.append(f'<rect x="{x0}" y="{y}" width="{a * scale:.1f}" height="12" rx="2" fill="{c["weak"]}"/>')
        b.append(t(x0 + a * scale + 6, y + 10, f"{a}", 11, c["faint"], 400, font=MONO))
        b.append(f'<rect x="{x0}" y="{y + 16}" width="{n8 * scale:.1f}" height="12" rx="2" fill="{c["accent"]}"/>')
        b.append(t(x0 + n8 * scale + 6, y + 26, f"{n8}", 11, c["text"], 600, font=MONO))
        b.append(t(W - 20, y + 22, f"×{n8 / a:.1f}", 18, c["accent"], 600, "end"))
    b.append(t(20, 314, "16 MiB transfers sha256-checked both ways on Xray 26.3.27, 26.7.28, 26.9.9", 12, c["faint"]))
    return svg(W, H, "".join(b), "XHTTP packet-up upload throughput: upstream mihomo vs my fork")


# ---------------------------------------------------------------- Android: tap to first request
def android_connect(c):
    H = 290
    b = [frame(W, H, c), heading(c, "Tap “connect” → first request through the VPN",
                                 "Seconds, lower is better · realme RMX8899, Android 16, Wi-Fi · measured over adb")]
    rows = [("BadVPN 1.1.5", 0.85, "median of 5", c["accent"]), ("BadVPN 1.1.4", 1.35, "3 runs", c["accent2"]),
            ("ClashFest", 1.56, "3 runs", c["weak"]), ("INCY 3.7.0", 1.56, "3 runs", c["weak"])]
    x0, scale, top = 130, 330.0, 80
    for v in (0, 0.5, 1.0, 1.5):
        x = x0 + v * scale
        b.append(vline(x, top - 4, top + 4 * 34, c, c["grid"]))
        b.append(t(x, top + 4 * 34 + 14, f"{v:g} s", 11, c["faint"], 400, "middle", MONO))
    for i, (name, v, note, fill) in enumerate(rows):
        y = top + i * 34
        b.append(t(x0 - 12, y + 19, name, 13, c["text"], 600 if i == 0 else 400, "end"))
        b.append(f'<rect x="{x0}" y="{y + 6}" width="{v * scale:.1f}" height="18" rx="2" fill="{fill}"/>')
        b.append(t(x0 + v * scale + 8, y + 20, f"{v:.2f} s", 13, c["text"] if i == 0 else c["muted"], 600, font=MONO))
        b.append(t(x0 + v * scale + 70, y + 20, note, 11, c["faint"], 400, font=MONO))
    b.append(t(20, 256, "1.1.4 vs ClashFest vs INCY: one rough session on 29.09.2026, 3 runs each, different exits.",
               12, c["faint"]))
    b.append(t(20, 276, "1.1.5 drops a 500 ms wait and a second config pass: separate session, 5 runs, 1.1.4 median 1.41 s.",
               12, c["faint"]))
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
                (OUT / f"banner-{name}{suffix}-{theme}.svg").write_text(banner(kind, *args, c), encoding="utf-8")
    print(len(list(OUT.iterdir())), "files in", OUT)


if __name__ == "__main__":
    main()
