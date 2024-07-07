from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_buttons = [
    [KeyboardButton(text="Click")],
    [KeyboardButton(text="Получить подписку"), KeyboardButton(text="Вывести голду")],
    [KeyboardButton(text="Тех. поддержка"), KeyboardButton(text="Профиль и баланс")],
    [KeyboardButton(text="Отзывы")],
    [KeyboardButton(text="Канал")]
]

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=main_buttons, resize_keyboard=True)
