from .models import User, Admin, Support
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
    def add_user(cls, telegram_id: int, username: str, name: str, std_id: int, money: int, refferals: int, prime_status: bool) -> None:
        session = cls.database_controler.create_session()
        user = User(
            telegram_id=telegram_id,
            username=username,
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
    def get_user_from_username(cls, username: str) -> User:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.username == username
        ).first()
        session.close()
        return user

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
    def add_refferals(cls, telegram_id: int) -> None:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        user.refferals += 1
        session.commit()
        session.close()

    @classmethod
    def id_in_database(cls, telegram_id: int) -> bool:
        session = cls.database_controler.create_session()
        users = session.query(User).all()
        return telegram_id in [int(user.telegram_id) for user in users]

    @classmethod
    def get_user_name(cls, telegram_id: int) -> str:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        session.close()
        return user.name

    @classmethod
    def get_user_std_id(cls, telegram_id: int) -> int:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        session.close()
        return user.std_id

    @classmethod
    def get_user_money(cls, telegram_id: int) -> float:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        session.close()
        return user.money

    @classmethod
    def get_user_refferals(cls, telegram_id: int) -> int:
        session = cls.database_controler.create_session()
        user = session.query(User).filter(
            User.telegram_id == telegram_id
        ).first()
        session.close()
        return user.refferals

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


class SupportRepository:
    database_controler = EngineController()

    @classmethod
    def create_question(cls, telegram_id: str, username: str, question: str) -> None:
        session = cls.database_controler.create_session()
        support = Support(
            telegram_id=telegram_id,
            username=username,
            question=question
        )
        session.add(support)
        session.commit()
        session.close()
    
    @classmethod
    def get_question(cls) -> Support:
        session = cls.database_controler.create_session()
        question = session.query(Support).first()
        session.close()
        return question
    
    @classmethod
    def get_all_questions(cls) -> list[Support]:
        session = cls.database_controler.create_session()
        questions = session.query(Support).all()
        session.close()
        return questions

    @classmethod
    def delete_question(cls, telegram_id: str) -> None:
        session = cls.database_controler.create_session()
        support = session.query(Support).filter(
            Support.telegram_id == telegram_id
        ).first()
        session.delete(support)
        session.commit()
        session.close()
