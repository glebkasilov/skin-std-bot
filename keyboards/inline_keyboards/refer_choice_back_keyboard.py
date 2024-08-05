from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


refer_choice_back_buttons = [
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="refer_back"
        )
    ]
]

refer_choice_back_menu = InlineKeyboardMarkup(inline_keyboard=refer_choice_back_buttons)

