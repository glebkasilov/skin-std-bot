from aiogram import Router, F, types
from bot import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.media_group import MediaGroupBuilder

from states.check_subscribe_state import CheckSubscribe
from keyboards.inline_keyboards.check_subscribe_keyboard import sub_ver_menu
from keyboards.reply_keyboards.subscribe_keyboard import sub_keyboard
from keyboards.reply_keyboards.register_keyboard import reg_keyboard


router = Router()


@router.message(F.text, Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    builder = MediaGroupBuilder(
        caption="Приветствую Вас в нашем боте!...",
    )

    builder.add_photo(
        media=FSInputFile("images/greet.jpg"),
    )

    await message.reply_media_group(
        media=builder.build()
    )
    await message.answer(
        text="Теперь Вы должны подписаться на наши каналы!",
        reply_markup=sub_keyboard
    )
    await state.set_state(CheckSubscribe.not_subscribe)


@router.message(F.text == "Подписки", CheckSubscribe.not_subscribe)
async def cmd_subscribe(message: Message, state: FSMContext):
    await message.answer(
        "Подписка на каналы",
        reply_markup=sub_ver_menu
    )


@router.callback_query(CheckSubscribe.not_subscribe, F.data == "sub_check")
async def check_subs(callback: CallbackQuery, bot: Bot, state: FSMContext):
    user_channel_status = await bot.get_chat_member(chat_id='@freeskis', user_id=callback.from_user.id)
    if user_channel_status.status != 'left':
        await callback.message.edit_text('Спасибо за подписку!')
        await state.clear()
        await state.set_state(CheckSubscribe.is_subscribe)
        await callback.message.answer("Теперь Вы можете зарегистрироваться в боте", reply_markup=reg_keyboard)
    else:
        await bot.answer_callback_query(callback.id, text='Для начала подпишись на наш канал', show_alert=True)


