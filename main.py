import asyncio
from bot import Bot, web_app
from pyrogram import idle
from config import *

async def main():
    # 1. Initialize the Bot Instance
    # Using the variables defined in your config.py
    bot = Bot(
        SESSION,
        WORKERS,
        DB_CHANNEL,
        FSUBS,
        TOKEN,
        ADMINS,
        MESSAGES,
        AUTO_DEL,
        DB_URI,
        DB_NAME,
        API_ID,
        API_HASH,
        PROTECT,
        DISABLE_BTN
    )

    # 2. Start the Bot and Web Server (Health Check)
    # This keeps the bot alive on platforms like Render, Koyeb, or Heroku
    await bot.start()
    await web_app()
    
    print("Success: Bot and Web Server are now running...")
    
    # 3. Keep the script running
    # This prevents the script from exiting immediately
    await idle()
    
    # 4. Graceful Shutdown
    await bot.stop()

if __name__ == "__main__":
    # Execution using the asyncio event loop
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")
