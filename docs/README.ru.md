# Ярослав · Rerowros

Сети, устойчивые к блокировкам, прокси-клиенты для Android и десктопа, инструменты для Telegram и AI.
Веду VPN-продукт в продакшене целиком и контрибьючу в open-source, на котором он построен.

[Telegram](https://t.me/rerowros) · [EN](../README.md)

## Open source

| Проект | Что сделал |
|---|---|
| [**Nemu-x/ClashFest**](https://github.com/Nemu-x/ClashFest) · Android-клиент на mihomo · 219★ | Core contributor: [30 смёрженных PR](https://github.com/Nemu-x/ClashFest/pulls?q=is%3Apr+author%3ARerowros+is%3Amerged), +19.6k строк, ~15% текущего кода. Переключение Wi-Fi ↔ LTE с согласованными DNS и underlying network ([#154](https://github.com/Nemu-x/ClashFest/pull/154)); слой конфига mihomo с сохранением комментариев и валидацией через Go ([#29](https://github.com/Nemu-x/ClashFest/pull/29)), превью YAML-диффа ([#13](https://github.com/Nemu-x/ClashFest/pull/13)); усиление границ доверия ([#171](https://github.com/Nemu-x/ClashFest/pull/171), [#172](https://github.com/Nemu-x/ClashFest/pull/172)); проверка APK-обновлений ([#158](https://github.com/Nemu-x/ClashFest/pull/158)); редизайн на Material 3 ([#3](https://github.com/Nemu-x/ClashFest/pull/3)). |
| [**PasarGuard**](https://github.com/PasarGuard/panel) · панель + нода · 2.6k★ | Смёржено: xHTTP-опции в подписках Mihomo ([panel#509](https://github.com/PasarGuard/panel/pull/509)), даты API в UTC ([panel#208](https://github.com/PasarGuard/panel/pull/208)), share-link ([panel#880](https://github.com/PasarGuard/panel/pull/880)), время в логах WireGuard ([node#47](https://github.com/PasarGuard/node/pull/47)). На ревью: редактор маршрутизации и DNS по приложениям ([panel#759](https://github.com/PasarGuard/panel/pull/759)), подтверждаемый отзыв доступа с fencing синхронизации нод ([panel#756](https://github.com/PasarGuard/panel/pull/756)), жизненный цикл ноды ([node#78](https://github.com/PasarGuard/node/pull/78)), атомарное обновление ноды с откатом ([scripts#25](https://github.com/PasarGuard/scripts/pull/25)). |
| [**MetaCubeX/ClashMetaForAndroid**](https://github.com/MetaCubeX/ClashMetaForAndroid) | На ревью: границы локального управления ([#798](https://github.com/MetaCubeX/ClashMetaForAndroid/pull/798)), проверка Gradle-дистрибутива ([#799](https://github.com/MetaCubeX/ClashMetaForAndroid/pull/799)). |
| Другое смёрженное | Русская локализация Better Politics Mod для Victoria 3 ([#334](https://github.com/Better-Politics-Mod/Better-Politics-Mod-Vic-3/pull/334), +6k строк) · асинхронный клиент и обновление токенов в [kworker](https://github.com/Tinokil/kworker/pull/1). |

## Проекты

**[tg-recall](https://github.com/Rerowros/tg-recall)** — локальный архив Telegram для людей и AI-агентов. Синхронизирует разрешённые чаты в SQLite FTS5, гибридный поиск, локальная транскрипция, свой MCP-сервер, который отвечает со ссылками `tg://` на исходные сообщения. Python, 15k строк, 300+ тестов, CI на Windows и Linux.

**[bpn-client](https://github.com/Rerowros/bpn-client)** — десктопный VPN-клиент под Windows. Tauri UI, привилегированный сервис на Rust через IPC, Mihomo TUN, опционально zapret/winws. 25k строк Rust, 158 тестов.

**BPN / BadVPN** *(приватный, в продакшене)* — сам VPN-продукт: бэкенд на Next.js + Prisma/Postgres, Telegram-бот на Python и Mini App, несколько брендов. ~190k строк, 1.8k коммитов, 160+ тестовых файлов. Учёт трафика на леджере с переносом остатка (shadow-валидация, выкатка волнами, fail-closed гейты), сверка платежей без доверия вебхукам, идемпотентные админ-действия через outbox, маршрут front-нода → exit для ограниченных мобильных сетей. Публичные части: [badvpn-routing](https://github.com/Rerowros/badvpn-routing) (правила Mihomo с CI-проверкой источников) и [server-checker](https://github.com/Rerowros/server-checker) (проверка доступности VPS и DPI).

**[Remoji-tg-mcp](https://github.com/Rerowros/Remoji-tg-mcp)** — MCP-сервер для поиска кастомных эмодзи и стикеров Telegram, [на PyPI](https://pypi.org/project/remoji-tg-mcp/).
**[yookassa-telegram](https://github.com/Rerowros/yookassa_telegram)** — оплата ЮKassa для aiogram 3: чеки 54-ФЗ, вебхуки, возвраты, [на PyPI](https://pypi.org/project/yookassa-telegram/).

## Как работаю

AI-directed engineering: много кода пишут Claude Code и Codex, архитектура, ревью, тесты и эксплуатация — на мне. Сначала спека (OpenSpec), PR с ревью, CI-гейты.

**Стек:** Python · TypeScript · Rust · Kotlin · Go — Next.js, FastAPI, aiogram, Tauri, Android, mihomo/Xray, PostgreSQL, Cloudflare Workers.
