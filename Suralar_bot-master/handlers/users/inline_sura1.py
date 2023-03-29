from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from filters import Shaxsiy
from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura1')
async def suralar(message:CallbackQuery):

    await message.message.answer(text="Fotiha Surasi🌹")
    dokument_manzil = InputFile(path_or_bytesio='for_send/Fotiha.docx')

    user_id = message.from_user.id
    await bot.send_document(chat_id=user_id, document=dokument_manzil)
    # await message.message.answer(text="Yetti oyatdan iborat bu sura Makkada nozil bo‘lgan. U «Fotiha», ya’ni «Ochuvchi sura» deb ataladi. Qur’ondagi suralarning joylashish tartibida avvalgi o‘rinda turgani va qisqa bo‘lishiga qaramasdan Qur’onning asosiy ma’no-mohiyatini o‘zida mujassam etgani uchun ham u Qur’on mazmunini «Ochuvchi» deb nomlangan. Bu surada yagona Allohga bo‘lgan e’tiqod, Uning o‘zigagina ibodat qilish, oxirat kuni borligiga ishonish, yolgiz Allohniig o‘zidan madad-yordam so‘rash, haq din va to‘g‘ri yo‘lni Uning o‘zigina ko‘rsata olishiga iymon keltirish kabi Islom dinining asosiy talablari o‘z aksini topgan. Shuning uchun bu surani «Ummul-Qur’on» — «Qur’onning onasi — asli» deb ham ataydilar. 1. Mehribon va rahmli Alloh nomi bilan (boshlayman). 2-3-4. Hamdu sano butun olamlar Xojasi, Mehribon va Rahmli, jazo (qiyomat) kunining Egasi — Podshohi bo‘lmish Alloh uchundir. I z o h. Maqtov-olqishga haqdor bo‘lish uchun bashar olamiga podshoh bo‘lishning o‘zigina kifoya qilmaydi. Balki koinotdagi barcha sayyoralar va ulardagi bor jonli-jonsiz mavjudotning hammasi ustidan ilmu hikmat va rahm-shafqat bilan egalik qiladigan, bundan tashqari, oxiratdagi hisob-kitob kunida ham yagona podshoh bo‘lgan Alloh taolonig O’zigina hamdu sanoga loyiq zotdir. 5. Sengagina ibodat qilamiz va Sendangina madad so‘raymiz. I z o h. Ya’ni, Sendan o‘zganing oldida boshimizni egmaymiz va Sendan o‘zgaga yordam so‘rab iltijo ham qilmaymiz. 6-7. Bizlarni, g‘azabga duchor bo‘lmagan va haq yo‘ldan toymagan zotlarga in’om qilgan yo‘ling bo‘lmish — To‘g‘ri yo‘lga yo‘llagaysan. I z o h. Mazkur zotlar — barcha payg‘ambarlar, haqiqiy iymon-e’tiqod egalari va o‘z aqidalari yo‘lida jonlarini fido qilgan kishilardir.")

