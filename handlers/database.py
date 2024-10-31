import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()

        # Таблица для отзывов
        self.reviews = Table(
            'reviews', self.metadata,
            Column('id', Integer, primary_key=True),
            # ... остальные колонки
        )

        # Таблица для блюд
        self.dishes = Table(
            'dishes', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('price', Integer),
            Column('category', String)
            # ... другие колонки
        )

    def create_tables(self):
        self.metadata.create_all(self.engine)