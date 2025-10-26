# Jabber Fake Checker Bot

Telegram бот для проверки Jabber ID на наличие кириллических символов.

## Проблема

Кидалы используют кириллические символы в Jabber ID, которые визуально неотличимы от латинских:

- `user@jabber.ru` - латиница
- `usеr@jabber.ru` - русская **е** (совершенно другой Jabber!)

## Функционал

- Проверка любого Jabber ID на кириллицу
- Визуальное выделение подозрительных символов
- Указание позиций и похожих латинских символов
- Быстрая обработка без задержек

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repo-url>
cd jabber-fake-checker
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env`:
```bash
cp .env.example .env
```

4. Получите токен бота от [@BotFather](https://t.me/BotFather) и добавьте в `.env`:
```
BOT_TOKEN=ваш_токен_здесь
```

## Запуск

```bash
python bot.py
```

## Использование

1. Запустите бота командой `/start`
2. Отправьте Jabber ID для проверки
3. Получите результат с выделением кириллицы

## Структура проекта

```
.
├── bot.py                 # Точка входа
├── config.py              # Конфигурация
├── handlers/              # Обработчики команд
│   ├── commands.py
│   └── checker.py
├── utils/                 # Утилиты
│   └── jabber_checker.py
├── requirements.txt
└── README.md
```

## Технологии

- Python 3.11+
- aiogram 3.x
- asyncio

## Лицензия

MIT

