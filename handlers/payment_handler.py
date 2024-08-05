from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery

from database.repository import UserRepository
from filters.in_db_filter import InDbFilter

router = Router()


@router.message(F.text, Command("pay"), InDbFilter())
async def pay(message: Message):
    if UserRepository.get_user_prime_status(message.from_user.id):
        await message.reply("Вы уже перевели деньги, нам больше не надо)")
    else:
        await message.reply("""Для пополнения бота переведите 300₽ на счет:
5599002083122228
и напишите об этом нашиму админу @freeskisADM

<i>В течение нескольких часов Ваша подписка будет активирована</i>""",
                            parse_mode=ParseMode.HTML
                            )
