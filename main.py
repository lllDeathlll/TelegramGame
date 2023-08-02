from aiogram import Bot, Dispatcher, executor, types
# Import token from cfg.py
from cfg import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.message):
    await message.answer(text=message.text) # Write message

if __name__ == '__main__':
    executor.start_polling(dp)