from aiogram.filters import BaseFilter
from aiogram.types import Message
from database.repository import AdminRepository


class CheckAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return AdminRepository.get_admin(message.from_user.id)