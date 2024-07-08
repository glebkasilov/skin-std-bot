from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.media_group import MediaGroupBuilder

from states.check_subscribe_state import CheckSubscribe
from database.repository import UserRepository
from filters.not_in_db_filter import NotInDbFilter
from keyboards.reply_keyboards.only_menu_keyboard import only_menu_keyboard


router = Router()


class Registration(StatesGroup):
    name_input = State()
    id_input = State()


@router.message(F.text == "Зарегистрироваться", CheckSubscribe.is_subscribe, NotInDbFilter())
async def name_input(message: Message, state: FSMContext):
    print(UserRepository.id_in_database(message.from_user.id))
    await message.answer(
        "Введите Ваш никнейм:",
    )
    await state.set_state(Registration.name_input)


@router.message(Registration.name_input, F.text, NotInDbFilter())
async def name_input(message: Message, state: FSMContext):
    await state.update_data({"name": message.text})
    await state.set_state(Registration.id_input)
    await message.answer(
        "Введите Ваш Standoff id:",
    )


@router.message(Registration.id_input, F.text, NotInDbFilter())
async def id_input(message: Message, state: FSMContext):
    await state.update_data({"id": message.text})
    data = await state.get_data()

    UserRepository.add_user(
        telegram_id=message.from_user.id,
        name=data["name"],
        std_id=data["id"],
        money=0,
        refferals=0,
        prime_status=False
    )
    await state.clear()

    await message.answer("Регистрация прошла успешно!", reply_markup=only_menu_keyboard)
