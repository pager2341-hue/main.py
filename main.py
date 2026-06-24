import logging
import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = '8954961595:AAGXCHXe32wB1DRQeNwqJONoz65nB2z286U'
ADMIN_ID = '8708515019' # အစ်ကို့ရဲ့ Telegram ID ကို ဒီမှာ ထည့်ပါ

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    # ၁။ User ကို ပြန်ပြောမယ့် message
    welcome_text = (
        f"👋 မင်္ဂလာပါ {user.full_name}!\n\n"
        "🇯🇵 TikTok Japan Account နှင့် Monetization ဝန်ဆောင်မှုများအတွက် "
        "အဆင်သင့်ရှိပါသည်။\n\n"
        "ဆက်သွယ်ရန်: @thant12450\n"
        "⏰ လုပ်ငန်းချိန်: (3:00 PM - 11:00 PM)\n"
        "⚠️ ငွေမပေးချေမီ Video Call (VC) ခေါ်၍ အတည်ပြုနိုင်ပါသည်။"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)

    # ၂။ အစ်ကို့ဆီကို User အချက်အလက် ပို့မယ့် message
    admin_notify = (
        f"🔔 *New User Found!*\n\n"
        f"Name: {user.full_name}\n"
        f"ID: `{user.id}`\n"
        f"Username: @{user.username}"
    )
    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_notify, parse_mode='Markdown')

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.start()

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("✅ Bot နှင့် Web Server စတင် အလုပ်လုပ်နေပြီ...")
    application.run_polling()
    
