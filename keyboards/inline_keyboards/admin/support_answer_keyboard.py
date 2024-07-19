from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


yes_no_buttons = [
    [
        InlineKeyboardButton(text="Да", callback_data="support_yes"),
        InlineKeyboardButton(text="Нет", callback_data="support_no")
    ]
]

support_answer_menu = InlineKeyboardMarkup(inline_keyboard=yes_no_buttons)