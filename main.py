from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
# Import keyboards from keyboards.py
from keyboards import start_kb, help_kb, game_start_kb
# Import token from cfg.py
from cfg import TOKEN_API

STAGE = "bunker_history"

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
<b>/start_game</b> - <em>start the game</em>
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
    
# Adds command to start the game
@dp.message_handler(commands=["start_game"])
async def game_start_command(message: types.Message):
    reply_markup = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
    button_next = InlineKeyboardButton(text="История бункера", callback_data="bunker_history")
    reply_markup.add(button_next)
    text = open("lore/world_history.txt", "r")
    await message.reply(text=text.read(),
    reply_markup=reply_markup)
    
dp.register_message_handler(game_start_command)
    
async def world_history(callback_query: CallbackQuery):
    await callback_query.answer("История мира")
    reply_markup = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
    button_next = InlineKeyboardButton(text="История бункера", callback_data="bunker_history")
    reply_markup.add(button_next)
    text = open("lore/world_history.txt", "r")
    await callback_query.message.edit_text(text=text.read(), reply_markup=reply_markup)   
    
dp.register_callback_query_handler(world_history, lambda c: c.data == 'world_history')
dp.register_message_handler(world_history)
    
async def bunker_history(callback_query: CallbackQuery):
    await callback_query.answer("История бункера")
    reply_markup = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
    button_previous = InlineKeyboardButton("История мира", callback_data='world_history')
    button_next = InlineKeyboardButton("Кто мы?", callback_data='who_are_we')
    reply_markup.add(button_previous).insert(button_next)
    text = open("lore/bunker_history.txt", "r")
    await callback_query.message.edit_text(text=text.read(), reply_markup=reply_markup)

dp.register_callback_query_handler(bunker_history, lambda c: c.data == 'bunker_history')
dp.register_message_handler(bunker_history)

async def who_are_we(callback_query: CallbackQuery):
    await callback_query.answer("Кто мы?")
    reply_markup = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
    button_previous = InlineKeyboardButton("История бункера", callback_data='bunker_history')
    button_next = InlineKeyboardButton("Далее", callback_data='the_beginning')
    reply_markup.add(button_previous).insert(button_next)
    text = open("lore/who_are_we.txt", "r")
    await callback_query.message.edit_text(text=text.read(), reply_markup=reply_markup)  
    
dp.register_callback_query_handler(who_are_we, lambda c: c.data == 'who_are_we')
dp.register_message_handler(who_are_we)
    
'''@dp.callback_query_handler()
async def game_start_callback(callback: types.CallbackQuery):
    if callback.data == "one":
        await callback.message.edit_text("ONE")
        return await callback.answer(text="You chose one")
    if callback.data == "two":
        await callback.message.edit_text("TWO")
        return await callback.answer(text="You chose two")'''
    
if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup)