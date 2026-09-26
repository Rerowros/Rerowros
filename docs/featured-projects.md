# Featured Projects

Extended write-ups for the projects listed in the profile README.

Private work is described at the product level by design — the goal is to show what kind of systems I build without turning internal repository structure into public documentation.

---

## BadVPN

Private production platform.

**What it does:**
Builds a complete VPN product around Telegram and the web — covering subscriptions, payments, referrals, support, and traffic analytics within a single domain.

**What sets it apart:**
- Multi-auth model with Telegram and web account linking.
- AI-assisted support flow backed by a rich domain schema.
- Cleanly separated billing, subscription, referral payout, and support logic.
- Product ownership beyond code: roadmap, pricing, retention, support workflows, payment reliability, and operational analytics.
- Telegram bot + Telegram Web App/PWA + public site + admin/support surfaces built around the same product loop.
- Practical integration work around payment reconciliation, proxy subscription lifecycle, SEO/content surfaces, and operator dashboards.

**Relevant for clients:**
If your product needs one person to reason across user flows, backend logic, payments, support, and operational dashboards, this is the closest match to how I think and work.

---

## BPN Client

Source-available active MVP: [Rerowros/bpn-client](https://github.com/Rerowros/bpn-client)

**What it does:**
Builds a Windows-first desktop VPN client around a subscription workflow, Mihomo runtime, privileged service control, diagnostics, and future bypass tooling.

**What sets it apart:**
- Tauri 2 desktop UI with React and TypeScript.
- Rust privileged service and IPC-oriented architecture for operations that should not live in the UI process.
- Mihomo/Clash runtime integration, TUN routing direction, Smart Routing, and optional zapret/winws tooling.
- Product-level attention to policy summaries, diagnostics, runtime resources, update flows, and safer operator/user visibility.

**Relevant for clients:**
Good evidence for infrastructure-adjacent desktop products where UX, security boundaries, runtime packaging, and lower-level networking details all matter.

---

## BadVPN Routing

Public repository: [Rerowros/badvpn-routing](https://github.com/Rerowros/badvpn-routing)

**What it does:**
Maintains public Mihomo/Clash.Meta routing rules and subscription templates used around the BadVPN/BPN ecosystem.

**What sets it apart:**
- Rule providers for common VPN split-routing needs such as YouTube/Discord, AI services, Telegram, GitHub, games, RU direct routing, and torrents.
- Validation/scripts around upstream sources and export flows.
- Clear separation between the private commercial platform and public routing assets that users can inspect.

**Relevant for clients:**
Shows the part of VPN work that is easy to underestimate: maintainable configuration, predictable routing behavior, and rules that operators can debug.

---

## MegaFon Support Bot

Private production automation system.

**What it does:**
Handles customer support and request intake through a Telegram bot paired with a web admin panel, including address lookup, tariff updates, and staff-facing workflows.

**What sets it apart:**
- Combines `Telethon` and `Flask` in a single operational toolchain.
- Geocoding plus fuzzy address matching for messy real-world input.
- Production-ready deployment flow, not just a local demo.

---

## Badass Bot

Private product.

**What it does:**
Runs a Telegram storefront with catalog navigation, order management, and support flows.

**What sets it apart:**
- Deep-link navigation directly into products and categories.
- Image caching to avoid repeated Telegram media uploads.
- Admin flows for exports, broadcasting, and payment detail updates.

---

## Kwork AI Draft Bot

Private/local automation project.

**What it does:**
Scans new Kwork projects, deduplicates them, asks an LLM to decide whether a reply is worth spending attention on, generates a personalized draft, and sends a compact review card to Telegram.

**What sets it apart:**
- Human-in-the-loop by design: it prepares drafts and recommendations instead of blindly sending replies.
- SQLite storage for seen projects, decisions, draft history, delivery status, and monthly/daily recommendation counters.
- RAG layer over curated profile/project knowledge so replies can reference relevant experience without dumping the whole profile into every prompt.
- Private estimate block for Telegram only: hours, price range, confidence, and reasoning stay out of the public reply unless explicitly needed.

**Relevant for clients:**
Good example of practical AI automation: structured outputs, safety limits, budget-aware behavior, and operator review before irreversible actions.

---

## CareerTrack

Public repository: [Rerowros/mtc](https://github.com/Rerowros/mtc)

**What it does:**
Telegram-first AI career assistant with a companion web app. Guides onboarding, builds a structured user profile, ranks vacancies, and explains every recommendation.

**What sets it apart:**
- Contract-first profile model instead of free-form AI output.
- Deterministic orchestration with role-based AI routing and fallback paths.
- Hybrid onboarding: conversational flow first, structured fallback when needed.

---

## Remoji-TG-MCP

Public repository: [Rerowros/Remoji-tg-mcp](https://github.com/Rerowros/Remoji-tg-mcp)

**What it does:**
Lets MCP-compatible AI clients search Telegram stickers and custom emoji.

**What sets it apart:**
- Browser-based auth flow instead of terminal-only setup.
- Visual picker for sticker and emoji selection.
- Parallel search and download with isolated local data storage.

---

## PasarGuard Panel / Node Contribution Track

Upstream repositories: [PasarGuard/panel](https://github.com/PasarGuard/panel), [PasarGuard/node](https://github.com/PasarGuard/node)

**What it is:**
Open-source VPN panel/node work focused on reliability and operational correctness.

**What I focus on:**
- API datetime correctness and subscription option correctness.
- UTC log timestamp correctness in node-side WireGuard flows.
- Changes that are easy for maintainers to review instead of broad rewrites.

**Public signal:**
Includes merged upstream PR work such as API datetime-format fixes ([panel #208](https://github.com/PasarGuard/panel/pull/208)), WireGuard UTC log timestamps ([node #47](https://github.com/PasarGuard/node/pull/47)), and Mihomo xHTTP subscription option support ([panel #509](https://github.com/PasarGuard/panel/pull/509)).

---

## ClashFest Contribution Track

Upstream repository: [Nemu-x/ClashFest](https://github.com/Nemu-x/ClashFest)

**What it is:**
Android proxy/VPN client work around Clash/mihomo behavior and configuration compatibility.

**What I focus on:**
- Reproducible fixtures and compatibility notes.
- Analysis around mihomo/Clash behavior.
- Small upstream-friendly changes rather than noisy fork-only edits.
- Dashboard/routing controls, subscription import behavior, proxy group fixes, rule-provider refresh, request history, YAML diff preview, proxy switching, and centralized Mihomo YAML parsing.

**Public signal:**
This is currently one of the strongest public contribution tracks: multiple merged upstream PRs in an Android proxy/VPN client, without claiming ownership of the original app. Examples include [#3](https://github.com/Nemu-x/ClashFest/pull/3), [#4](https://github.com/Nemu-x/ClashFest/pull/4), [#6](https://github.com/Nemu-x/ClashFest/pull/6), [#7](https://github.com/Nemu-x/ClashFest/pull/7), [#8](https://github.com/Nemu-x/ClashFest/pull/8), [#9](https://github.com/Nemu-x/ClashFest/pull/9), [#11](https://github.com/Nemu-x/ClashFest/pull/11), [#12](https://github.com/Nemu-x/ClashFest/pull/12), [#13](https://github.com/Nemu-x/ClashFest/pull/13), [#14](https://github.com/Nemu-x/ClashFest/pull/14), [#15](https://github.com/Nemu-x/ClashFest/pull/15), and [#29](https://github.com/Nemu-x/ClashFest/pull/29).

---

## kworker

Public repository: [Rerowros/kworker](https://github.com/Rerowros/kworker)

**What it does:**
Async Python client for the Kwork API.

**What sets it apart:**
- Practical async interface around a closed or limited-access API.
- Useful as the API layer for higher-level automation such as project scanning, draft generation, and Telegram review workflows.

**Relevant for clients:**
Shows experience wrapping limited or unofficial APIs into higher-level automation workflows.

---

## Headless Commerce and B2B CMS Work

Private client work.

**What it does:**
Delivers storefronts, catalog sites, and marketing systems built on Astro and Payload CMS.

**What sets it apart:**
- Reusable content models for products, articles, and lead capture.
- Migration paths from legacy stacks into a clean headless setup.
- Demonstrates that I move between product engineering and client delivery without changing engineering standards.

---

## Selection Rule

The profile README stays focused on:

- Projects with strong architecture and real business workflows.
- Public tools that reveal something distinctive about how I build.
- Private systems that can be described clearly at the product level.
- Open-source contribution tracks where the work is reviewable and relevant to VPN/proxy infrastructure.

Left out: thin utilities, old coursework, empty repositories, forks that don't represent my main product work.
