from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import MetaTrader5 as mt5

# Telegram bot tokenini kiriting
TOKEN = "7903654492:AAGG2AoqhP_wa8JR8r82vXNQVLwfLmFlc4M"

# MT5 ga ulanamiz
mt5.initialize()

# Start buyrug‘i
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🤖 Salom! Men Forex bozorini analiz qiluvchi botman.\n\n"
                                    "🔹 /price EURUSD - Joriy narx\n"
                                    "🔹 /analyze EURUSD - Forex tahlil\n"
                                    "🔹 /help - Yordam")

# Narxni olish
async def get_price(update: Update, context: CallbackContext) -> None:
    symbol = context.args[0] if context.args else "EURUSD"
    price = mt5.symbol_info_tick(symbol).ask
    await update.message.reply_text(f"📊 {symbol} narxi: {price}")

# Forex analiz qilish (oddiy versiya)
async def analyze(update: Update, context: CallbackContext) -> None:
    symbol = context.args[0] if context.args else "EURUSD"
    price = mt5.symbol_info_tick(symbol).ask
    trend = "📈 Buy" if price > 1.10 else "📉 Sell"
    await update.message.reply_text(f"📊 {symbol} bo‘yicha tahlil:\n\n"
                                    f"🔹 Joriy narx: {price}\n"
                                    f"📢 Signal: {trend}")

# Botni ishga tushirish
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", get_price))
    app.add_handler(CommandHandler("analyze", analyze))

    app.run_polling()

if __name__ == "__main__":
    main()

