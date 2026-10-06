"""Renders the static profile SVGs (dark + light) into assets/. Run: python scripts/render_assets.py"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(card="#0d1117", panel="#161b22", border="#30363d", text="#e6edf3", muted="#9198a1",
                 faint="#6e7681", grid="#21262d", ok="#3fb950", okbg="#12261e", bad="#f85149",
                 badbg="#2b1416", n1="#484f58", dot="#21262d"),
    "light": dict(card="#ffffff", panel="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e",
                  faint="#818b98", grid="#e5e8eb", ok="#1a7f37", okbg="#dafbe1", bad="#cf222e",
                  badbg="#ffebe9", n1="#afb8c1", dot="#e5e8eb"),
}

GRAD = """<linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#2f6bff"/><stop offset=".55" stop-color="#8b3dff"/><stop offset="1" stop-color="#e81cff"/>
</linearGradient>
<linearGradient id="gu" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1200" y2="0">
<stop offset="0" stop-color="#2f6bff"/><stop offset=".55" stop-color="#8b3dff"/><stop offset="1" stop-color="#e81cff"/>
</linearGradient>"""


def t(x, y, s, size=16, fill=None, weight=400, anchor="start", font=SANS, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            f'<defs>{GRAD}</defs>{body}</svg>\n')


def frame(w, h, c):
    return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="{c["card"]}" stroke="{c["border"]}"/>'


# ---------------------------------------------------------------- header
def icon(kind, x, y, c):
    s = c["text"]
    if kind == "phone":
        return (f'<rect x="{x-7}" y="{y-11}" width="14" height="22" rx="3" fill="none" stroke="{s}" stroke-width="1.8"/>'
                f'<line x1="{x-2}" y1="{y+7}" x2="{x+2}" y2="{y+7}" stroke="{s}" stroke-width="1.8" stroke-linecap="round"/>')
    if kind == "laptop":
        return (f'<rect x="{x-10}" y="{y-9}" width="20" height="13" rx="2" fill="none" stroke="{s}" stroke-width="1.8"/>'
                f'<line x1="{x-13}" y1="{y+8}" x2="{x+13}" y2="{y+8}" stroke="{s}" stroke-width="1.8" stroke-linecap="round"/>')
    if kind == "server":
        return (f'<rect x="{x-10}" y="{y-10}" width="20" height="8" rx="2" fill="none" stroke="{s}" stroke-width="1.8"/>'
                f'<rect x="{x-10}" y="{y+2}" width="20" height="8" rx="2" fill="none" stroke="{s}" stroke-width="1.8"/>'
                f'<circle cx="{x+5}" cy="{y-6}" r="1.3" fill="{s}"/><circle cx="{x+5}" cy="{y+6}" r="1.3" fill="{s}"/>')
    if kind == "globe":
        return (f'<circle cx="{x}" cy="{y}" r="11" fill="none" stroke="{s}" stroke-width="1.8"/>'
                f'<ellipse cx="{x}" cy="{y}" rx="5" ry="11" fill="none" stroke="{s}" stroke-width="1.5"/>'
                f'<line x1="{x-11}" y1="{y}" x2="{x+11}" y2="{y}" stroke="{s}" stroke-width="1.5"/>')
    raise ValueError(kind)


def header(c):
    W, H = 1200, 340
    b = [frame(W, H, c)]
    b.append(f'<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">'
             f'<circle cx="2" cy="2" r="1.2" fill="{c["dot"]}"/></pattern></defs>')
    b.append(f'<rect x="680" y="20" width="500" height="200" fill="url(#dots)"/>')
    b.append(t(56, 66, "@Rerowros", 18, "url(#g)", 600, font=MONO))
    b.append(t(56, 126, "Iaroslav", 60, c["text"], 700))
    b.append(t(56, 168, "Censorship-resistant networking", 25, c["muted"]))
    b.append(t(56, 202, "Android & desktop VPN clients · Telegram & AI tools", 25, c["muted"]))

    # network path: clients -> DPI -> front -> exit -> internet
    pa = "M740,82 C805,82 815,130 875,130 L1005,130 L1125,130"
    pb = "M740,178 C805,178 815,130 875,130 L1005,130 L1125,130"
    for p in (pa, pb):
        b.append(f'<path d="{p}" fill="none" stroke="url(#gu)" stroke-width="2.5" stroke-linecap="round"/>')
    b.append(f'<line x1="808" y1="50" x2="808" y2="208" stroke="{c["bad"]}" stroke-width="2" '
             f'stroke-dasharray="5 6" opacity=".75"/>')
    b.append(t(808, 42, "DPI", 13, c["bad"], 700, "middle", MONO))
    b.append(f'<path id="pa" d="{pa}" fill="none"/><path id="pb" d="{pb}" fill="none"/>')
    for pid, begin in (("pa", "0s"), ("pb", "1.4s"), ("pa", "2.1s")):
        b.append(f'<circle r="4.5" fill="#e81cff"><animateMotion dur="2.8s" begin="{begin}" '
                 f'repeatCount="indefinite"><mpath href="#{pid}"/></animateMotion></circle>')
    nodes = [(740, 82, "phone", "Android"), (740, 178, "laptop", "Windows"),
             (875, 130, "server", "front"), (1005, 130, "server", "exit"), (1125, 130, "globe", "internet")]
    for x, y, kind, label in nodes:
        b.append(f'<circle cx="{x}" cy="{y}" r="25" fill="{c["panel"]}" stroke="url(#g)" stroke-width="2"/>')
        b.append(icon(kind, x, y, c))
        ly = y + 44 if label not in ("Android",) else y - 34
        b.append(t(x, ly, label, 13, c["muted"], 500, "middle", MONO))

    b.append(f'<line x1="56" y1="232" x2="1144" y2="232" stroke="{c["border"]}"/>')
    stats = [("~190k", "lines in my VPN product"), ("2", "VPN apps: Android, Windows"),
             ("30", "merged PRs in ClashFest"), ("5", "patches on mihomo core")]
    for i, (num, label) in enumerate(stats):
        x = 56 + i * 275
        b.append(t(x, 282, num, 36, "url(#g)", 700))
        b.append(t(x, 310, label, 17, c["muted"]))
    return svg(W, H, "".join(b), "Iaroslav · Rerowros — censorship-resistant networking, VPN clients, Telegram and AI tools")


# ---------------------------------------------------------------- architecture
def box(x, y, w, h, title, lines, c, hl=False, sub=None):
    stroke = 'url(#g)' if hl else c["border"]
    sw = 2 if hl else 1
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{c["panel"]}" stroke="{stroke}" stroke-width="{sw}"/>',
           t(x + 20, y + 36, title, 20, c["text"], 650)]
    yy = y + 58
    if sub:
        out.append(t(x + 20, yy, sub, 15, c["muted"], 500, font=MONO))
        yy += 26
    for ln in lines:
        indent = ln.startswith("  ")
        out.append(t(x + (34 if indent else 20), yy, ln.strip(), 16, c["faint"] if indent else c["muted"]))
        yy += 23
    return "".join(out)


def arrow_defs(c):
    return (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c["muted"]}"/></marker>'
            f'<marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="#c13bff"/></marker></defs>')


def label(x, y, s, c, anchor="middle"):
    return t(x, y, s, 14, c["faint"], 500, anchor, MONO)


def architecture(c):
    W, H = 1200, 600
    b = [frame(W, H, c), arrow_defs(c)]
    b.append(t(40, 56, "How BPN fits together", 26, c["text"], 700))
    b.append(t(40, 84, "My VPN product, end to end · private code, ~190k lines, 1.8k commits", 16, c["muted"]))

    # packet flow sits under the boxes, so the moving dot only shows between them
    b.append('<path id="flow" d="M185,520 L1055,520" fill="none"/>')
    for x1, x2 in ((330, 406), (640, 676), (910, 946)):
        b.append(f'<line x1="{x1}" y1="520" x2="{x2}" y2="520" stroke="url(#gu)" stroke-width="2.5" marker-end="url(#ahg)"/>')
    b.append('<circle r="5" fill="#e81cff"><animateMotion dur="3.2s" repeatCount="indefinite">'
             '<mpath href="#flow"/></animateMotion></circle>')

    b.append(box(40, 116, 290, 200, "Telegram bot · Mini App", [
        "sign-up, plans, payments", "support, referrals", "several brands, one backend"], c, sub="Python · aiogram"))
    b.append(box(410, 116, 400, 200, "Backend", [
        "• traffic ledger with rollover", "  shadow-validated, staged rollout",
        "• payments reconciled, not webhook-trusted", "• idempotent admin actions via outbox"], c,
        sub="Next.js · Prisma · PostgreSQL"))
    b.append(box(890, 116, 270, 200, "VPN panel", [
        "users, limits, traffic", "node configs, rollout"], c, sub="Xray · REALITY · XHTTP"))

    b.append(f'<line x1="330" y1="196" x2="406" y2="196" stroke="{c["muted"]}" stroke-width="1.6" marker-end="url(#ah)"/>')
    b.append(label(368, 184, "orders", c))
    b.append(f'<line x1="810" y1="196" x2="886" y2="196" stroke="{c["muted"]}" stroke-width="1.6" marker-end="url(#ah)"/>')
    b.append(label(848, 184, "users", c))
    b.append(f'<line x1="886" y1="240" x2="814" y2="240" stroke="{c["muted"]}" stroke-width="1.6" marker-end="url(#ah)"/>')
    b.append(label(848, 262, "traffic", c))

    # subscription: backend -> clients
    b.append(f'<path d="M470,316 V376 H185 V424" fill="none" stroke="{c["muted"]}" stroke-width="1.6" '
             f'stroke-dasharray="6 5" marker-end="url(#ah)"/>')
    b.append(label(330, 368, "subscription link", c))
    # panel -> nodes
    b.append(f'<path d="M1025,316 V376 H525" fill="none" stroke="{c["muted"]}" stroke-width="1.6" stroke-dasharray="6 5"/>')
    for x in (525, 795):
        b.append(f'<line x1="{x}" y1="376" x2="{x}" y2="424" stroke="{c["muted"]}" stroke-width="1.6" '
                 f'stroke-dasharray="6 5" marker-end="url(#ah)"/>')
    b.append(label(1015, 368, "node configs", c, "end"))

    b.append(box(40, 428, 290, 140, "Clients", [
        "Windows · Tauri + Rust", "Android · Kotlin"], c, hl=True, sub="core: mihomo, my fork"))
    b.append(box(410, 428, 230, 140, "Front node", ["entry point for mobile", "networks on whitelists"], c))
    b.append(box(680, 428, 230, 140, "Exit node", ["abroad, clean IP", "for the traffic"], c))
    b.append(f'<rect x="950" y="428" width="210" height="140" rx="14" fill="{c["card"]}" stroke="{c["border"]}" stroke-dasharray="4 5"/>')
    b.append(icon("globe", 1055, 484, c))
    b.append(t(1055, 532, "Internet", 20, c["text"], 650, "middle"))
    return svg(W, H, "".join(b), "How BPN fits together: Telegram bot, backend, VPN panel, clients, front and exit nodes")


# ---------------------------------------------------------------- REALITY matrix
def reality(c):
    W, H = 1200, 430
    b = [frame(W, H, c)]
    b.append(t(40, 56, "REALITY that still connects to current Xray", 26, c["text"], 700))
    b.append(t(40, 84, "mihomo client ↔ real Xray REALITY server on 127.0.0.1 · VLESS over TCP · interop test in the fork",
               16, c["muted"]))
    cols = ["Xray 26.3.27", "Xray 26.7.28", "Xray 26.9.9"]
    cx0, cw, ch = 640, 170, 44
    for i, col in enumerate(cols):
        b.append(t(cx0 + i * (cw + 10) + cw / 2, 128, col, 14, c["muted"], 600, "middle", MONO))
    rows = [
        ("upstream mihomo · chrome", "", "ynn", False),
        ("upstream mihomo · firefox", "ML-KEM on", "ynn", False),
        ("upstream mihomo · no fingerprint", "", "nnn", False),
        ("my fork · chrome / firefox / safari", "ML-KEM on", "yyy", True),
    ]
    y = 146
    for name, note, res, hl in rows:
        if hl:
            b.append(f'<rect x="28" y="{y - 6}" width="1144" height="{ch + 12}" rx="12" fill="none" stroke="url(#g)" stroke-width="2"/>')
        b.append(t(48, y + 28, name, 16, c["text"], 650 if hl else 500))
        if note:
            b.append(t(400, y + 28, note, 14, c["faint"], 500, font=MONO))
        for i, r in enumerate(res):
            x = cx0 + i * (cw + 10)
            okk = r == "y"
            b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="9" fill="{c["okbg"] if okk else c["badbg"]}"/>')
            b.append(t(x + cw / 2, y + 28, "✓ connects" if okk else "✕ fails", 15, c["ok"] if okk else c["bad"], 600, "middle"))
        y += ch + 16
    b.append(t(40, 404, "Patches: current Xray client version in the session ID, Firefox 148 / Safari 26.3 uTLS fingerprints, "
                        "opt-in X25519MLKEM768", 15, c["faint"]))
    return svg(W, H, "".join(b), "REALITY compatibility: upstream mihomo vs my fork across Xray versions")


# ---------------------------------------------------------------- XHTTP upload chart
def xhttp(c):
    W, H = 1200, 490
    b = [frame(W, H, c)]
    b.append(t(40, 56, "Parallel XHTTP uploads: 5–8× faster upload", 26, c["text"], 700))
    b.append(t(40, 84, "Upload, Mbit/s · 150 ms RTT · mihomo ↔ real Xray 26.3.27 · packet-up mode, used for CDN-fronted lines",
               16, c["muted"]))
    # legend
    b.append(f'<rect x="40" y="106" width="14" height="14" rx="3" fill="{c["n1"]}"/>')
    b.append(t(62, 118, "upstream: 1 request in flight", 14, c["muted"]))
    b.append(f'<rect x="300" y="106" width="14" height="14" rx="3" fill="url(#g)"/>')
    b.append(t(322, 118, "my fork: up to 8 in flight, Xray-style pipelining", 14, c["muted"]))

    x0, scale, top = 300, 50.0, 150
    for v in (0, 5, 10, 15):
        x = x0 + v * scale
        b.append(f'<line x1="{x}" y1="{top}" x2="{x}" y2="{top + 4 * 66 - 6}" stroke="{c["grid"]}"/>')
        b.append(t(x, top + 4 * 66 + 14, str(v), 12, c["faint"], 500, "middle", MONO))
    rows = [("POST · HTTP/2", 2.3, 12.3), ("GET + headers · HTTP/2", 1.8, 12.9),
            ("POST · HTTP/1.1", 1.8, 13.8), ("GET + headers · HTTP/1.1", 2.4, 11.5)]
    for i, (name, a, bb) in enumerate(rows):
        y = top + i * 66 + 6
        b.append(t(x0 - 20, y + 25, name, 15, c["text"], 500, "end"))
        b.append(f'<rect x="{x0}" y="{y}" width="{a * scale:.1f}" height="17" rx="4" fill="{c["n1"]}"/>')
        b.append(t(x0 + a * scale + 8, y + 13, f"{a}", 13, c["muted"], 600, font=MONO))
        b.append(f'<rect x="{x0}" y="{y + 22}" width="{bb * scale:.1f}" height="17" rx="4" fill="url(#gu)"/>')
        b.append(t(x0 + bb * scale + 8, y + 35, f"{bb}", 13, c["text"], 700, font=MONO))
        b.append(t(1150, y + 31, f"×{bb / a:.1f}", 26, "url(#g)", 700, "end"))
    b.append(t(40, 468, "16 MiB transfers sha256-checked both ways on Xray 26.3.27, 26.7.28 and 26.9.9 · "
                        "upstream ceiling ≈ request size / RTT", 15, c["faint"]))
    return svg(W, H, "".join(b), "XHTTP packet-up upload throughput: upstream mihomo vs my fork")


# ---------------------------------------------------------------- Android: tap to first request
def android_connect(c):
    W, H = 1200, 400
    b = [frame(W, H, c)]
    b.append(t(40, 56, "Tap “connect” → first request through the VPN", 26, c["text"], 700))
    b.append(t(40, 84, "Seconds, lower is better · realme RMX8899, Android 16, Wi-Fi · measured over adb", 16, c["muted"]))
    rows = [("BadVPN 1.1.5", 0.85, "median of 5", "url(#gu)", 1),
            ("BadVPN 1.1.4", 1.35, "3 runs", "url(#gu)", .45),
            ("ClashFest", 1.56, "3 runs", c["n1"], 1),
            ("INCY 3.7.0", 1.56, "3 runs", c["n1"], 1)]
    x0, scale, top = 260, 460.0, 120
    for v in (0, 0.5, 1.0, 1.5):
        x = x0 + v * scale
        b.append(f'<line x1="{x}" y1="{top - 6}" x2="{x}" y2="{top + 4 * 50}" stroke="{c["grid"]}"/>')
        b.append(t(x, top + 4 * 50 + 18, f"{v:g} s", 12, c["faint"], 500, "middle", MONO))
    for i, (name, v, note, fill, op) in enumerate(rows):
        y = top + i * 50
        b.append(t(x0 - 20, y + 22, name, 17, c["text"], 650 if i == 0 else 500, "end"))
        b.append(f'<rect x="{x0}" y="{y + 4}" width="{v * scale:.1f}" height="26" rx="5" fill="{fill}" opacity="{op}"/>')
        b.append(t(x0 + v * scale + 10, y + 23, f"{v:.2f} s", 16, c["text"] if i == 0 else c["muted"], 700, font=MONO))
        b.append(t(x0 + v * scale + 90, y + 23, note, 13, c["faint"], 500, font=MONO))
    b.append(t(40, 362, "1.1.4 vs ClashFest vs INCY: one rough session on 29.09.2026, 3 runs each, different exit servers.",
               14, c["faint"]))
    b.append(t(40, 384, "1.1.5 (no 500 ms wait, no second config pass): separate session, 5 runs vs 1.1.4 median 1.41 s.",
               14, c["faint"]))
    return svg(W, H, "".join(b), "Time from tap to first request through the VPN: BadVPN 1.1.5 0.85 s, ClashFest and INCY 1.56 s")


# ---------------------------------------------------------------- section banners
def glyph(kind, cx, cy, c):
    st = f'fill="none" stroke="{c["text"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
    if kind == "phone":
        return (f'<rect x="{cx-14}" y="{cy-23}" width="28" height="46" rx="6" {st}/>'
                f'<line x1="{cx-4}" y1="{cy+15}" x2="{cx+4}" y2="{cy+15}" {st}/>')
    if kind == "laptop":
        return (f'<rect x="{cx-22}" y="{cy-17}" width="44" height="28" rx="3" {st}/>'
                f'<line x1="{cx-28}" y1="{cy+18}" x2="{cx+28}" y2="{cy+18}" {st}/>')
    if kind == "stack":
        return "".join(f'<rect x="{cx-22}" y="{cy-22+k*16}" width="44" height="11" rx="3" {st}/>'
                       f'<circle cx="{cx+13}" cy="{cy-16.5+k*16}" r="1.6" fill="{c["text"]}"/>' for k in range(3))
    if kind == "fork":
        return (f'<circle cx="{cx-12}" cy="{cy-17}" r="5" {st}/><circle cx="{cx-12}" cy="{cy+17}" r="5" {st}/>'
                f'<circle cx="{cx+13}" cy="{cy-17}" r="5" {st}/><line x1="{cx-12}" y1="{cy-12}" x2="{cx-12}" y2="{cy+12}" {st}/>'
                f'<path d="M{cx+13},{cy-12} C{cx+13},{cy+2} {cx-12},{cy-2} {cx-12},{cy+10}" {st}/>')
    if kind == "pr":
        return (f'<circle cx="{cx-13}" cy="{cy-17}" r="5" {st}/><circle cx="{cx-13}" cy="{cy+17}" r="5" {st}/>'
                f'<circle cx="{cx+13}" cy="{cy+17}" r="5" {st}/><line x1="{cx-13}" y1="{cy-12}" x2="{cx-13}" y2="{cy+12}" {st}/>'
                f'<path d="M{cx+13},{cy+12} V{cy-8} Q{cx+13},{cy-17} {cx+4},{cy-17} H{cx-2}" {st}/>'
                f'<path d="M{cx+3},{cy-23} L{cx-3},{cy-17} L{cx+3},{cy-11}" {st}/>')
    if kind == "chat":
        return (f'<path d="M{cx-22},{cy-16} H{cx+22} V{cy+10} H{cx-6} L{cx-16},{cy+20} V{cy+10} H{cx-22} Z" {st}/>'
                + "".join(f'<circle cx="{cx+dx}" cy="{cy-3}" r="2.4" fill="{c["text"]}"/>' for dx in (-10, 0, 10)))
    if kind == "terminal":
        return (f'<rect x="{cx-24}" y="{cy-19}" width="48" height="38" rx="5" {st}/>'
                f'<path d="M{cx-14},{cy-6} L{cx-6},{cy+1} L{cx-14},{cy+8}" {st}/>'
                f'<line x1="{cx-1}" y1="{cy+9}" x2="{cx+12}" y2="{cy+9}" {st}/>')
    if kind == "book":
        return (f'<path d="M{cx},{cy-14} C{cx-8},{cy-20} {cx-18},{cy-20} {cx-25},{cy-17} V{cy+17} '
                f'C{cx-18},{cy+14} {cx-8},{cy+14} {cx},{cy+20} Z" {st}/>'
                f'<path d="M{cx},{cy-14} C{cx+8},{cy-20} {cx+18},{cy-20} {cx+25},{cy-17} V{cy+17} '
                f'C{cx+18},{cy+14} {cx+8},{cy+14} {cx},{cy+20}" {st}/>')
    if kind == "panel":
        return (f'<rect x="{cx-24}" y="{cy-20}" width="48" height="40" rx="5" {st}/>'
                f'<line x1="{cx-24}" y1="{cy-9}" x2="{cx+24}" y2="{cy-9}" {st}/>'
                f'<line x1="{cx-13}" y1="{cy+12}" x2="{cx-13}" y2="{cy+4}" {st}/>'
                f'<line x1="{cx}" y1="{cy+12}" x2="{cx}" y2="{cy-1}" {st}/>'
                f'<line x1="{cx+13}" y1="{cy+12}" x2="{cx+13}" y2="{cy+7}" {st}/>')
    raise ValueError(kind)


def banner(kind, kicker, title, subtitle, stats, c):
    W, H = 1200, 190
    b = [frame(W, H, c)]
    b.append(f'<rect x="1" y="1" width="8" height="{H-2}" rx="4" fill="url(#gu)"/>')
    b.append(f'<rect x="44" y="47" width="96" height="96" rx="24" fill="{c["panel"]}" stroke="url(#g)" stroke-width="2"/>')
    b.append(glyph(kind, 92, 95, c))
    b.append(t(170, 72, kicker, 15, "url(#g)", 700, font=MONO, extra='letter-spacing="1.5"'))
    b.append(t(170, 114, title, 36, c["text"], 700))
    b.append(t(170, 148, subtitle, 19, c["muted"]))
    b.append(f'<line x1="668" y1="40" x2="668" y2="150" stroke="{c["border"]}"/>')
    for k, (num, lab) in enumerate(stats):
        x = 700 + k * 165
        size = 36 if len(num) <= 5 else 30 if len(num) <= 7 else 24
        b.append(t(x, 102, num, size, "url(#g)", 700))
        for j, line in enumerate(lab.split("\n")):
            b.append(t(x, 131 + j * 20, line, 16, c["muted"]))
    b.append(t(1168, 34, "↗", 18, c["faint"], 600, "end"))
    return svg(W, H, "".join(b), f"{title} — {subtitle}")


BANNERS = {
    "android": ("phone", {
        "en": ("ANDROID APP", "BadVPN for Android", "VPN client on my mihomo fork, Android 6+",
               [("0.85 s", "tap → first request\nthrough the VPN"), ("0.2 s", "cold start\nto home screen"),
                ("1 key", "every APK signed,\nSHA-256 published")]),
        "ru": ("ANDROID-ПРИЛОЖЕНИЕ", "BadVPN для Android", "VPN-клиент на моём форке mihomo, Android 6+",
               [("0.85 с", "от нажатия до\nпервого запроса"), ("0.2 с", "холодный старт\nдо главной"),
                ("1 ключ", "все APK подписаны,\nSHA-256 в релизе")]),
    }),
    "windows": ("laptop", {
        "en": ("WINDOWS APP", "BPN for Windows", "Tauri UI + privileged Rust service, Mihomo TUN",
               [("25k", "lines of Rust"), ("158", "tests"), ("3", "components\nchecked by hash")]),
        "ru": ("ПРИЛОЖЕНИЕ ДЛЯ WINDOWS", "BPN для Windows", "Tauri + привилегированный сервис на Rust",
               [("25k", "строк Rust"), ("158", "тестов"), ("3", "компонента\nсверяются по хешу")]),
    }),
    "product": ("stack", {
        "en": ("THE PRODUCT · PRIVATE", "BPN / BadVPN", "Telegram bot, backend, panel, nodes, two apps",
               [("~190k", "lines of code"), ("1.8k", "commits"), ("160+", "test files")]),
        "ru": ("САМ ПРОДУКТ · ПРИВАТНЫЙ", "BPN / BadVPN", "Бот, бэкенд, панель, ноды и два приложения",
               [("~190k", "строк кода"), ("1.8k", "коммитов"), ("160+", "тестовых файлов")]),
    }),
    "mihomo": ("fork", {
        "en": ("PROXY CORE · FORK", "Rerowros/mihomo", "Upstream tag + 5 patches: REALITY, uTLS, XHTTP",
               [("×5–8", "faster XHTTP\nupload"), ("3 / 3", "Xray versions\nconnect"), ("5", "patches, rebased\nper release")]),
        "ru": ("ЯДРО · ФОРК", "Rerowros/mihomo", "Тег upstream + 5 патчей: REALITY, uTLS, XHTTP",
               [("×5–8", "быстрее отправка\nпо XHTTP"), ("3 / 3", "версии Xray\nподключаются"), ("5", "патчей, ребейз\nна каждый релиз")]),
    }),
    "clashfest": ("pr", {
        "en": ("OPEN SOURCE · CORE CONTRIBUTOR", "Nemu-x/ClashFest", "Android client on mihomo · 222★",
               [("30", "merged PRs"), ("+19.6k", "lines"), ("~15%", "of the codebase")]),
        "ru": ("OPEN SOURCE · CORE CONTRIBUTOR", "Nemu-x/ClashFest", "Android-клиент на mihomo · 222★",
               [("30", "смёрженных PR"), ("+19.6k", "строк"), ("~15%", "текущего кода")]),
    }),
    "tg-recall": ("chat", {
        "en": ("PROJECT · PYTHON · MCP", "tg-recall", "Local-first Telegram archive for people and AI",
               [("300+", "tests"), ("15k", "lines of Python"), ("2 OS", "CI on Windows\nand Linux")]),
        "ru": ("ПРОЕКТ · PYTHON · MCP", "tg-recall", "Локальный архив Telegram для людей и AI",
               [("300+", "тестов"), ("15k", "строк Python"), ("2 ОС", "CI на Windows\nи Linux")]),
    }),
    "sre-bench": ("terminal", {
        "en": ("PROJECT · BENCHMARK", "sre-agent-bench", "AI agents fix a broken Ubuntu server over SSH",
               [("11", "injected faults"), ("11", "model / harness\nsetups"), ("2", "survival checks:\nSIGKILL, reboot")]),
        "ru": ("ПРОЕКТ · БЕНЧМАРК", "sre-agent-bench", "AI-агенты чинят сломанный сервер по SSH",
               [("11", "неисправностей"), ("11", "конфигураций\nмоделей"), ("2", "проверки:\nSIGKILL, ребут")]),
    }),
    "wiki-mcp": ("book", {
        "en": ("PROJECT · CLOUDFLARE WORKERS", "wiki-mcp", "Agent-maintained wiki as a remote MCP server",
               [("0.83", "recall@5 on\na golden set"), ("536", "pages in the\nprivate wiki"), ("OAuth 2.1", "claude.ai,\nChatGPT")]),
        "ru": ("ПРОЕКТ · CLOUDFLARE WORKERS", "wiki-mcp", "Вики, которую ведут агенты, как MCP-сервер",
               [("0.83", "recall@5 на\nэталоне"), ("536", "страниц в\nприватной вики"), ("OAuth 2.1", "claude.ai,\nChatGPT")]),
    }),
    "pasarguard": ("panel", {
        "en": ("OPEN SOURCE · CONTRIBUTOR", "PasarGuard", "VPN panel + node · 2.6k★",
               [("4", "merged PRs"), ("4", "in review"), ("3", "repos: panel,\nnode, scripts")]),
        "ru": ("OPEN SOURCE · КОНТРИБЬЮТОР", "PasarGuard", "VPN-панель + нода · 2.6k★",
               [("4", "смёржено"), ("4", "на ревью"), ("3", "репо: panel,\nnode, scripts")]),
    }),
}


def main():
    OUT.mkdir(exist_ok=True)
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
