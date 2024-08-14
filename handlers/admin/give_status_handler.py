from aiogram import Router, F, types
from bot import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from filters.check_admin import CheckAdmin
from database.repository import UserRepository

router = Router()

class GiveStatus(StatesGroup):
    give_status = State()


@router.message(F.text, Command("give_status"), CheckAdmin())
async def give_status(message: Message, state: FSMContext):
    await message.reply("Напишите ID пользователя:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(GiveStatus.give_status)


@router.message(F.text, GiveStatus.give_status, CheckAdmin())
async def give_status(message: Message, state: FSMContext, bot: Bot):
    username = message.text
    print(username, [i.username for i in UserRepository.get_all_users()])
    if username in [i.username for i in UserRepository.get_all_users()]:
        UserRepository.set_user_prime_status(username, True)
        await message.reply(f"Пользователь @{username} получил статус Prime")
        user = UserRepository.get_user_from_username(username)
        await bot.send_message(
            chat_id=user.telegram_id,
            text="Поздравляем, Вы получили статус VIP статус!\n\nСпасибо за поддержку!"
        )
    
    else:
        await message.reply("Такого пользователя нет в базе данных")

    await state.clear()