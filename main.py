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

# Bot Token (Environment Variable မှာ ထည့်ထားရင် ပိုကောင်းပါတယ်)
TOKEN = '8954961595:AAGXCHXe32wB1DRQeNwqJONoz65nB2z286U'

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"👋 မင်္ဂလာပါ {user.full_name}\n\n"
             "ဝန်ဆောင်မှုများအတွက် @thant12450 ထံ ဆက်သွယ်နိုင်ပါသည်။\n"
             "⏰ လုပ်ငန်းချိန်: (3:00 PM - 11:00 PM)\n"
             "⚠️ ငွေမပေးချေမီ Video Call (VC) ခေါ်၍ အတည်ပြုနိုင်ပါသည်။"
    )

# Flask Web Server setup (Render အတွက်)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # 1. Flask server ကို Background မှာ run ပါ
    t = Thread(target=run_flask)
    t.start()

    # 2. Telegram Bot application တည်ဆောက်ပါ
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("✅ Bot နှင့် Web Server စတင် အလုပ်လုပ်နေပြီ...")
    
    # 3. Bot ကို Polling စနစ်ဖြင့် run ပါ
    application.run_polling()
    
