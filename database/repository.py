from .models import User, Admin
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
    def add_money(cls, telegram_id: int, money: float) -> None:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        user.money += money
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

    @classmethod
    def add_refferals(cls, telegram_id: int, refferals: int) -> None:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        user.refferals = refferals + user.refferals
        session.commit()
        session.close()

    @classmethod
    def id_in_database(cls, telegram_id: int) -> bool:
        session = cls.database_controler.create_session()
        users = session.query(User).all()
        return telegram_id in [int(user.telegram_id) for user in users]

    # TODO: add get methods

    @classmethod
    def get_user_prime_status(cls, telegram_id: int) -> bool:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        session.close()
        return user.prime_status


class AdminRepository:
    database_controller = EngineController()

    @classmethod
    def get_admin(cls, admin_id: int) -> Admin:
        session = cls.database_controller.create_session()
        admin = session.query(Admin).filter(
            Admin.telegram_id == admin_id).first()
        session.close()
        return admin

    @classmethod
    def get_all_admins(cls) -> list[Admin]:
        session = cls.database_controller.create_session()
        admins = session.query(Admin).all()
        session.close()
        return admins

    @classmethod
    def create(cls, telegram_id: str, name: str) -> None:
        session = cls.database_controller.create_session()
        admin = Admin(
            telegram_id=telegram_id,
            name=name
        )
        session.add(admin)
        session.commit()
        session.close()
