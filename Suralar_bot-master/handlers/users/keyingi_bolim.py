from aiogram import types
from handlers.users.keyingi_inline_buttons import keyingi_inline_tugmalar
from loader import dp

@dp.message_handler(text="Keyingi bo'lim🌹")
async def suralar(sura: types.Message):
    await sura.answer(text="Keyingi bo'limdagi suralarni tanlang🌹",reply_markup=keyingi_inline_tugmalar)
