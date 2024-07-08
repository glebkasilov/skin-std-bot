from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.media_group import MediaGroupBuilder
from random import randint

from database.repository import UserRepository
from filters.in_db_filter import InDbFilter
from keyboards.reply_keyboards.main_menu_keyboard import main_menu_keyboard

router = Router()


@router.message(F.text, Command("menu"), InDbFilter())
async def menu(message: Message):
    await message.reply(
        "Вы открыли меню",
        reply_markup=main_menu_keyboard
    )


@router.message(F.text == "Click", InDbFilter())
async def click(message: Message):
    count = round(randint(1, 5) * 0.10, 2)
    await message.reply(
        f"+ {count} голды"
    )
    UserRepository.add_money(message.from_user.id, count)


@router.message(F.text == "Получить подписку", InDbFilter())
async def subscribe(message: Message):
    await message.reply(
        f"""✅Способы получения подписки:

    •Пригласите 15 человек

    или

    •Пополните бота на 300₽"""
    )


@router.message(F.text == "Вывести голду", InDbFilter())
async def subscribe(message: Message):
    if not UserRepository.get_user_prime_status(message.from_user.id):
        await message.reply(
            "✨Прежде получите VIP статус✨"
        )
    else:
        await message.reply(
            "Ахуел?"
        )


@router.message(F.text == "Тех. поддержка", InDbFilter())
async def support(message: Message):
    await message.reply(
        "Для техничекской поддержки напишите /help"
    )


@router.message(F.text == "Профиль и баланс", InDbFilter())
async def profile(message: Message):
    pass


@router.message(F.text == "Отзывы", InDbFilter())
async def reviews(message: Message):
    await message.reply(
        "Влад, пидорас, сделай отзывы"
    )


@router.message(F.text == "Канал", InDbFilter())
async def channel(message: Message):
    await message.reply(
        "Канал: @freeskis"
    )
