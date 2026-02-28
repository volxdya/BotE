import json

import aiohttp
from random import choice, randint

import key_board.reply_keyboard as rkb
from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart, CommandObject
from collections import deque

import gif
from photos import photo_list, photof_list, photo_path

router = Router()

idf = [-1002730278858, 5922044080, -1003772916363]


HISTORY_SIZE = 15

recent_photos = deque(maxlen=HISTORY_SIZE)
recent_photos_f = deque(maxlen=HISTORY_SIZE)


@router.message(CommandStart())
async def cmsta(message: Message):
    print(f'{message.from_user.username}:{message.from_user.id} st98')
    if message.chat.id not in idf:
        await message.answer("Hello\nSelect a Epstein's file category", reply_markup=rkb.reply_start)
    else:
        await message.answer('Hello. My name is Jeffrey Epstein')


@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("""
Привет я Джеффри Эпштейн. Вот что я могу:
/port - мой портрет
/photo - рандомное фото из моих файлов
/gif - рандомная gif
Гдзи{параграф} - гдз по истории. Пример: Гдзи1
Гдза{параграф} - гдз по английскому языку. Пример: Гдза1
Гдзо{параграф} - гдз по обществознанию. Пример: Гдзо1
/joke и /joke18 и /mat - шутки
/pege {предмет} - предсказание баллов на ЕГЭ по предмету с помощью квантовых вычислений, древних легенд, блокчейна и астрологии. Пример: /pege информатика
    """)


@router.message(Command('port'))
async def port(message: Message):
    photosd = FSInputFile(r"Epstein.jpg")
    await message.answer_photo(photo=photosd, caption='My portrait')


@router.message(Command('photo'))
async def randomphoto(message: Message):
    if message.chat.id not in idf:
        photo_pool = photo_list
        history = recent_photos
    else:
        photo_pool = photof_list
        history = recent_photos_f

    if len(photo_pool) <= HISTORY_SIZE:
        history.clear()

    available_photos = [p for p in photo_pool if p not in history]

    if not available_photos:
        history.clear()
        available_photos = photo_pool

    selected_photo = choice(available_photos)

    history.append(selected_photo)

    photo = FSInputFile(selected_photo)
    await message.answer_photo(photo=photo)
    
    print(f'{message.from_user.username}:{message.from_user.id} EPH')


async def add_photo(photo, bot: Bot):
    path = f"{photo_path}/{photo.file_unique_id}.jpg"
    print("add photo:", path)
    await bot.download(photo.file_id, path)
    photo_list.append(path)


@router.message(Command("add_photo"), F.photo)
async def add_photo_by_message(message: Message, bot: Bot):
    await add_photo(message.photo[-1], bot)
    await message.answer("Фото добавлено")


@router.message(
    Command("add_photo"),
    F.reply_to_message,
    F.reply_to_message.photo
)
async def add_photo_by_reply(message: Message, bot: Bot):
    await add_photo(message.reply_to_message.photo[-1], bot)
    await message.answer("Фото добавлено")


@router.message(F.text == "Epstein's photo")
async def eph(message: Message):
    await message.answer('TGK_Link: t.me/jefphph')


@router.message(F.text == "Epsten's messages")
async def epm(message: Message):
    await message.answer('TGK_Link: t.me/jefmes')


@router.message(F.text == "Epstein's purchases")
async def epp(message: Message):
    await message.answer('TGK_Link: t.me/jefpur')


@router.message(F.text == "Keys for pashalko")
async def epk(message: Message):
    await message.answer("`Epstein`\n`Ainaz`\n`Eldar`", parse_mode="MarkdownV2")


'''
@router.message(F.text == 'Adolf_Hitler')
async def adkp(message: Message):
    print(f'{message.from_user.username}:{message.from_user.id} MI')
    await message.reply("||My idol||", parse_mode="MarkdownV2")
'''


@router.message(F.text == 'Epstein')
async def epkp(message: Message):
    await message.reply("||Island||", parse_mode="MarkdownV2")


@router.message(F.text == 'Ainaz')
async def agkp(message: Message):
    await message.reply("||ЖИРНЫЙ||", parse_mode="MarkdownV2")


@router.message(F.text == 'Eldar')
async def adkp(message: Message):
    await message.reply("||Shnyyyyyyyr||", parse_mode="MarkdownV2")


@router.message(F.text.startswith("Гдзи"))
async def gdzid(message: Message):
    hlink = message.text
    await message.answer(f"https://reshak.ru/otvet/reshebniki.php?otvet={hlink[4:]}&predmet=medinsky_russia11")


@router.message(F.text.startswith('Гдза'))
async def gdzad(message: Message):
    elink = message.text
    await message.answer(f'https://gdz.ru/class-11/english/reshebnik-spotlight-11/{elink[4:]}-pg/')


@router.message(F.text.startswith('Гдзо'))
async def gdzod(message: Message):
    olink = message.text
    await message.answer(f'https://reshak.ru/otvet/reshebniki.php?otvet={olink[4:]}&predmet=bogolubov11')


async def get_joke(category: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://rzhunemogu.ru/RandJSON.aspx?CType={category}", timeout=5) as response:
                raw = await response.text(encoding="cp1251")
                data = json.loads(raw, strict=False)

        return data.get("content", "Не удалось придумать анекдот")
    except Exception as e:
        print("Joke error:", e)
        return "Не удалось придумать анекдот"


@router.message(Command("joke"))
async def joke(message: Message):
    await message.answer(await get_joke(1))


@router.message(Command("joke18"))
async def joke(message: Message):
    if message.chat.id in idf:
        await message.answer("нет")
    else:
        await message.answer(await get_joke(11))


mat = open("resources/mat.txt", encoding="utf-8").readlines()


@router.message(Command("mat"))
async def ramdom_mat(message: Message):
    if message.chat.id not in idf:
        await message.answer(choice(mat))


@router.message(Command("pege"))
async def predict_ege(message: Message, command: CommandObject):
    if command.args is None:
        await message.answer("Ошибка: не передан аргумент")
    else:
        await message.answer(f"Ты получишь {randint(0, 100)} баллов на ЕГЭ по {command.args}")


@router.message(Command("gif"))
async def random_gif(message: Message):
    await message.answer_animation(gif.random_gif_id())


@router.message(Command("add_gif"), F.reply_to_message, F.reply_to_message.animation)
async def add_gif(message: Message):
    gif.add_gif(message.reply_to_message.animation.file_id)
    await message.answer("Гифка добавлена")
