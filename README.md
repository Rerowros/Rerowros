<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Rerowros — Iaroslav, software engineer" src="assets/header-light.svg" width="100%">
</picture>

<p>
  <a href="https://t.me/rerowros"><img src="https://img.shields.io/badge/Telegram-@rerowros-171717?logo=telegram&logoColor=white&labelColor=000000&style=flat-square" alt="Telegram"></a>
  <a href="docs/README.ru.md"><img src="https://img.shields.io/badge/README-по--русски-171717?labelColor=000000&style=flat-square" alt="README in Russian"></a>
</p>

I write production software end to end: an Android app, a Windows app with a privileged Rust service, the backend and servers behind them, and the network core both apps share. In open source I'm a core contributor to ClashFest; on the side I build tools for AI agents.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Rerowros/Rerowros/output/stats-dark.svg">
  <img alt="Activity over the last 12 months: contributions, streaks, merged PRs to other repos" src="https://raw.githubusercontent.com/Rerowros/Rerowros/output/stats-light.svg" width="100%">
</picture>

## Apps

<a href="https://github.com/Rerowros/bpn-android-releases">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-android-dark.svg">
  <img alt="BadVPN for Android" src="assets/banner-android-light.svg" width="100%">
</picture>
</a>

<details>
<summary><b>Screenshots · connect-time benchmark vs ClashFest and INCY</b></summary>
<br>

[![Android release](https://img.shields.io/github/v/release/Rerowros/bpn-android-releases?label=APK&logo=android&logoColor=white&color=171717&labelColor=000000&style=flat-square)](https://github.com/Rerowros/bpn-android-releases/releases/latest)

A fork of [ClashFest](https://github.com/Nemu-x/ClashFest), where I'm a core contributor, running on [my mihomo fork](https://github.com/Rerowros/mihomo/tree/bpn/v1.19.32). One tap to connect, a separate mode for mobile networks that only allow whitelisted sites, and subscription import from Telegram or a QR code. Updates come from our own server; every APK is signed with the same key and its SHA-256 is published with the release.

<p>
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/01-home-on.png" width="23%" alt="Home screen, VPN on">
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/06-servers.png" width="23%" alt="Connection modes">
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/07-servers-whitelist.png" width="23%" alt="Whitelist mode">
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/05-home-light.png" width="23%" alt="Light theme">
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/android-connect-dark.svg">
  <img alt="Tap to first request through the VPN: BadVPN 1.1.5 0.85 s, BadVPN 1.1.4 1.35 s, ClashFest 1.56 s, INCY 1.56 s" src="assets/android-connect-light.svg" width="100%">
</picture>

The 1.1.5 speed-up came from two changes: no fixed 500 ms wait before the first config load, and no second pass over a config that was already validated.

</details>

<a href="https://github.com/Rerowros/bpn-releases">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-windows-dark.svg">
  <img alt="BPN for Windows" src="assets/banner-windows-light.svg" width="100%">
</picture>
</a>

<details>
<summary><b>How it's built</b></summary>
<br>

[![Windows release](https://img.shields.io/github/v/release/Rerowros/bpn-releases?label=installer&logo=windows&logoColor=white&color=171717&labelColor=000000&style=flat-square)](https://github.com/Rerowros/bpn-releases/releases/latest)

Windows 10/11. The Tauri UI runs unprivileged and talks over IPC to a Rust service that owns the TUN interface and runs Mihomo on [my core fork](https://github.com/Rerowros/mihomo/tree/bpn/v1.19.32). Optional zapret + WinDivert for YouTube, Discord and games. Third-party binaries (mihomo, zapret, WinDivert) are downloaded on first connect and checked by hash, and the app updates itself. 25k lines of Rust, 158 tests. The source is private; installers are public.

</details>

## Under the hood

<a href="https://github.com/Rerowros/mihomo/tree/bpn/v1.19.32">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-mihomo-dark.svg">
  <img alt="Rerowros/mihomo — network core fork" src="assets/banner-mihomo-light.svg" width="100%">
</picture>
</a>

<details>
<summary><b>The 5 patches · REALITY matrix · XHTTP benchmark</b></summary>
<br>

The network core both apps run on: an upstream [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo) tag plus five small patches, moved to each new release by rebase. Every patch has tests and a written "remove when" condition; the REALITY and XHTTP changes are also tested against a real Xray binary ([BADVPN.md](https://github.com/Rerowros/mihomo/blob/bpn/v1.19.32/BADVPN.md)).

- **P1–P4, REALITY:** current Xray client version, Firefox 148 / Safari 26.3 uTLS fingerprints, opt-in X25519MLKEM768. Without them current Xray servers reject the client. Upstream declined the version change ([#3132](https://github.com/MetaCubeX/mihomo/issues/3132)) and is waiting for uTLS 1.9.0 ([#3193](https://github.com/MetaCubeX/mihomo/issues/3193)).
- **P5, XHTTP:** uploads in packet-up mode are pipelined the way Xray does it, up to 8 requests in flight instead of one.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/mihomo-reality-dark.svg">
  <img alt="REALITY compatibility: upstream mihomo fails on Xray 26.7.28 and 26.9.9, the fork connects on all three" src="assets/mihomo-reality-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/mihomo-xhttp-dark.svg">
  <img alt="XHTTP upload at 150 ms RTT: upstream 1.8–2.4 Mbit/s, fork 11.5–13.8 Mbit/s" src="assets/mihomo-xhttp-light.svg" width="100%">
</picture>

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-product-dark.svg">
  <img alt="BPN — the service behind the apps" src="assets/banner-product-light.svg" width="100%">
</picture>

<details>
<summary><b>Architecture diagram · what's interesting in the backend</b></summary>
<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/bpn-architecture-dark.svg">
  <img alt="How BPN fits together: Telegram bot and Mini App, backend, VPN panel, clients, front node, exit node" src="assets/bpn-architecture-light.svg" width="100%">
</picture>

The service behind both apps: a Next.js + Prisma/PostgreSQL backend, a Python Telegram bot with a Mini App, a VPN panel and the nodes. Several brands run on the same backend.

- Traffic is counted on a ledger with rollover. It went live behind shadow validation, a staged rollout and fail-closed gates.
- Payments are reconciled, not taken on trust from webhooks.
- Admin actions go through an outbox, so a retry never applies twice.
- Mobile networks that only allow whitelisted destinations get front-node → exit routing.

Public pieces: [badvpn-routing](https://github.com/Rerowros/badvpn-routing) (Mihomo rulesets with source-checking CI) and [server-checker](https://github.com/Rerowros/server-checker) (VPS reachability and DPI checks).

</details>

## Open source

<a href="https://github.com/Nemu-x/ClashFest">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-clashfest-dark.svg">
  <img alt="Nemu-x/ClashFest — core contributor" src="assets/banner-clashfest-light.svg" width="100%">
</picture>
</a>

<details>
<summary><b>Highlights from 30 merged PRs</b></summary>
<br>

Open-source Android client on mihomo and the base of my own Android app. [30 merged PRs](https://github.com/Nemu-x/ClashFest/pulls?q=is%3Apr+author%3ARerowros+is%3Amerged), +19.6k lines, about 15% of today's codebase:

- Wi-Fi ↔ LTE failover that keeps DNS and the underlying network consistent ([#154](https://github.com/Nemu-x/ClashFest/pull/154))
- a mihomo config layer that preserves comments, with native Go validation ([#29](https://github.com/Nemu-x/ClashFest/pull/29)) and a YAML diff preview ([#13](https://github.com/Nemu-x/ClashFest/pull/13))
- trust-boundary hardening ([#171](https://github.com/Nemu-x/ClashFest/pull/171), [#172](https://github.com/Nemu-x/ClashFest/pull/172)) and APK update verification ([#158](https://github.com/Nemu-x/ClashFest/pull/158))
- the Material 3 redesign ([#3](https://github.com/Nemu-x/ClashFest/pull/3))

</details>

<a href="https://github.com/PasarGuard/panel">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-pasarguard-dark.svg">
  <img alt="PasarGuard — contributor" src="assets/banner-pasarguard-light.svg" width="100%">
</picture>
</a>

<details>
<summary><b>4 merged, 4 in review</b></summary>
<br>

Open-source VPN panel and node.

- merged: Mihomo xHTTP subscription options ([panel#509](https://github.com/PasarGuard/panel/pull/509)), UTC-correct API dates ([panel#208](https://github.com/PasarGuard/panel/pull/208)), share-link fix ([panel#880](https://github.com/PasarGuard/panel/pull/880)), WireGuard log timestamps ([node#47](https://github.com/PasarGuard/node/pull/47))
- in review: per-app routing and DNS editor ([panel#759](https://github.com/PasarGuard/panel/pull/759)), confirmed access revocation with node-sync fencing ([panel#756](https://github.com/PasarGuard/panel/pull/756)), node lifecycle hardening ([node#78](https://github.com/PasarGuard/node/pull/78)), atomic node updates with rollback ([scripts#25](https://github.com/PasarGuard/scripts/pull/25))

</details>

## Projects

<a href="https://github.com/Rerowros/tg-recall">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-tg-recall-dark.svg">
  <img alt="tg-recall" src="assets/banner-tg-recall-light.svg" width="100%">
</picture>
</a>

<details>
<summary><b>How it works</b></summary>
<br>

Syncs allow-listed chats into SQLite FTS5, with hybrid retrieval and local transcription. A hand-rolled MCP server lets AI agents search the archive and answers with `tg://` links back to the source messages. Read-only by design: it cannot send, edit or mark anything as read.

</details>

- [**sre-agent-bench**](https://github.com/Rerowros/sre-agent-bench) — AI agents repair a deliberately broken Ubuntu server over SSH; an external verifier checks that the fix survives SIGKILL and a reboot.
- [**wiki-mcp**](https://github.com/Rerowros/wiki-mcp) — a research wiki that agents maintain through reviewed proposal branches, served as a remote MCP server on Cloudflare Workers.

<sub>Every image here is generated from code in [`scripts/`](scripts); the activity card is re-rendered daily by GitHub Actions.</sub>
