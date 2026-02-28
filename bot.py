import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers.cmd import router
from handlers.admin import router_admin
from dotenv import load_dotenv
from aiogram.client.session.aiohttp import AiohttpSession


async def main():
    try:
        load_dotenv()
        bot_token = os.getenv('BOT_TOKEN')
        bot = Bot(token = bot_token, session = AiohttpSession(proxy="http://proxy.server:3128"))
        dp = Dispatcher()
        dp.include_router(router)
        dp.include_router(router_admin)
        print("Bot start")
        await dp.start_polling(bot, skip_updates=True)
    except Exception as ex:
        print(f"Error:{ex}")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
