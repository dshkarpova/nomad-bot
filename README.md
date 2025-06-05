# The Nomád Circle Telegram Bot

Цей бот збирає анкети учасників для спільноти **The Nomád Circle** — простору для свідомих українців за кордоном 🪿

## 🔍 Що робить бот:
- Надсилає вітальне повідомлення з кнопкою
- Запускає опитування з 7 питань
- Зберігає відповіді у Google Sheets

## 🚀 Як запустити локально

1. Встанови залежності:
```
pip install -r requirements.txt
```

2. Поклади свій `credentials.json` файл у цю ж папку (ключ Google Sheets).

3. Запусти бота:
```
python3 nomad_bot.py
```

## ☁️ Деплой на Render

- Тип сервісу: **Background Worker**
- Команда запуску:
```
python3 nomad_bot.py
```

## 📁 Структура проєкту
```
nomad_bot.py
credentials.json
requirements.txt
README.md
```

## 🧵 Авторка
**Dasha Karpova**

Instagram: [@thenomad_media](https://www.instagram.com/thenomad_media/)