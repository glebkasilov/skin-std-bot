from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.models import Admin


async def make_admin_keyboard(
    admin_id: str,
    admins: list[Admin],
    user_id: str,
    question: str
) -> InlineKeyboardMarkup:
    admins_buttons = [
        [
            InlineKeyboardButton(
                text=f"{admin.name}",
                callback_data=f"admin_question_{question}_{admin.telegram_id}_to_{user_id}"
            )
        ]
        for admin in admins if admin.telegram_id != admin_id
    ]
    return InlineKeyboardMarkup(inline_keyboard=admins_buttons)