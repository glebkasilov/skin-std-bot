from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
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
    if UserRepository.get_user_refferals(message.from_user.id) >= 10 and not UserRepository.get_user_prime_status(message.from_user.id):
        UserRepository.set_user_prime_status(message.from_user.username, True)
        await message.reply(
            "Поздравляем, Вы получили статус VIP статус!"
        )

    elif not UserRepository.get_user_prime_status(message.from_user.id):
        await message.reply(
            f"""✅Способы получения подписки:

        •Пригласите 10 человек

        или

        •Пополните бота на 300₽
        <i>Для этого пишите</i> /pay""",
            parse_mode=ParseMode.HTML
        )
    else:
        await message.reply(
            "Благодарим Вас, Вы уже получили подписку"
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
    user = message.from_user.id
    builder = MediaGroupBuilder(
        caption=f"""🐙<strong> Профиль</strong> [{user}]
➖➖➖➖➖➖➖➖➖➖
🔴 <strong>{"Нет премиум статуса"if not UserRepository.get_user_prime_status(user) else "Премиум статус подключен!"}</strong>
➖➖➖➖➖➖➖➖➖➖
💵 Баланс: <strong>{"{:.2f}".format(UserRepository.get_user_money(user))} G</strong>
🔄 На выдаче: <strong>0 G</strong>
➖➖➖➖➖➖➖➖➖➖
🏠 Рефералы: <strong>{UserRepository.get_user_refferals(user)}</strong>
Ваш реферальный код: <I>{user}</I>"""
    )

    builder.add_photo(
        media=FSInputFile("images/profile.png"),
        parse_mode=ParseMode.HTML
    )

    await message.reply_media_group(
        media=builder.build()
    )


@router.message(F.text == "Отзывы", InDbFilter())
async def reviews(message: Message):
    await message.reply(
        """@skin_std_reviews - Канал с отзывами о магазине
        
@freeskisADM - Пиши сюда отзыв о боте"""
    )


@router.message(F.text == "Канал", InDbFilter())
async def channel(message: Message):
    await message.reply(
        "Канал: @freeskis"
    )
