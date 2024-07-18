from aiogram  import Dispatcher , Bot , filters , types, F
import asyncio
bot=Bot(token='7110029090:AAHojzfETeRW0iEbAXWL1KRw8L4f4Ix5XV8')
dp = Dispatcher(bot=bot)


@dp.message(F.text)
async def echo_function(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

