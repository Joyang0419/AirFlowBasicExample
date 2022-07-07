# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy import insert, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.cursor import CursorResult

Base = declarative_base()
engine_url = "mysql+pymysql://root:joy@localhost:3306/airflow"
engine = create_engine(engine_url, echo=True)


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, autoincrement=True)
    enable = Column(Boolean)


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def create_session():
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    return session


def insert_row():
    stmt = (
        insert(Test).values(
            enable=False
        )
    )
    db_session = create_session()
    result: CursorResult = db_session.execute(statement=stmt)
    db_session.commit()

    return result.inserted_primary_key[0]


def update_row(_id, enable):
    stmt = (
        update(Test).
        where(Test.id == _id).
        values(enable=enable)
    )
    db_session = create_session()
    db_session.execute(statement=stmt)
    db_session.commit()
