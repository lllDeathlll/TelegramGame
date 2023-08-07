from aiogram import Bot, Dispatcher, executor, types
# Import keyboards from keyboards.py
from keyboards import start_kb, help_kb
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
    await bot.send_message(chat_id=message.from_user.id,
                           text="Welcome to our <b>telegram bot!</b>",
                           parse_mode="HTML",
                           reply_markup=start_kb)
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgUAAxkBAAEJ5u9ky0lSzGPELeYrA1QmXJIK2G3qFgACbwMAAukKyAOvzr7ZArpddC8E")
    await message.delete()

# Adds help command that lists all commands
@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
<b>/start</b> - <em>start working with bot</em>
<b>/help</b> - <em>list of commands</em>
<b>/description</b> - <em>gives you a description of our bot</em>
""",
                           parse_mode="HTML",
                           reply_markup=help_kb)
    
# Adds description command that gives a description of bot
@dp.message_handler(commands=["description"])
async def desc_command(message: types.Message):
    await message.reply(text="""In our bot you will be able to play a game called "foobar". To start the game press play button""")
    await bot.send_photo(caption="""<a href="https://t.me/poncheg11">Никита Вокуев</a>""", parse_mode="HTML",
                         photo="https://i.mycdn.me/i?r=AzFIxPtkV78jcmdRfpoIOyaJnpzDvEoFL64PcQU7Y2RAeDO7EuABt8t6j6ROsg0SwU4",
                         chat_id=message.chat.id)
    
# Returns sticker id
@dp.message_handler(content_types=["sticker"])
async def sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)