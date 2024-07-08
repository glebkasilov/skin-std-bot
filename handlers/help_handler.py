from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.repository import AdminRepository
from keyboards.inline_keyboards.admin.question_keyboard import make_keyboard


router = Router()


class Help(StatesGroup):
    ask_question = State()


@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    await message.reply(
        "Опишите свою проблему:"
    )
    await state.set_state(Help.ask_question)


@router.message(F.text, Help.ask_question)
async def help_message(message: Message, bot: Bot, state: FSMContext):
    text = message.text

    await message.answer(
        f"Ваш вопрос: {
            text}. Модераторы ответят на него как только будут свободны😄"
    )
    admins = AdminRepository.get_all_admins()

    await bot.send_message(
        chat_id=admins[0].telegram_id,
        text=f"Вопрос от {message.from_user.full_name}: {text}",
        reply_markup=await make_keyboard(message.from_user.id, text)
    )

    await state.clear()


@router.message(Help.ask_question)
async def wrong_input(message: Message):
    await message.answer(
        "Некорректный тип ввода. \n\nПопробуйте еще раз."
    )
