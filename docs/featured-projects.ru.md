# Избранные проекты

Расширенные описания проектов из профильного README.

Приватные кейсы описаны на уровне продукта — цель показать, какие системы я строю, без публикации внутренней структуры репозиториев.

---

## BadVPN

Приватная production-платформа.

**Что делает:**
Полноценный VPN-продукт вокруг Telegram и web — подписки, платежи, рефералка, поддержка и аналитика трафика в одном домене.

**Что выделяет:**
- Multi-auth модель с привязкой аккаунтов через Telegram и web.
- AI-поддержка поверх богатой доменной схемы.
- Отдельная логика для биллинга, подписок, реферальных выплат и операций поддержки.
- Product ownership не только на уровне кода: roadmap, pricing, retention, support workflows, payment reliability и operational analytics.
- Telegram bot + Telegram Web App/PWA + public site + admin/support surfaces вокруг одного продуктового цикла.
- Практичные интеграции вокруг payment reconciliation, proxy subscription lifecycle, SEO/content surfaces и operator dashboards.

**Почему релевантно клиентам:**
Если продукту нужен человек, который видит user flows, backend logic, payments, support и operational dashboards как одну систему, это самый близкий пример моего рабочего мышления.

---

## BPN Client

Source-available active MVP: [Rerowros/bpn-client](https://github.com/Rerowros/bpn-client)

**Что делает:**
Windows-first desktop VPN client вокруг subscription workflow, Mihomo runtime, privileged service control, diagnostics и будущих bypass tooling сценариев.

**Что выделяет:**
- Tauri 2 desktop UI на React и TypeScript.
- Rust privileged service и IPC-oriented architecture для операций, которые не должны жить внутри UI process.
- Mihomo/Clash runtime integration, TUN routing direction, Smart Routing и optional zapret/winws tooling.
- Product-level внимание к policy summaries, diagnostics, runtime resources, update flows и понятной visibility для operator/user.

**Почему релевантно клиентам:**
Хорошее доказательство для infrastructure-adjacent desktop products, где одновременно важны UX, security boundaries, runtime packaging и низкоуровневые networking details.

---

## BadVPN Routing

Публичный репозиторий: [Rerowros/badvpn-routing](https://github.com/Rerowros/badvpn-routing)

**Что делает:**
Публичные Mihomo/Clash.Meta routing rules и subscription templates вокруг BadVPN/BPN ecosystem.

**Что выделяет:**
- Rule providers для типовых split-routing сценариев: YouTube/Discord, AI services, Telegram, GitHub, games, RU direct routing и torrents.
- Validation/scripts вокруг upstream sources и export flows.
- Чёткое разделение между приватной коммерческой платформой и публичными routing assets, которые можно inspect/review.

**Почему релевантно клиентам:**
Показывает ту часть VPN-работы, которую легко недооценить: поддерживаемые конфиги, предсказуемое routing behavior и правила, которые можно debug.

---

## MegaFon Support Bot

Приватная production-автоматизация.

**Что делает:**
Поддержка клиентов и приём заявок через Telegram-бот и web-admin: поиск адресов, обновление тарифов, внутренние операционные сценарии.

**Что выделяет:**
- Связка `Telethon` и `Flask` внутри одного рабочего инструмента.
- Геокодинг и fuzzy-поиск адресов для шумных реальных данных.
- Внятный deploy/setup-процесс, а не только локальная разработка.

---

## Badass Bot

Приватный продукт.

**Что делает:**
Telegram-магазин с каталогом, заказами и сценариями поддержки.

**Что выделяет:**
- Deep-link навигация прямо в товары и категории.
- Кеширование изображений — без повторной загрузки медиа в Telegram.
- Admin-сценарии для экспорта, рассылок и смены платёжных реквизитов.

---

## Kwork AI Draft Bot

Приватный/local automation project.

**Что делает:**
Сканирует новые проекты Kwork, дедуплицирует их, просит LLM решить, стоит ли тратить внимание на отклик, генерирует персональный черновик и отправляет компактную карточку в Telegram.

**Что выделяет:**
- Human-in-the-loop by design: бот готовит drafts/recommendations, а не слепо отправляет отклики.
- SQLite storage для seen projects, decisions, draft history, delivery status и monthly/daily recommendation counters.
- RAG layer поверх curated profile/project knowledge, чтобы отклики ссылались на релевантный опыт без вставки всего профиля в каждый prompt.
- Private estimate block только для Telegram: часы, price range, confidence и reasoning не попадают в публичный отклик без необходимости.

**Почему релевантно клиентам:**
Хороший пример практичной AI automation: structured outputs, safety limits, budget-aware behavior и operator review перед необратимыми действиями.

---

## CareerTrack

Публичный репозиторий: [Rerowros/mtc](https://github.com/Rerowros/mtc)

**Что делает:**
Telegram-first AI-карьерный ассистент с companion web app: онбординг, структурированный профиль пользователя, ранжирование вакансий и объяснение рекомендаций.

**Что выделяет:**
- Contract-first профиль вместо полностью свободного AI-вывода.
- Детерминированная оркестрация с role-based роутингом и fallback-ветками.
- Гибридный онбординг: сначала conversational flow, затем structured fallback.

---

## Remoji-TG-MCP

Публичный репозиторий: [Rerowros/Remoji-tg-mcp](https://github.com/Rerowros/Remoji-tg-mcp)

**Что делает:**
MCP-совместимые AI-клиенты получают доступ к поиску Telegram stickers и custom emoji.

**Что выделяет:**
- Browser-based auth — не нужно настраивать через терминал.
- Визуальный выбор emoji и стикеров.
- Параллельный поиск и скачивание с изолированным локальным хранением.

---

## PasarGuard Panel / Node Contribution Track

Upstream-репозитории: [PasarGuard/panel](https://github.com/PasarGuard/panel), [PasarGuard/node](https://github.com/PasarGuard/node)

**Что это:**
Open-source VPN panel/node work вокруг надёжности и operational correctness.

**На чём фокус:**
- API datetime correctness и subscription option correctness.
- UTC log timestamp correctness в node-side WireGuard flows.
- Небольшие изменения, которые легко ревьюить maintainers, вместо широких переписываний.

**Публичный сигнал:**
Есть merged upstream PR work вроде API datetime-format fixes ([panel #208](https://github.com/PasarGuard/panel/pull/208)), WireGuard UTC log timestamps ([node #47](https://github.com/PasarGuard/node/pull/47)) и Mihomo xHTTP subscription option support ([panel #509](https://github.com/PasarGuard/panel/pull/509)).

---

## ClashFest Contribution Track

Upstream-репозиторий: [Nemu-x/ClashFest](https://github.com/Nemu-x/ClashFest)

**Что это:**
Android proxy/VPN client work вокруг Clash/mihomo behavior и совместимости конфигов.

**На чём фокус:**
- Reproducible fixtures и compatibility notes.
- Анализ поведения mihomo/Clash.
- Маленькие upstream-friendly changes вместо шумных fork-only edits.
- Dashboard/routing controls, subscription import behavior, proxy group fixes, rule-provider refresh, request history, YAML diff preview, proxy switching и centralized Mihomo YAML parsing.

**Публичный сигнал:**
Это один из самых сильных публичных contribution tracks: несколько merged upstream PRs в Android proxy/VPN client, без claim ownership оригинального приложения. Примеры: [#3](https://github.com/Nemu-x/ClashFest/pull/3), [#4](https://github.com/Nemu-x/ClashFest/pull/4), [#6](https://github.com/Nemu-x/ClashFest/pull/6), [#7](https://github.com/Nemu-x/ClashFest/pull/7), [#8](https://github.com/Nemu-x/ClashFest/pull/8), [#9](https://github.com/Nemu-x/ClashFest/pull/9), [#11](https://github.com/Nemu-x/ClashFest/pull/11), [#12](https://github.com/Nemu-x/ClashFest/pull/12), [#13](https://github.com/Nemu-x/ClashFest/pull/13), [#14](https://github.com/Nemu-x/ClashFest/pull/14), [#15](https://github.com/Nemu-x/ClashFest/pull/15), [#29](https://github.com/Nemu-x/ClashFest/pull/29).

---

## kworker

Публичный репозиторий: [Rerowros/kworker](https://github.com/Rerowros/kworker)

**Что делает:**
Async Python-клиент для API Kwork.

**Что выделяет:**
- Практичный асинхронный интерфейс для ограниченного внешнего API.
- Полезен как API layer для higher-level automation: project scanning, draft generation и Telegram review workflows.

**Почему релевантно клиентам:**
Показывает опыт упаковки limited/unofficial APIs в higher-level automation workflows.

---

## Headless Commerce и B2B CMS

Приватная клиентская работа.

**Что делает:**
Storefront-сайты, каталоги и маркетинговые системы на Astro и Payload CMS.

**Что выделяет:**
- Переиспользуемые content models для товаров, статей и lead capture.
- Миграции с legacy-стеков в чистую headless-архитектуру.
- Показывает, что я одинаково уверенно двигаюсь и в product engineering, и в client delivery.

---

## Правило отбора

В профильный README попадают:

- проекты с сильной архитектурой и реальными бизнес-сценариями,
- публичные инструменты, которые показывают мой стиль разработки,
- приватные системы, которые безопасно описывать на уровне продукта.
- open-source contribution tracks, где работа reviewable и связана с VPN/proxy-инфраструктурой.

Не попадают: тонкие утилиты, старые учебные проекты, пустые репозитории, форки без личного вклада.
