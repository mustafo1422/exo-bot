# from aiogram import Dispatcher, types, F, filters, Bot
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# import asyncio

# bot = Bot(token="7110029090:AAHojzfETeRW0iEbAXWL1KRw8L4f4Ix5XV8")
# dp = Dispatcher(bot=bot)


# keyboards = [
#     [KeyboardButton(text='Lavash'), KeyboardButton(text="Donar"), KeyboardButton(text="Free")],
#     [KeyboardButton(text="Hot-dog")],
#     [KeyboardButton(text="Hamburger"), KeyboardButton(text="Orbit")]
# ]
# main_button = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)

# keyboards1 = [
#     [KeyboardButton(text='pepsi'), KeyboardButton(text="cola"), KeyboardButton(text="fanta")],
#     [KeyboardButton(text="sprite")],
#     [KeyboardButton(text="Dinay"), KeyboardButton(text="1lSok")]
# ]
# main_button1 = ReplyKeyboardMarkup(keyboard=keyboards1, resize_keyboard=True)


# keyboards_second = [
#     [KeyboardButton(text='Ovqat'), KeyboardButton(text="Ichimliklar")],

# ]



# main_button_second = ReplyKeyboardMarkup(keyboard=keyboards_second, resize_keyboard=True)


# keyboards_second2 = [
#     [KeyboardButton(text="zakaz qilasmi"), KeyboardButton(text="Yoq")],

# ]



# main_button_second2 = ReplyKeyboardMarkup(keyboard=keyboards_second2, resize_keyboard=True)


# @dp.message(filters.Command("start"))
# async def start(message: types.Message):
#     await message.answer("Xush kelibsiz, qorniz ochmi?", reply_markup=main_button_second)


# @dp.message(F.text == "Ovqat")
# async def start(message: types.Message):
#     await message.answer(f"Nima yemoqchisiz", reply_markup=main_button)

# @dp.message(F.text == "Ichimliklar")
# async def start(message: types.Message):
#     await message.answer(f"Nma ichmoqsisiz", reply_markup=main_button1)

# @dp.message(F.text == "Hot-dog")
# async def start(message: types.Message):
#     await message.answer("Siz lavash tanladiz 31000 som", reply_markup=keyboards_second2())

# @dp.message(F.text == "Donar")
# async def start(message: types.Message):
#     await message.answer("Siz Donar tanladiz sizdan 23000 som",reply_markup=keyboards_second2())

# @dp.message(F.text == "Free")
# async def start(message: types.Message):
#     await message.answer("Siz kartoshka fri tanladiz sizdan 10000 som", reply_markup=keyboards_second2())

# @dp.message(F.text == "Donar")
# async def start(message: types.Message):
#     await message.answer("Siz Donar eni 93cm boyi 93cm tanladiz sizdan 553000 som", reply_markup=keyboards_second2())

# @dp.message(F.text == "pepsi")
# async def start(message: types.Message):
#     await message.answer("Siz pepsi tanladiz sizdan 10000 som",reply_markup=keyboards_second2())

# @dp.message(F.text == "fanta")
# async def start(message: types.Message):
#     await message.answer("Siz fanta tanladiz sizdan 10000 som",reply_markup=keyboards_second2())

# @dp.message(F.text == "sprite")
# async def start(message: types.Message):
#     await message.answer("Siz sprite tanladiz sizdan 10000 som",reply_markup=keyboards_second2())

# @dp.message(F.text == "Dinay")
# async def start(message: types.Message):
#     await message.answer("Siz Dinay tanladiz sizdan 10000 som",reply_markup=keyboards_second2())

# @dp.message(F.text == "1lsok")
# async def start(message: types.Message):
#     await message.answer("Siz sprite 1lsok sizdan 15000 som", reply_markup=keyboards_second2())

# async def main():
#     await dp.start_polling(bot)


# if __name__ == '__main__':
#     asyncio.run(main())


from aiogram import types, Bot, Dispatcher, F, filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

bot = Bot(token="7110029090:AAHojzfETeRW0iEbAXWL1KRw8L4f4Ix5XV8")
dp = Dispatcher(bot=bot)


main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Food'), KeyboardButton(text="Drink"), KeyboardButton(text="Info")]
])

drink_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Coca-Cola", callback_data="Coca-Cola")],
    [InlineKeyboardButton(text="sprite", callback_data="sprite" )],
    [InlineKeyboardButton(text="fanta", callback_data="fanta" )],
    [InlineKeyboardButton(text="pepsi", callback_data="pepsi" )],
    [InlineKeyboardButton(text="ays", callback_data="ays" )],
])

food_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Hamburger 🍔", callback_data="hamburger")],
    [InlineKeyboardButton(text="Hot-Dog", callback_data="Hot-dog" )],
    [InlineKeyboardButton(text="Lavash", callback_data="Lavash" )],
    [InlineKeyboardButton(text="donar", callback_data="Donar" )],
    [InlineKeyboardButton(text="Free 🍟", callback_data="Free" )],
])


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.full_name}, nima tanlaysiz?",
                         reply_markup=main_button)


@dp.message(F.text == "Food")
async def food_function(message: types.Message):
    await message.answer("Nima ovqat tanlisiz?", reply_markup=food_button)

@dp.message(F.text == "Drink")
async def food_function(message: types.Message):
    await message.answer("Nima ovqat tanlisiz?", reply_markup=drink_button)


@dp.callback_query(F.data == "hamburger")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://s1.1zoom.ru/big3/346/391554-svetik.jpg", text="Siz hamburger oldiz 40.000 so'm")


@dp.callback_query(F.data == "Hot-dog")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(text="Siz Hot-dog tanladiz 12.000 som")

@dp.callback_query(F.data == "Lavash")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://bogatyr.club/uploads/posts/2023-03/1677899894_bogatyr-club-p-shaurma-so-svininoi-foni-vkontakte-4.jpg", caption="Lavash tanladiz 51.000 som")

@dp.callback_query(F.data == "Donar")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://vostorg.buzz/uploads/posts/2022-12/1671916715_1-vostorg-buzz-p-donar-blyudo-1.jpg", caption="Siz Donar tanladiz 32.000 som")

@dp.callback_query(F.data == "Free")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.patee.ru/r/x6/15/8b/e2/960m.jpg", caption="Siz Free tanladiz 15.000 som")

@dp.callback_query(F.data == "fanta")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://aurearestaurante.cl/wp-content/uploads/2020/08/fanta_lata.png", caption="Siz fanta tanladiz 11.000 som")


@dp.callback_query(F.data == "Coca-Cola")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://fikiwiki.com/uploads/posts/2022-02/1644920245_36-fikiwiki-com-p-krasivie-kartinki-koka-kola-43.jpg",  caption="Siz coca-cola tanladiz 11.000 som")

@dp.callback_query(F.data == "sprite")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://express.uncle-ho.ru/wa-data/public/shop/products/64/09/964/images/210/210.970.jpg", caption="Siz sprite tanladiz 11.000 som")

@dp.callback_query(F.data == "pepsi")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yakuzasushi.ru/assets/images/products/179/pepsi.jpg", caption="Siz pepsi tanladiz 11.000 som")

@dp.callback_query(F.data == "ays")
async def food_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://telegra.ph/file/679408266f7f099e02ee2.jpg", caption="Siz Ays tea tanladiz 10.000 som")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
