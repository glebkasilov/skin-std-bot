from aiogram.filters import BaseFilter
from aiogram.types import Message
from database.repository import UserRepository


class NotInDbFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return not UserRepository.id_in_database(message.from_user.id)
