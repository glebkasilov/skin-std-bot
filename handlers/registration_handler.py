from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from states.check_subscribe_state import CheckSubscribe
from database.repository import UserRepository
from filters.not_in_db_filter import NotInDbFilter
from keyboards.reply_keyboards.only_menu_keyboard import only_menu_keyboard
from keyboards.inline_keyboards.refer_choice_keyboard import refer_choice_menu
from keyboards.inline_keyboards.refer_choice_back_keyboard import refer_choice_back_menu

router = Router()


class Registration(StatesGroup):
    name_input = State()
    id_input = State()
    refer_input = State()


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
    user_message = message.text
    if all(char in "0123456789" for char in user_message):
        await state.update_data({"id": user_message})
        data = await state.get_data()

        UserRepository.add_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            name=data["name"],
            std_id=data["id"],
            money=0,
            refferals=0,
            prime_status=False
        )
        await state.clear()
        await message.answer("Есть ли у Вас реферальный код?", reply_markup=refer_choice_menu)
    
    else:
        await message.answer("Ваш ID должен содержать только цифры!")


@router.callback_query(F.data.startswith("refer"))
async def refer_choice(callback: CallbackQuery, state: FSMContext):
    data = callback.data.split("_")[-1]
    print(data)
    if data == "yes":
        await callback.message.edit_text("Введите реферальный код:", reply_markup=refer_choice_back_menu)
        await state.set_state(Registration.refer_input)
    elif data == "no":
        await callback.message.delete()
        await callback.message.answer("Регистрация прошла успешно!", reply_markup=only_menu_keyboard)
    else:
        await callback.message.delete()
        await callback.message.answer("Регистрация прошла успешно!", reply_markup=only_menu_keyboard)
        await state.clear()


@router.message(Registration.refer_input, F.text)
async def refer_input(message: Message, state: FSMContext):
    user_message = message.text
    if user_message in [str(user_id.telegram_id) for user_id in UserRepository.get_all_users()]:
        UserRepository.add_refferals(int(user_message))
        await message.reply("Регистрация прошла успешно!", reply_markup=only_menu_keyboard)
        await state.clear()
    else:
        await message.reply("Такого реферального кода нет(", reply_markup=refer_choice_back_menu)