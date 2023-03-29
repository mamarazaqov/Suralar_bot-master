from aiogram import types

from handlers.users.keyingi_inline_buttons import keyingi_inline_tugmalar
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp

@dp.message_handler(text="Qur'oni Karim tarjimalari🌹")
async def suralar(sura: types.Message):
    await sura.answer(text="Qur'oni Karim suralarini tanlang🌹",reply_markup=inline_tugmalar)
    await sura.answer(text="Keyingi bo'limga o'tish uchun Keyingi Bo'lim🌹 tugmasini bosing🌹")