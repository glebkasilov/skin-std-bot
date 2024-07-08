from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def make_keyboard(user_id: str, question: str) -> InlineKeyboardMarkup:
    questions_buttons = [
        [
            InlineKeyboardButton(
                text="Ответить на вопрос",
                callback_data=f"question_answer_{user_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text="Передать другому админу",
                callback_data=f"question_pass_{question}_{user_id}"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=questions_buttons)
