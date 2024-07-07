from .models import User
from .engine import EngineController


class UserRepository:
    database_controler = EngineController()

    @classmethod
    def get_user(cls, telegram_id: int) -> User:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id).first()
        session.close()
        return user

    @classmethod
    def get_all_users(cls) -> list[User]:
        session = cls.database_controler.create_session()
        users = session.query(User).all()
        session.close()
        return users

    @classmethod
    def add_user(cls, telegram_id: int, name: str, std_id: int, money: int, refferals: int, prime_status: bool) -> None:
        session = cls.database_controler.create_session()
        user = User(
            telegram_id=telegram_id,
            name=name,
            std_id=std_id,
            money=money,
            refferals=refferals,
            prime_status=prime_status
        )
        session.add(user)
        session.commit()
        session.close()

    @classmethod
    def get_username(cls, telegram_id: int) -> str:
        session = cls.database_controler.create_session()
        username = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first().name
        session.close()
        return username

    @classmethod
    def update_money(cls, telegram_id: int, money: int) -> None:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        user.money = money
        session.commit()
        session.close()
    
    @classmethod
    def update_prime_status(cls, telegram_id: int, prime_status: bool) -> None:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        user.prime_status = prime_status
        session.commit()
        session.close()
    
    