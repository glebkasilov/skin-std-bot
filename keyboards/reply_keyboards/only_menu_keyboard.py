from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = [[KeyboardButton(text="/menu")]]

only_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=menu_button, resize_keyboard=True, one_time_keyboard=True)
