from aiogram import types, Dispatcher, F, filters, Bot
import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


bot = Bot(token="6459329359:AAHoJ2ZO8E4-oRXP47zwGHDGLtXJKHI_85c")
dp = Dispatcher(bot=bot)


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()


contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
])


@dp.message(filters("start"))
async def start(message: types.Message, state: FSMContext):
   await state.set_data(Registration.first_name)
   await message.answer("Yaxshi endi familya kiriting:")



@dp.message(Registration.first_name)
async def first_name   