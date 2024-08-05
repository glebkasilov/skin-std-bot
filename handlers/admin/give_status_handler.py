from aiogram import Router, F, types
from bot import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from filters.check_admin import CheckAdmin

router = Router()

class GiveStatus(StatesGroup):
    give_status = State()


@router.message(F.text, Command("give_status"), CheckAdmin())
async def give_status(message: Message, state: FSMContext):
    await message.reply("Напишите ID пользователя:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("give_status")