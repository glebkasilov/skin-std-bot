from aiogram import Router, F, types
from bot import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.repository import SupportRepository, AdminRepository
from filters.check_admin import CheckAdmin
from keyboards.inline_keyboards.admin.support_answer_keyboard import support_answer_menu


router = Router()


class Support(StatesGroup):
    answer_with_text = State()


@router.message(F.text, Command("support"), CheckAdmin())
async def answer_support(message: Message, state: FSMContext):
    if len(SupportRepository.get_all_questions()) == 1:
        await message.reply(
            f"У Вас новый вопрос, ответить на него?",
            reply_markup=support_answer_menu
        )
    
    elif len(SupportRepository.get_all_questions()) != 0:
        await message.reply(
            f"У Вас {len(SupportRepository.get_all_questions())} вопроса(ов), ответить на один из них?",
            reply_markup=support_answer_menu
        )

    else:
        await message.reply(
            "У Вас нет вопросов",
        )


@router.callback_query(F.data.startswith("support_"), CheckAdmin())
async def answer_support_for_message(callback: CallbackQuery, state: FSMContext):
    answer_support = callback.data.split("_")[1]
    if answer_support == "yes":
        qustion_mass = SupportRepository.get_question()
        await callback.message.delete()
        await state.set_state(Support.answer_with_text)
        await callback.message.answer(f"Вопрос от {qustion_mass.username}: {qustion_mass.question}\nНапишите Ваш ответ:", reply_markup=types.ReplyKeyboardRemove())
        await state.update_data({"id": qustion_mass.telegram_id})
    else:
        await callback.message.delete()


@router.message(F.text, Support.answer_with_text, CheckAdmin())
async def answer_support_text(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(
        chat_id=data["id"],
        text=f"От администратора {AdminRepository.get_admin(message.from_user.id).name}:\n{message.text}"
    )
    SupportRepository.delete_question(data["id"])
    await state.clear()