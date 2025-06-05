
README: Telegram бот + Google Sheets інтеграція

1. Створи Google Таблицю з назвою "Nomad Applications"
   Колонки (перший рядок): name, from, where, occupation, reason, Crimea

2. Створи Google Cloud Project:
   - Перейди: https://console.cloud.google.com
   - Увімкни Google Sheets API
   - Створи Service Account (тип: JSON)
   - Завантаж credentials.json і заміни ним шаблон

3. Поділись таблицею з email сервісного акаунта (Editor-доступ)

4. Встанови бібліотеки:
   pip install python-telegram-bot==20.7 gspread oauth2client

5. У файлі nomad_bot.py:
   - заміни "YOUR_BOT_TOKEN_HERE" на токен бота

6. Запусти бота:
   python nomad_bot.py

Готово!
