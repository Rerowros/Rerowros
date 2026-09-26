# Iaroslav · Rerowros

Engineer working on censorship-resistant networking, Android/desktop proxy clients and Telegram/AI tooling.
I run a production VPN product end to end and contribute upstream to the open-source stack it is built on.

[Telegram](https://t.me/rerowros) · [RU](./docs/README.ru.md)

## Open source

| Project | What I did |
|---|---|
| [**Nemu-x/ClashFest**](https://github.com/Nemu-x/ClashFest) · Android client on mihomo · 219★ | Core contributor: [30 merged PRs](https://github.com/Nemu-x/ClashFest/pulls?q=is%3Apr+author%3ARerowros+is%3Amerged), +19.6k LOC, ~15% of the current codebase. Wi-Fi ↔ LTE failover with consistent DNS/underlying network ([#154](https://github.com/Nemu-x/ClashFest/pull/154)); comment-preserving mihomo config layer with native Go validation ([#29](https://github.com/Nemu-x/ClashFest/pull/29)) and YAML diff preview ([#13](https://github.com/Nemu-x/ClashFest/pull/13)); trust-boundary hardening ([#171](https://github.com/Nemu-x/ClashFest/pull/171), [#172](https://github.com/Nemu-x/ClashFest/pull/172)); APK update verification ([#158](https://github.com/Nemu-x/ClashFest/pull/158)); Material 3 redesign ([#3](https://github.com/Nemu-x/ClashFest/pull/3)). |
| [**PasarGuard**](https://github.com/PasarGuard/panel) · VPN panel + node · 2.6k★ | Merged: Mihomo xHTTP subscription options ([panel#509](https://github.com/PasarGuard/panel/pull/509)), UTC-correct API dates ([panel#208](https://github.com/PasarGuard/panel/pull/208)), share-link fix ([panel#880](https://github.com/PasarGuard/panel/pull/880)), WireGuard log timestamps ([node#47](https://github.com/PasarGuard/node/pull/47)). In review: per-app routing & DNS editor ([panel#759](https://github.com/PasarGuard/panel/pull/759)), confirmed access revocation with node-sync fencing ([panel#756](https://github.com/PasarGuard/panel/pull/756)), node lifecycle hardening ([node#78](https://github.com/PasarGuard/node/pull/78)), atomic node updates with rollback ([scripts#25](https://github.com/PasarGuard/scripts/pull/25)). |
| [**MetaCubeX/ClashMetaForAndroid**](https://github.com/MetaCubeX/ClashMetaForAndroid) | In review: local control boundary hardening ([#798](https://github.com/MetaCubeX/ClashMetaForAndroid/pull/798)), Gradle distribution verification ([#799](https://github.com/MetaCubeX/ClashMetaForAndroid/pull/799)). |
| Other merged | Russian localization for Better Politics Mod, Victoria 3 ([#334](https://github.com/Better-Politics-Mod/Better-Politics-Mod-Vic-3/pull/334), +6k lines) · async client and token refresh for [kworker](https://github.com/Tinokil/kworker/pull/1). |

## Projects

**[tg-recall](https://github.com/Rerowros/tg-recall)** — local-first Telegram archive for people and AI agents. Syncs allow-listed chats into SQLite FTS5, hybrid retrieval, local transcription, hand-rolled MCP server that answers with `tg://` source links. Python, 15k LOC, 300+ tests, CI on Windows and Linux.

**[bpn-client](https://github.com/Rerowros/bpn-client)** — Windows-first desktop VPN client. Tauri UI, privileged Rust service over IPC, Mihomo TUN, optional zapret/winws DPI tooling. 25k LOC Rust, 158 tests.

**BPN / BadVPN** *(private, in production)* — the VPN product itself: Next.js + Prisma/Postgres backend, Python Telegram bot and Mini App, multi-brand. ~190k LOC, 1.8k commits, 160+ test files. Traffic accounting on a ledger with rollover (shadow validation, staged rollout, fail-closed gates), payment reconciliation that does not trust webhooks, idempotent admin actions via outbox, front-node → exit routing for restricted mobile networks. Public pieces: [badvpn-routing](https://github.com/Rerowros/badvpn-routing) (Mihomo rulesets with source-checking CI) and [server-checker](https://github.com/Rerowros/server-checker) (VPS reachability and DPI checks).

**[sre-agent-bench](https://github.com/Rerowros/sre-agent-bench)** — benchmark of AI coding agents repairing a deliberately broken Ubuntu server over SSH: 11 injected faults (service, creds, proxy, DB exposure, backups, restart policy), auditd action capture, an external verifier that checks survival after SIGKILL and reboot. Results for 11 model/harness configurations.

**[wiki-mcp](https://github.com/Rerowros/wiki-mcp)** — agent-maintained research wiki served as a remote MCP server on Cloudflare Workers: OAuth 2.1 for claude.ai/ChatGPT, D1 + KV, agents write through proposal branches that merge only after a schema-lint CI gate, retrieval tracked against a golden set (recall@5 0.83 on the private 536-page instance).

**[lumacalc](https://github.com/Rerowros/lumacalc)** — native Windows calculator in Rust + Slint: pure engine crate with `unsafe` forbidden, thin Win32 platform layer, clippy pedantic, per-user install.

**[Remoji-tg-mcp](https://github.com/Rerowros/Remoji-tg-mcp)** — MCP server for finding Telegram custom emoji and stickers, [on PyPI](https://pypi.org/project/remoji-tg-mcp/).
**[yookassa-telegram](https://github.com/Rerowros/yookassa_telegram)** — YooKassa payments for aiogram 3: fiscal receipts, webhooks, refunds, [on PyPI](https://pypi.org/project/yookassa-telegram/).

## How I work

AI-directed engineering: Claude Code and Codex write a lot of the code; I own the architecture, review, tests and production operations. Specs first (OpenSpec), reviewed PRs, CI gates.

**Stack:** Python · TypeScript · Rust · Kotlin · Go — Next.js, FastAPI, aiogram, Tauri, Android, mihomo/Xray, PostgreSQL, Cloudflare Workers.
