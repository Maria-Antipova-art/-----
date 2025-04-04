from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.utils.random_fox import fox
from less3.keyboards.keyboards import kb1,kb2

from random import randint

router = Router()

@router.message(Command("start"))
async def command_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}! Выбери нужную кнопку!',reply_markup=kb1)

@router.message(Command("user"))
async def send_user(message: types.Message):
    await message.answer("Как дела?")

@router.message(Command("stop"))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}!')

@router.message(Command("fox"))
@router.message(Command("Лиса"))

async def send_fox(message: types.Message):
    name = message.chat.first_name
    img_fox=fox()
    await message.answer(f'Держи лису, {name}!')
    await message.answer_photo(photo=img_fox)
    #await bot.send_photo(message.from_user.id,photo=img_fox)

@router.message(F.text.lower() == "num")
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")

@router.message(F.text)
async def msd_echo(message: types.Message):
    msg_user = message.text
    name = message.chat.first_name
    if 'Привет' in msg_user:
      await message.answer(f'Привет, {name}!')
    elif 'Пока' in msg_user:
      await message.answer(f'Пока-пока, {name}!')
    elif 'Покажи кубик' in msg_user:
      await message.answer_dice(emoji="")
    elif 'Лиса' in msg_user:
      await message.answer(f'Смотри,что у меня есть, {name}!',reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова!')