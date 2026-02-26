import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers.cmd import router
from handlers.Admin import router_admin
from dotenv import load_dotenv
from handlers.Antifl import AntiFloodMiddleware



async def main():
    try:
        load_dotenv()
        bot_tocken = os.getenv('BOT_TOCKEN')
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



'''
curl.exe -X POST "https://api.telegram.org/bot8508011364:AAGxseSRIQiHr8xaBN3DfFhsUpqIaNrX3Jg/sendMessage" ` -d "chat_id=882885310" ` -d "text=Привет это я Эпштейн. Посмотри все категории и найди все пасхалки, чтобы получить шанс на поездку на мой остров"
curl.exe -X POST "https://api.telegram.org/bot8508011364:AAGxseSRIQiHr8xaBN3DfFhsUpqIaNrX3Jg/sendMessage" ` -d "chat_id=7790399263" ` -d "text=Вы зачислены в список гостей на остров Эпштейна. Все подробности у @UserVadik"
curl.exe -X POST "https://api.telegram.org/bot8508011364:AAGxseSRIQiHr8xaBN3DfFhsUpqIaNrX3Jg/sendMessage" ` -d "chat_id=1005396335" ` -d "text=Try sending the keys (words)"
curl.exe -X POST "https://api.telegram.org/bot8508011364:AAGxseSRIQiHr8xaBN3DfFhsUpqIaNrX3Jg/sendMessage" ` -d "chat_id=8127753414" ` -d "text=/port"
curl.exe -X POST "https://api.telegram.org/bot8508011364:AAGxseSRIQiHr8xaBN3DfFhsUpqIaNrX3Jg/sendMessage" ` -d "chat_id=-1002101964028" ` -d "text=А он вас не хочет"
curl.exe -X POST "https://api.telegram.org/bot8508011364:AAGxseSRIQiHr8xaBN3DfFhsUpqIaNrX3Jg/sendMessage" ` -d "chat_id=-1002730278858" ` -d "text=Бот успешно запущен"
'''