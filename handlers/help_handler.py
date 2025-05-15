from aiogram import Router, F, Bot, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database.repository import AdminRepository, SupportRepository
from keyboards.reply_keyboards.main_menu_keyboard import main_menu_keyboard
from filters.in_db_filter import InDbFilter


router = Router()


class Help(StatesGroup):
    ask_question = State()


@router.message(Command("help"), InDbFilter())
async def cmd_help(message: Message, state: FSMContext):
    if str(message.from_user.id) not in [i.telegram_id for i in SupportRepository.get_all_questions()]:
        await message.reply(
            "Опишите свою проблему:",
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.set_state(Help.ask_question)
    else:
        await message.reply(
            "Ваш вопрос уже на рассмотрение."
        )


@router.message(F.text, Help.ask_question, InDbFilter())
async def help_message(message: Message, bot: Bot, state: FSMContext):
    text = message.text

    await message.answer(
        f"Ваш вопрос: {text}. Модераторы ответят на него как только будут свободны😄",
        reply_markup=main_menu_keyboard
    )

    SupportRepository.create_question(
        message.from_user.id, message.from_user.username, text)

    admins = AdminRepository.get_all_admins()

    for i in admins:
        await bot.send_message(
            chat_id=i.telegram_id,
            text=f"Новая просьба о помощи(/support)"
        )

    await state.clear()


@router.message(Help.ask_question, InDbFilter())
async def wrong_input(message: Message):
    await message.answer(
        "Некорректный тип ввода. \n\nПопробуйте еще раз."
    )
