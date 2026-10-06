<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/header-dark.svg">
  <img alt="Ярослав · Rerowros — сети, устойчивые к блокировкам, VPN-клиенты для Android и Windows, инструменты для Telegram и AI" src="../assets/header-light.svg" width="100%">
</picture>

<p>
  <a href="https://t.me/rerowros"><img src="https://img.shields.io/badge/Telegram-@rerowros-26A5E4?logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="../README.md"><img src="https://img.shields.io/badge/README-in%20English-8b3dff" alt="README in English"></a>
</p>

Делаю и веду VPN-продукт целиком: Telegram-бот и бэкенд, приложения для Windows и Android, пропатченное ядро и серверы. Контрибьючу в open-source, на котором он построен.

## Мои приложения

### BadVPN для Android &nbsp;[![Android release](https://img.shields.io/github/v/release/Rerowros/bpn-android-releases?label=APK&logo=android&logoColor=white&color=3DDC84)](https://github.com/Rerowros/bpn-android-releases/releases/latest)

VPN-клиент для Android 6+ на [моём форке mihomo](#форк-mihomo). Подключение в одно нажатие, отдельный режим для мобильного интернета на белых списках, подписка из Telegram или по QR добавляется сама. Обновляется сам с нашего сервера. Все APK подписаны одним ключом, SHA-256 публикуется в релизе. → [**bpn-android-releases**](https://github.com/Rerowros/bpn-android-releases)

<p>
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/01-home-on.png" width="23%" alt="Главная, VPN включён">
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/06-servers.png" width="23%" alt="Как подключаться">
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/07-servers-whitelist.png" width="23%" alt="Белые списки">
  <img src="https://raw.githubusercontent.com/Rerowros/bpn-android-releases/main/screenshots/05-home-light.png" width="23%" alt="Светлая тема">
</p>

### BPN для Windows &nbsp;[![Windows release](https://img.shields.io/github/v/release/Rerowros/bpn-releases?label=installer&logo=windows&logoColor=white&color=0078D4)](https://github.com/Rerowros/bpn-releases/releases/latest)

Десктопный клиент для Windows 10/11: интерфейс на Tauri и привилегированный сервис на Rust через IPC, Mihomo TUN на моём форке ядра, опционально zapret + WinDivert для YouTube, Discord и игр. Сам скачивает компоненты, сверяет их по хешу и обновляется. 25k строк Rust, 158 тестов. → [**bpn-releases**](https://github.com/Rerowros/bpn-releases)

### Что за ними

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/bpn-architecture-dark.svg">
  <img alt="Как устроен BPN: Telegram-бот и Mini App, бэкенд на Next.js, VPN-панель, клиенты, front-нода, exit-нода" src="../assets/bpn-architecture-light.svg" width="100%">
</picture>

Сам продукт приватный: ~190k строк, 1.8k коммитов, 160+ тестовых файлов. Учёт трафика на леджере с переносом остатка: включали через shadow-валидацию, выкатку волнами и fail-closed гейты. Платежи сверяются, а не принимаются на веру по вебхукам. Админ-действия идут через outbox, поэтому идемпотентны. Для ограниченных мобильных сетей — маршрут front-нода → exit. Публичные части: [badvpn-routing](https://github.com/Rerowros/badvpn-routing) (правила Mihomo с CI-проверкой источников) и [server-checker](https://github.com/Rerowros/server-checker) (проверка доступности VPS и DPI).

## Форк mihomo

[**Rerowros/mihomo**](https://github.com/Rerowros/mihomo/tree/bpn/v1.19.32) — ядро обоих приложений: тег upstream [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo) плюс пять небольших патчей, которые переносятся ребейзом на каждый новый релиз. У каждого патча есть тесты и записанное условие «когда убрать». Правки REALITY и XHTTP дополнительно проверяются против настоящего бинаря Xray ([BADVPN.md](https://github.com/Rerowros/mihomo/blob/bpn/v1.19.32/BADVPN.md)).

- **P1–P4, REALITY:** актуальная версия клиента Xray, отпечатки uTLS Firefox 148 / Safari 26.3, X25519MLKEM768 по опции. Без них новые серверы Xray не пускают клиента. Upstream отказался менять версию ([#3132](https://github.com/MetaCubeX/mihomo/issues/3132)) и ждёт uTLS 1.9.0 ([#3193](https://github.com/MetaCubeX/mihomo/issues/3193)).
- **P5, XHTTP:** отправка в режиме packet-up идёт конвейером, как в Xray: до 8 запросов одновременно вместо одного.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/mihomo-reality-dark.svg">
  <img alt="Совместимость REALITY: upstream mihomo не подключается к Xray 26.7.28 и 26.9.9, форк — ко всем трём" src="../assets/mihomo-reality-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/mihomo-xhttp-dark.svg">
  <img alt="Отправка через XHTTP при RTT 150 мс: upstream 1,8–2,4 Мбит/с, форк 11,5–13,8 Мбит/с" src="../assets/mihomo-xhttp-light.svg" width="100%">
</picture>

## Open source

**[Nemu-x/ClashFest](https://github.com/Nemu-x/ClashFest)** · Android-клиент на mihomo · 222★ — core contributor: [30 смёрженных PR](https://github.com/Nemu-x/ClashFest/pulls?q=is%3Apr+author%3ARerowros+is%3Amerged), +19.6k строк, ~15% текущего кода.
- переключение Wi-Fi ↔ LTE с согласованными DNS и underlying network ([#154](https://github.com/Nemu-x/ClashFest/pull/154))
- слой конфига mihomo с сохранением комментариев и валидацией через Go ([#29](https://github.com/Nemu-x/ClashFest/pull/29)), превью YAML-диффа ([#13](https://github.com/Nemu-x/ClashFest/pull/13))
- усиление границ доверия ([#171](https://github.com/Nemu-x/ClashFest/pull/171), [#172](https://github.com/Nemu-x/ClashFest/pull/172)) и проверка APK-обновлений ([#158](https://github.com/Nemu-x/ClashFest/pull/158))
- редизайн на Material 3 ([#3](https://github.com/Nemu-x/ClashFest/pull/3))

## Проекты

| | |
|---|---|
| **[tg-recall](https://github.com/Rerowros/tg-recall)** | Локальный архив Telegram для людей и AI-агентов. Синхронизирует разрешённые чаты в SQLite FTS5, гибридный поиск, локальная транскрипция, свой MCP-сервер, который отвечает со ссылками `tg://` на исходные сообщения. Python, 15k строк, 300+ тестов, CI на Windows и Linux. |
| **[sre-agent-bench](https://github.com/Rerowros/sre-agent-bench)** | Бенчмарк AI-агентов, которые по SSH чинят специально сломанный Ubuntu-сервер: 11 внесённых неисправностей, запись действий через auditd, внешний верификатор проверяет, что починка переживает SIGKILL и перезагрузку. Результаты для 11 конфигураций моделей. |
| **[wiki-mcp](https://github.com/Rerowros/wiki-mcp)** | Исследовательская вики, которую ведут агенты, как удалённый MCP-сервер на Cloudflare Workers: OAuth 2.1 для claude.ai/ChatGPT, D1 + KV, запись через proposal-ветки с мержем только после CI-проверки схемы. Качество поиска на эталонном наборе (recall@5 0.83 на вики из 536 страниц). |
| **[lumacalc](https://github.com/Rerowros/lumacalc)** | Нативный калькулятор под Windows на Rust + Slint: чистый крейт-движок без `unsafe`, тонкий слой Win32, clippy pedantic, установка без прав админа. |
| **[Remoji-tg-mcp](https://github.com/Rerowros/Remoji-tg-mcp)** | MCP-сервер для поиска кастомных эмодзи и стикеров Telegram, [на PyPI](https://pypi.org/project/remoji-tg-mcp/). |
| **[yookassa-telegram](https://github.com/Rerowros/yookassa_telegram)** | Оплата ЮKassa для aiogram 3: чеки 54-ФЗ, вебхуки, возвраты, [на PyPI](https://pypi.org/project/yookassa-telegram/). |

## Ещё контрибьючу

**[PasarGuard](https://github.com/PasarGuard/panel)** · панель + нода · 2.6k★
- смёржено: xHTTP-опции в подписках Mihomo ([panel#509](https://github.com/PasarGuard/panel/pull/509)), даты API в UTC ([panel#208](https://github.com/PasarGuard/panel/pull/208)), share-link ([panel#880](https://github.com/PasarGuard/panel/pull/880)), время в логах WireGuard ([node#47](https://github.com/PasarGuard/node/pull/47))
- на ревью: редактор маршрутизации и DNS по приложениям ([panel#759](https://github.com/PasarGuard/panel/pull/759)), подтверждаемый отзыв доступа с fencing синхронизации нод ([panel#756](https://github.com/PasarGuard/panel/pull/756)), жизненный цикл ноды ([node#78](https://github.com/PasarGuard/node/pull/78)), атомарное обновление ноды с откатом ([scripts#25](https://github.com/PasarGuard/scripts/pull/25))

## Стек

<p>
  <img src="https://skillicons.dev/icons?i=py,ts,rust,kotlin,go,nextjs,fastapi,tauri,androidstudio,postgres,prisma,cloudflare,linux&perline=13" alt="Python, TypeScript, Rust, Kotlin, Go, Next.js, FastAPI, Tauri, Android, PostgreSQL, Prisma, Cloudflare, Linux">
</p>

Python · TypeScript · Rust · Kotlin · Go — Next.js, FastAPI, aiogram, Tauri, Android, mihomo/Xray, PostgreSQL, Cloudflare Workers.
