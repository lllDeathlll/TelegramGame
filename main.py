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
async def desc_command(message: types.Message):
    await message.reply(text=
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nec lobortis magna. Aenean augue quam, tincidunt non sodales nec, sollicitudin eu enim. Fusce gravida varius lorem, ac rutrum eros laoreet ut. Nam maximus lacus sit amet augue molestie varius. Proin varius condimentum nisl, eu facilisis ipsum feugiat in. Vivamus blandit arcu sed sem cursus tempus. Nulla tempus quam nec nisl mollis suscipit. Fusce tempus massa luctus massa suscipit, malesuada scelerisque urna convallis. Fusce aliquet pretium diam congue luctus. Proin ut vulputate orci, vitae bibendum eros. Vestibulum pellentesque massa ex, in accumsan magna dapibus vitae. Nullam quis iaculis elit, non pellentesque magna. Donec non consectetur risus. Phasellus eget elit ante. Nam vel ultricies lorem. Mauris faucibus arcu erat, a malesuada ipsum viverra sed.

Sed elementum mauris sem, id congue augue feugiat vel. Curabitur volutpat ante ante. Quisque finibus ipsum sed quam porttitor iaculis. Nullam venenatis ultrices consequat. Proin non odio euismod, luctus purus vitae, egestas sem. Fusce euismod ac lacus in condimentum. Donec scelerisque gravida pellentesque. Nullam a ipsum vitae nibh mollis interdum nec non libero. Phasellus erat eros, hendrerit rhoncus vulputate in, lobortis eget eros. Quisque mauris est, rutrum rutrum felis non, malesuada pulvinar libero. Proin sed tincidunt leo. Proin interdum elit tristique, porta urna a, posuere lorem. Cras nisl diam, euismod vel dignissim quis, luctus a diam. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce dapibus sem at fermentum interdum. Aenean luctus sed mauris ac sagittis.

Maecenas et tellus accumsan, maximus lacus nec, consequat arcu. Duis porta pellentesque mollis. Quisque euismod euismod neque, at faucibus nisl lacinia non. Aenean in velit lorem. In suscipit leo sapien, non congue ex bibendum id. Curabitur sapien nibh, commodo a magna ut, vestibulum feugiat augue. Curabitur vitae mauris imperdiet, aliquet risus sed, aliquet augue. Mauris sit amet arcu a elit lobortis pretium eget ut enim. Quisque maximus dui sapien, nec rhoncus elit convallis dignissim.

Nulla aliquam sapien felis, et maximus ligula venenatis eget. Aliquam ut pretium leo, non vulputate elit. Etiam sollicitudin, metus eget consectetur cursus, justo ligula faucibus sem, ut aliquam magna odio at erat. In fringilla erat quis blandit sagittis. Aliquam lobortis ultrices diam. Quisque lobortis auctor lorem fermentum pellentesque. Maecenas eget vulputate risus. Aenean placerat erat non feugiat vulputate. Proin a elit vel odio lacinia bibendum at in turpis. Etiam semper ut leo id viverra. In id ornare ligula.

Etiam euismod mattis accumsan. Nullam ut ornare ex, venenatis efficitur ante. Maecenas faucibus dapibus lacus non facilisis. Fusce at suscipit dolor. Mauris viverra nulla magna, id porttitor leo porttitor at. Duis luctus dictum eleifend. Duis lacinia a turpis eget fermentum.
""")
    
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)