from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


check_subscribe_buttons = [
    [
        InlineKeyboardButton(text="Канал 1", url="https://t.me/pelmen_sel")
    ],
    [
        InlineKeyboardButton(
            text="Канал 2", url="https://t.me/skin_std_feedback")
    ],
    [
        InlineKeyboardButton(text="Проверка подписки",
                             callback_data="sub_check")
    ]
]

sub_ver_menu = InlineKeyboardMarkup(inline_keyboard=check_subscribe_buttons)
