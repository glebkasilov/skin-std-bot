from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


refer_choice_buttons = [
    [
        InlineKeyboardButton(
            text="Да",
            callback_data="refer_yes"
        )
    ],
    [
        InlineKeyboardButton(
            text="Нет",
            callback_data="refer_no"
        )
    ]
]

refer_choice_menu = InlineKeyboardMarkup(inline_keyboard=refer_choice_buttons)
