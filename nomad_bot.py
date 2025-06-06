from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Етапи опитування
NAME, CITY_FROM, CITY_NOW, OCCUPATION, REASON, CRIMEA, USERNAME = range(7)

# Підключення до Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_dict = json.loads(os.environ['GOOGLE_CREDS_JSON'])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gs = gspread.authorize(creds)
sheet = gs.open("Nomad Applications").sheet1  # Назва таблиці

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Привіт! Заповни коротку заявку — ми переглянемо її з турботою і якнайшвидше надішлемо запрошення в чат, якщо все збігається :) \n\n"
        "The Nomád Circle — це простір для свідомих українців, які цінують культуру, важливі сенси і взаємну підтримку 💭\n\n"
    )
    await update.message.reply_text(welcome_text)
