<div align="center">
  <a href="https://jerseyfc.me">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=0891b2&height=220&section=header&text=Привет,%20я%20Ярослав&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=35" alt="Header" />
  </a>

  <h3>Full-stack product engineer для Telegram-first продуктов, AI-автоматизации, SaaS MVP и VPN-инфраструктуры</h3>

  <p>
    Помогаю фаундерам и небольшим командам превращать сырые продуктовые идеи в рабочие системы:
    Telegram-боты и mini apps, Next.js-кабинеты, Python-backend, AI workflows,
    платежи/подписки и operational tooling.
  </p>

  <p>
    Лучше всего подхожу для MVP, внутренних инструментов, automation-heavy продуктов и инфраструктурных SaaS,
    где один инженер должен понимать и бизнес-логику, и детали реализации.
  </p>

  <p>
    <a href="https://t.me/rerowros" target="_blank">
      <img src="https://img.shields.io/badge/Telegram-Обсудить_проект-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram" />
    </a>
    <a href="./featured-projects.ru.md">
      <img src="https://img.shields.io/badge/Кейсы-Избранные_проекты-0f766e?style=for-the-badge&logo=readme&logoColor=white" alt="Избранные проекты" />
    </a>
    <a href="https://jerseyfc.me">
      <img src="https://img.shields.io/badge/Website-jerseyfc.me-111827?style=for-the-badge&logo=vercel&logoColor=white" alt="Website" />
    </a>
  </p>

  <p>
    <a href="./README.ru.md">RU</a> / <a href="../README.md">EN</a>
  </p>
</div>

---

### Основные направления

- **Telegram-first продукты** — боты, Telegram Web Apps, подписки, support flows, админки, аналитика и рассылки.
- **AI-автоматизация** — structured LLM pipelines, RAG/context flows, генерация черновиков, scoring systems и human-in-the-loop tools.
- **SaaS и внутренние инструменты** — Next.js frontends, Python/FastAPI services, dashboards, платежи, интеграции и operator workflows.
- **VPN/proxy-инфраструктура** — panel integrations, node APIs, логика подписок/трафика, Mihomo/Clash routing и desktop client tooling.

### Продуктовый подход

Большая часть моей работы находится на стыке product ownership и implementation. В своём VPN-продукте **BPN / BadVPN** я веду полный product loop:

- roadmap, pricing, subscriptions, retention, support и payment reliability;
- Telegram bot, Telegram Web App/PWA, public site, admin/support tools и backend automation;
- analytics, AI-assisted support workflows, billing/referral logic и edge cases user lifecycle;
- Windows desktop client work вокруг Tauri, Rust, Mihomo, Smart Routing и zapret/winws flows.

Этот опыт особенно полезен в freelance/contract работе, где цель не просто написать код, а сделать workflow надёжным для users, operators и бизнеса.

### Избранные проекты

#### Private / Product Work

| Проект | Что я делал | Почему это важно |
|---|---|---|
| **BPN / BadVPN** | VPN-продукт, Telegram bot, TWA/PWA, public site, admin/support tooling, payments, subscriptions, analytics, routing rules | Показывает product + engineering ownership в реальном subscription business. |
| [`BPN Client`](https://github.com/Rerowros/bpn-client) | Source-available Windows-first VPN client MVP: Tauri/React UI, Rust privileged agent, Mihomo runtime, Smart Routing, zapret/winws runtime tooling | Инфраструктурный desktop-продукт с security, diagnostics, updates и routing complexity. |
| **Kwork AI Draft Bot** | Human-in-the-loop freelance automation: сканирование проектов Kwork, LLM scoring, RAG profile context, Telegram delivery черновиков, budget-safe counters | Показывает практичный AI workflow, где quality control важнее слепой автоматизации. |
| **MegaFon Support Bot** | Telegram support automation, web admin panel, address/tariff pipelines, geocoding, fuzzy search | Реальный operational workflow для support/field operations, не toy chatbot. |
| **Badass Bot** | Telegram storefront, deep-link catalog, order export, image caching, broadcasts, admin operations | E-commerce flow внутри Telegram с практичными admin-инструментами. |
| **Client Web Systems** | Astro/Payload CMS sites, catalogs, content migrations, B2B web systems | Client delivery с reusable content models и чистым handover. |

#### Public / Reviewable Work

| Repository | Focus | Stack / Domain |
|---|---|---|
| [`BadVPN Routing`](https://github.com/Rerowros/badvpn-routing) | Публичные Mihomo/Clash.Meta routing rules и subscription template для VPN users | YAML, Mihomo, Clash.Meta, automation |
| [`CareerTrack`](https://github.com/Rerowros/mtc) | Telegram-first AI career assistant: structured onboarding, vacancy ranking, explainable recommendations, companion web app | AI, Telegram, product workflows |
| [`Remoji-TG-MCP`](https://github.com/Rerowros/Remoji-tg-mcp) | MCP server для поиска Telegram emoji/stickers с browser-first auth и visual selection | MCP, browser auth, Telegram |
| [`PasarGuard Panel / Node`](https://github.com/PasarGuard/panel) | Merged upstream PRs для VPN panel/node reliability: API datetime formats, WireGuard UTC logs, Mihomo xHTTP subscription options | Python, FastAPI-style backend, VPN infrastructure |
| [`kworker`](https://github.com/Rerowros/kworker) | Forked async Kwork API client, который я использую как API layer для своего Kwork automation tooling | Python, async API clients |

#### Open Source Track

- [`PasarGuard/panel`](https://github.com/PasarGuard/panel) / [`PasarGuard/node`](https://github.com/PasarGuard/node) — merged PRs вокруг API datetime correctness ([panel #208](https://github.com/PasarGuard/panel/pull/208)), WireGuard UTC log timestamps ([node #47](https://github.com/PasarGuard/node/pull/47)) и Mihomo xHTTP subscription options ([panel #509](https://github.com/PasarGuard/panel/pull/509)).
- [`Nemu-x/ClashFest`](https://github.com/Nemu-x/ClashFest) — несколько merged PRs в Android proxy/VPN client: dashboard/routing controls, subscription import, proxy group fixes, rule-provider refresh, request history, YAML diff preview, proxy switching и centralized Mihomo YAML parsing.

### Стек

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" />

  <br/>

  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Astro-FF5D01?style=for-the-badge&logo=astro&logoColor=white" />
  <img src="https://img.shields.io/badge/Aiogram-2C5BB4?style=for-the-badge&logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/Telethon-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" />

  <br/>

  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" />
  <img src="https://img.shields.io/badge/Tauri-24C8DB?style=for-the-badge&logo=tauri&logoColor=white" />
</div>

### Как я работаю

- Предпочитаю маленькие reviewable changes вместо широких переписываний.
- Проектирую вокруг failure modes: retries, fallback paths, redacted logs, diagnostics и operator visibility.
- Думаю о business workflow за кодом: pricing, support, payments, retention и handover.
- Активно использую AI tools, но human responsibility за architecture, review, security и product judgment остаётся на мне.

### Подробнее

- [Избранные проекты](./featured-projects.ru.md)
- [English profile version](../README.md)

<br />

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Rerowros&theme=github_dark" alt="Profile Details" />
</div>

<div align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Rerowros&theme=github_dark" alt="Языки по репозиториям" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Rerowros&theme=github_dark" alt="Языки по коммитам" />
</div>
