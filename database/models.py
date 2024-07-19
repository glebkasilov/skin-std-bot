import sqlalchemy

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    telegram_id = sqlalchemy.Column(
        sqlalchemy.String(32),
        primary_key=True,
        unique=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.String(128)
    )

    std_id = sqlalchemy.Column(
        sqlalchemy.String(32),
        unique=True
    )

    money = sqlalchemy.Column(
        sqlalchemy.Float
    )

    refferals = sqlalchemy.Column(
        sqlalchemy.Integer
    )

    prime_status = sqlalchemy.Column(
        sqlalchemy.Boolean
    )

    def __repr__(self) -> str:
        return f"User: {self.telegram_id}"


class Admin(Base):
    __tablename__ = "admin"

    telegram_id = sqlalchemy.Column(
        sqlalchemy.String(32),
        primary_key=True,
        unique=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.String(128)
    )

    def __repr__(self) -> str:
        return f"Admin: {self.telegram_id}"


class Support(Base):
    __tablename__ = "support"

    telegram_id = sqlalchemy.Column(
        sqlalchemy.String(32),
        primary_key=True,
        unique=True
    )
    
    username = sqlalchemy.Column(
        sqlalchemy.String(128)
    )

    question = sqlalchemy.Column(
        sqlalchemy.String(4096)
    )

    def __repr__(self) -> str:
        return f"Question from a user: {self.telegram_id}"
