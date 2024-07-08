from aiogram import Router, F, types
from bot import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.media_group import MediaGroupBuilder

from states.check_subscribe_state import CheckSubscribe
from keyboards.inline_keyboards.check_subscribe_keyboard import sub_ver_menu
from keyboards.reply_keyboards.subscribe_keyboard import sub_keyboard
from keyboards.reply_keyboards.register_keyboard import reg_keyboard
from filters.not_in_db_filter import NotInDbFilter


router = Router()


@router.message(F.text, Command("start"), NotInDbFilter())
async def cmd_start(message: Message, state: FSMContext):
    builder = MediaGroupBuilder(
        caption="""🔷 Добро пожаловать!

🥇<strong>skin_std_bot</strong>-лучший бот для майнинга и покупки внутриигровой валюты. В нашем сообществе принимают участвие более 10 человек, для оптимизации времени и решения проблем.

✅Именно у нас есть:
•<strong>НЕ</strong> купленные отзывы
•<strong>отзывчивый</strong> состав администраторов

•<strong>возврат средств</strong> в течении 2-ух дней"""
    )

    builder.add_photo(
        media=FSInputFile("images/greet.png"),
        parse_mode=ParseMode.HTML
    )

    await message.reply_media_group(
        media=builder.build()
    )
    await message.answer(
        text="Теперь Вы должны подписаться на наши каналы!",
        reply_markup=sub_keyboard
    )
    await state.set_state(CheckSubscribe.not_subscribe)


@router.message(F.text == "Подписки", CheckSubscribe.not_subscribe, NotInDbFilter())
async def cmd_subscribe(message: Message, state: FSMContext):
    await message.answer(
        "Подписка на каналы",
        reply_markup=sub_ver_menu
    )


@router.callback_query(CheckSubscribe.not_subscribe, F.data == "sub_check", NotInDbFilter())
async def check_subs(callback: CallbackQuery, bot: Bot, state: FSMContext):
    user_channel_status = await bot.get_chat_member(chat_id='@freeskis', user_id=callback.from_user.id)
    user_channel_status1 = await bot.get_chat_member(chat_id='@skin_std_reviews', user_id=callback.from_user.id)
    user_channel_status2 = await bot.get_chat_member(chat_id='@skin_std_feedback', user_id=callback.from_user.id)
    if user_channel_status.status != 'left' and user_channel_status1.status != 'left' and user_channel_status2.status != 'left':
        await callback.message.edit_text('Спасибо за подписку!')
        await state.clear()
        await state.set_state(CheckSubscribe.is_subscribe)
        await callback.message.answer("Теперь Вы можете зарегистрироваться в боте", reply_markup=reg_keyboard)
    else:
        await bot.answer_callback_query(callback.id, text='Для начала подпишись на наш канал', show_alert=True)
