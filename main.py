from aiogram import Bot, Dispatcher, executor, types
import random
import string
import requests
# Import token from cfg.py
from cfg import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Adds random letter on text
@dp.message_handler()
async def random(message: types.message):
    await message.reply(text=f"{await random.choice(set([string.ascii_letters]))}")

# Adds start command with welcome message
@dp.message_handler(commands=["start"])
async def help_command(message: types.message):
    await message.answer(text="Welcome to our telegram bot!")
    await message.delete()

# Adds help command that lists all commands
@dp.message_handler(commands=["help"])
async def help_command(message: types.message):
    await message.reply(text="""
/start - start working with bot
/help - list of commands
/description - gives you a description of our bot
/bitcoin - gives you bitcoin rate
""")
    
# Adds description command that gives a description of bot
@dp.message_handler(commands=["description"])
async def help_command(message: types.message):
    await message.reply(text="In our bot you will be able to play a game")
    
# Adds bitcoin command that gives you bitcoin rate    
@dp.message_handler(commands=['bitcoin'])
async def help_command(message: types.message):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = await requests.get(url)
    data = response.json()

    await message.reply(text=f"Bitcoin value in USD is: {data['bpi']['USD']['rate']}")

count = 0
 
# Adds count command that adds 1 every time
@dp.message_handler(commands=['count'])
async def help_command(message: types.message):
    global count
    await message.reply(text=f"Count is {count}")
    count += 1

if __name__ == '__main__':
    executor.start_polling(dp)