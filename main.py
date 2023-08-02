from aiogram import Bot, Dispatcher, executor, types
# Import token from cfg.py
from cfg import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

'''@dp.message_handler()
async def echo(message: types.message):
    await message.answer(text=str(message.text).capitalize) # Mirror a message to user'''

'''@dp.message_handler()
async def echo_capitalize(message: types.message):
    await message.answer(text=message.text.capitalize()) # Mirror a capitalized message to user'''
    
@dp.message_handler()
async def echo_upper(message: types.message):
    if message.text.count(' ') >= 1: # Checks if message is more than 1 word
        await message.answer(text=message.text.upper()) # Mirror an upper message to user

if __name__ == '__main__':
    executor.start_polling(dp)