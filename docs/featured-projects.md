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

## PasarGuard Node Bridge

Public repository: [Rerowros/node_bridge_py](https://github.com/Rerowros/node_bridge_py)

**What it does:**
Connects Python services to PasarGuard node infrastructure over gRPC and REST.

**What sets it apart:**
- Fully async API surface.
- Shared node and user abstractions across transport types.
- Chunked sync for large user batches instead of one oversized request.

---

## kworker

Public repository: [Rerowros/kworker](https://github.com/Rerowros/kworker)

**What it does:**
Async Python client for the Kwork API.

**What sets it apart:**
- Package-oriented design — reusable library, not project-local glue code.
- Practical async interface around a closed or limited-access API.

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

Left out: thin utilities, old coursework, empty repositories, forks that don't represent my main product work.
