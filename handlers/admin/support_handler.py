from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline_keyboards.admin.admin_keyboard import make_admin_keyboard
from keyboards.inline_keyboards.admin.question_keyboard import make_keyboard
from database.repository import AdminRepository


router = Router()


class Support(StatesGroup):
    answer_with_text = State()


@router.callback_query(F.data.startswith("question_"))
async def answer_question(callback: CallbackQuery, state: FSMContext):
    user_id = callback.data.split("_")[-1]
    if "question_pass_" in callback.data:
        question = callback.data.split("_")[-2]
        await callback.message.edit_text(
            "Выберите админа, которому передать вопрос:",
            reply_markup=await make_admin_keyboard(
                str(callback.from_user.id),
                AdminRepository.get_all_admins(),
                user_id,
                question
            )
        )
    elif "question_answer_" in callback.data:
        await callback.message.edit_text(
            "Напишите ответ на вопрос пользователя: "
        )
        await state.set_state(Support.answer_with_text)
        await state.update_data({callback.from_user.id: user_id})
        await callback.answer()


@router.message(Support.answer_with_text, F.text)
async def answer_with_text(message: Message, state: FSMContext, bot: Bot):
    text = message.text
    data = await state.get_data()
    admin = AdminRepository.get_admin(message.from_user.id)
    await message.answer(
        "Ваш ответ успешно отправлен)"
    )
    await bot.send_message(
        chat_id=data[message.from_user.id],
        text=f"Ответ от {admin.name}: {text}"
    )
    await state.set_data({message.from_user.id: None})
    await state.set_data({data[message.from_user.id]: None})
    await state.clear()


@router.callback_query(F.data.startswith("admin_"))
async def redirect_to_admin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = callback.data.split("_")
    to_admin = AdminRepository.get_admin(data[-3])
    await bot.send_message(
        chat_id=data[-3],
        text=f"Перенаправленный вопрос от админа: {data[-4]}",
        reply_markup=await make_keyboard(data[-1], data[-4])
    )
    await callback.message.edit_text(
        text=f"Вопрос передан админу: {to_admin.name}",
    )
    await callback.answer()
