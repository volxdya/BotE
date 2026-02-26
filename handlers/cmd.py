from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import Key_Board.Reply_KeyBoard as rkb
from Photo_List import photo_list
from random import choice

router = Router()

idf = [-1002730278858, 5922044080, -1003772916363]


@router.message(CommandStart())
async def cmsta(message: Message):
    print(f'{message.from_user.username}:{message.from_user.id} st98')
    if message.chat.id not in idf:
        await message.answer("Hello\nSelect a Epstein's file category", reply_markup = rkb.reply_start)
    else:
        await message.answer('Hello. My name is Jeffrey Epstein')

@router.message(Command('port'))
async def port(message: Message):
    photosd = FSInputFile(r"Epstein.jpg")
    await message.answer_photo(photo=photosd, caption='My portrait')

@router.message(Command('photo'))
async def randomphoto(message: Message):
    if message.chat.id not in idf:
        chosen_photo = choice(photo_list)
        photo = FSInputFile(f"photo/{chosen_photo}")
        await message.answer_photo(photo=photo, caption = 'Комнада будет доступна через 2,5 секунды')
    else:
        chosen_photof = choice(photo_list)
        photof = FSInputFile(f"photof/{chosen_photof}")
        await message.answer_photo(photo=photof, caption = 'Комнада будет доступна через 2,5 секунды')
    print(f'{message.from_user.username}:{message.from_user.id} EPH')

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

