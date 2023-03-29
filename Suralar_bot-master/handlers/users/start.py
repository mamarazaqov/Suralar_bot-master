import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.yonalishlar import yonalishlar_button
from loader import dp, db, bot
from filters import Shaxsiy

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.first_name
    try:
        db.qoshish(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Inshaalloh bu botimiz sizga foyda beradi!🌹")
    await message.answer(f"Botimizdagi ma'lumotlarning barchasi www.ziyouz.com saytidan olingan bo'lib, Alouddin Mansur tarjimasi🌹 \n \nBotda xato-kamchiliklar bo'lsa, Avvalo Allohdan, so'ngra sizdan kechirim so'raymiz!🌹")
    await message.answer(f"Qur'oni Karim Tarjimalari🌹 tugmasini bosing🌹",reply_markup=yonalishlar_button)
