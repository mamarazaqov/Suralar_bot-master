from aiogram.types import CallbackQuery
from loader import dp

@dp.callback_query_handler(text='dasturchi')
async def suralar(message:CallbackQuery):

     await message.message.answer(text=f" Bu botni dasturchi Muhammadamin hech qanday manfaatsiz, xolis niyatda yaratdi.🌹\n\n Bot sizga foyda bersa, biz xursandmiz! 😊 \n Barcha suralarni o'qib chiqing! Olloh o'zi qo'llasin🤲")
