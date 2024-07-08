from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reg_buttons = [[KeyboardButton(text="Подписки")]]

sub_keyboard = ReplyKeyboardMarkup(
    keyboard=reg_buttons, resize_keyboard=True, one_time_keyboard=True)
