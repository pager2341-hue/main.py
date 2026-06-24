import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# အစ်ကို့ Bot Token
TOKEN = '8954961595:AAGXCHXe32W89DRQeNwqJ0Noz65mB2s286U'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Admin ထံသို့ စာပို့ရန်
    await context.bot.send_message(
        chat_id='8708515019',
        text=f"📌 အသုံးပြုသူအသစ်: {user.full_name}\n🆔 ID: {user.id}"
    )
    
    # User ထံသို့ ပြန်ကြားချက် (ဤနေရာတွင် အစ်ကို့ username ထည့်ထားပါတယ်)
    await update.message.reply_text(
        f"မင်္ဂလာပါ {user.first_name}!\n\n"
        "ဝန်ဆောင်မှုအတွက် @thant12450 ကို တိုက်ရိုက်ဆက်သွယ်နိုင်ပါတယ်။\n\n"
        "⏰ ဝန်ဆောင်မှုချိန်: တနင်္လာ - သောကြာ (3:00 PM - 11:00 PM)\n\n"
        "⚠️ ငွေမပေးချေမီ Video Call (VC) ခေါ်၍ အတည်ပြုပါ။"
    )

if __name__ == '__main__':
    # Application ကို တည်ဆောက်ခြင်း
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Start command handler
    app.add_handler(CommandHandler("start", start))
    
    print("✅ Bot စတင် အလုပ်လုပ်နေပါပြီ...")
    # Polling method (Webhook မလိုပါ)
    app.run_polling()
  
