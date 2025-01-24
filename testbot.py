from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TEST_BOT_TOKEN = "7639618391:AAEdB5xclZPa00p2HNiOBlSyNzK7i5-0kOY"

TEST_GAME_SHORT_NAME = "xduel_test"

DEV_URL = "https://xanarhythm.s3.ap-southeast-1.amazonaws.com/xduel-dev/index.html"

current_game_url = DEV_URL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"X-Duel test version. Press play to start."
    )
    await update.message.reply_game(TEST_GAME_SHORT_NAME)


async def game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    user_id = query.from_user.id
    username = query.from_user.username
    first_name = query.from_user.first_name
    last_name = query.from_user.last_name

    # add these parameters to the game URL
    specialURL = current_game_url + f"?user_id={user_id}&username={username}&first_name={first_name}&last_name={last_name}"

    # make sure the URL is properly encoded
    specialURL = specialURL.replace(" ", "%20")

    print("Launching game with test URL:", specialURL)

    # Acknowledge the callback query
    await query.answer(
        text="Launching game...",
        show_alert=True,
        url=specialURL
    )

def main():

    print("Starting test bot...")

    application = Application.builder().token(TEST_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(game_callback))
    application.run_polling()
    

if __name__ == "__main__":
    main()