from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Етапи опитування
NAME, CITY_FROM, CITY_NOW, OCCUPATION, REASON, CRIMEA, USERNAME = range(7)

# Підключення до Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)  # Файл JSON має бути поряд
client = gspread.authorize(creds)
sheet = client.open("Nomad Applications").sheet1  # Назва таблиці

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "привіт! заповни коротку заявку — ми переглянемо її з турботою і якнайшвидше надішлемо запрошення в чат, якщо все збігається :) 🪿\n\n"
        "The Nomád Circle — це простір для свідомих українців, які цінують культуру, важливі сенси і взаємну підтримку 🪢\n\n"
        "тут ти зможеш знайти творчі колаборації, хостинг у Європі та світі або корисні поради від українців за кордоном 📨"
    )
    keyboard = [[InlineKeyboardButton("стати частиною спільноти 🍽️", callback_data="join")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Обробка кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("заявка коротка, але дуже важлива для нас — дякуємо за приділені пару хвилин 🫂")
    await query.message.reply_text("1. як тебе звати?")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("2. з якого ти міста?")
    return CITY_FROM

async def get_city_from(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["city_from"] = update.message.text
    await update.message.reply_text("3. в якому місті живеш зараз?")
    return CITY_NOW

async def get_city_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["city_now"] = update.message.text
    await update.message.reply_text("4. чим ти займаєшся?")
    return OCCUPATION

async def get_occupation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["occupation"] = update.message.text
    await update.message.reply_text("5. чому хочеш приєднатись до The Nomád Circle?")
    return REASON

async def get_reason(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["reason"] = update.message.text
    await update.message.reply_text("6. чий Крим?")
    return CRIMEA

async def get_crimea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["crimea"] = update.message.text
    await update.message.reply_text("7. введи свій telegram username для подальшого звʼязку📡")
    return USERNAME

async def get_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["username"] = update.message.text
    
    # Зберігаємо в таблицю
    sheet.append_row([
        context.user_data["name"],
        context.user_data["city_from"],
        context.user_data["city_now"],
        context.user_data["occupation"],
        context.user_data["reason"],
        context.user_data["crimea"],
        context.user_data["username"]
    ])
    
    await update.message.reply_text(
        "дякуємо за щирі відповіді!\n"
        "ми переглянемо заявку з турботою і надішлемо запрошення найближчим часом 📩\n\n"
        "Слава Україні!"
    )
    return ConversationHandler.END

# Завершення
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Опитування скасовано.")
    return ConversationHandler.END

# Основна функція
def main():
    app = ApplicationBuilder().token("7548553265:AAHO7oIvX-kXlxVtO0aniAhkxE5vP68m3JA").build()

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button, pattern="join")],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            CITY_FROM: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city_from)],
            CITY_NOW: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city_now)],
            OCCUPATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_occupation)],
            REASON: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_reason)],
            CRIMEA: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_crimea)],
            USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_username)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)

    print("Бот запущено!")
    app.run_polling()

if __name__ == "__main__":
    main()
