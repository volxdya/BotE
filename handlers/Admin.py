from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import os
from aiogram.client.session.aiohttp import AiohttpSession

router_admin = Router()
load_dotenv()
bot = Bot(os.getenv('BOT_TOCKEN'), session = AiohttpSession(proxy="http://proxy.server:3128"))
Admin_id = int(os.getenv('ADMIN_ID', 0))

class Admin_States(StatesGroup):
    waiting_for_text = State()

@router_admin.message(Command('admin'))
async def abrc(message: Message, state: FSMContext):
    if message.from_user.id != Admin_id:
        await message.answer("У вас нет прав использовать эту команду")
        return
    await message.answer("ID;text:")
    await state.set_state(Admin_States.waiting_for_text)
'''
@router_admin.message(Command('StihProDrakona'))
async def spd(message: Message):
    await message.answer("""Вот и я, например, так жёстко срал.
Показал туалетной двери свой оскал.
Я Пробил своё дно, полезло оно.
Славное, сильное говно.
Заплакал дракон от разжигающей вони.
В слезах утопил он дерьма последние стоны.

И каждый, кто срал Так хотя бы разок.
Любого говна уважает кусок.
Испустил мой жопень последние томные вздохи.
Разверзлись, как облака, мои булки и ноги.
Дерьму потоки открыты теперь.
И всё время, что срал, смотрел я на дверь.
Тернистые густы лились, словно кровь.
Дерьмища потоки и кала струи покрыли толчок, словно капли росы.
На заре, когда солнце восходит на небо.
Я сру и дристаю, в пределах туалета.""")
'''

@router_admin.message(Admin_States.waiting_for_text)
async def pubrc(message: Message, state: FSMContext):
    text = message.text.split(";", 1)
    await bot.send_message(chat_id = text[0], text = text[1])
    await state.clear()













