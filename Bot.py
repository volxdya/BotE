import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers.cmd import router
from handlers.Admin import router_admin
from dotenv import load_dotenv
from handlers.Antifl import AntiFloodMiddleware
from aiogram.client.session.aiohttp import AiohttpSession



async def main():
    try:
        load_dotenv()
        bot_tocken = os.getenv('BOT_TOCKEN', session = AiohttpSession(proxy="http://proxy.server:3128"))
        bot = Bot(bot_tocken)
        dp = Dispatcher()
        dp.include_router(router)
        dp.include_router(router_admin)
        dp.message.middleware(AntiFloodMiddleware(time_limit=1))
        print("Bot start")
        await dp.start_polling(bot, skip_updates= True)
    except Exception as ex:
        print(f"Oshibka:{ex}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")


