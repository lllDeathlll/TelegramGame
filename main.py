from aiogram import Bot, Dispatcher, executor, types
# Import token from cfg.py
from cfg import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Adds start command with welcome message
@dp.message_handler(commands=["start"])
async def start_command(message: types.message):
    await message.answer(text="Welcome to our telegram bot!")
    await message.delete()

# Adds help command that lists all commands
@dp.message_handler(commands=["help"])
async def help_command(message: types.message):
    await message.reply(text="""
/start - start working with bot
/help - list of commands
/description - gives you a description of our bot
""")
    
# Adds description command that gives a description of bot
@dp.message_handler(commands=["description"])
async def description_command(message: types.message):
    await message.reply(text="""In our bot you will be able to play a game called "foobar". To start the game press play button""")

if __name__ == '__main__':
    executor.start_polling(dp)