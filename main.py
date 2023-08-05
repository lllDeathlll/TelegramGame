from aiogram import Bot, Dispatcher, executor, types
# Import token from cfg.py
from cfg import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
    
# Adds function that completes on bot startup
async def on_startup(_):
    print("Bot connected successfully")

# Adds start command with welcome message
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text="Welcome to our <b>telegram bot!</b>", parse_mode="HTML")
    await bot.send_sticker(message.from_user.id, sticker="CAACAgUAAxkBAAEJ5u9ky0lSzGPELeYrA1QmXJIK2G3qFgACbwMAAukKyAOvzr7ZArpddC8E")
    await message.delete()

# Adds help command that lists all commands
@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text="""
<b>/start</b> - <em>start working with bot</em>
<b>/help</b> - <em>list of commands</em>
<b>/description</b> - <em>gives you a description of our bot</em>
""", parse_mode="HTML")
    
# Adds description command that gives a description of bot
@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await message.reply(text="In our bot you will be able to play a game called \"foobar\". To start the game press play button")
    
# Returns sticker id
@dp.message_handler(content_types=["sticker"])
async def sticker_id_command(message: types.Message):
    await message.answer(message.sticker.file_id)
    
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)