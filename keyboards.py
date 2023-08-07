from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# Adds keyboard on start command with auto resizing
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("/help"))

# Adds inline keyboard to message sent on help command that removes on press
help_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
help_b1 = KeyboardButton(text="/help")
help_b2 = KeyboardButton(text="/description")
help_b3 = KeyboardButton(text="/start_game")
help_kb.insert(help_b1).insert(help_b2).insert(help_b3)

# Adds first choice to the game start
game_start_kb = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
game_start_b1 = InlineKeyboardButton(text="Choose 1", callback_data="one")
game_start_b2 = InlineKeyboardButton(text="Choose 2", callback_data="two")
game_start_kb.add(game_start_b1).add(game_start_b2)