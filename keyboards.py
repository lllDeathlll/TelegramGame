from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# Adds keyboard on start command with auto resizing
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("/help"))

# Adds inline keyboard to message sent on help command that removes on press
help_kb = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
help_b1 = InlineKeyboardButton(text="/help")
help_b2 = InlineKeyboardButton(text="/description")
help_b3 = InlineKeyboardButton(text="/start_game")
help_kb.add(help_b1).insert(help_b2).insert(help_b3)