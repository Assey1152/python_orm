import os
from dotenv import load_dotenv
import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, Base

load_dotenv()
DSN = os.getenv('DSN')
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def load_data():
    with open("fixtures/tests_data.json") as f:
        json_data = json.load(f)
    with Session() as session:
        for record in json_data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()


def easy_load_data():
    with open("fixtures/tests_data.json") as f:
        json_data = json.load(f)
    with Session() as session:
        for row in json_data:
            match row['model']:
                case 'publisher':
                    session.add(Publisher(id=row.get('pk'), **row.get('fields')))
                case 'book':
                    session.add(Book(id=row.get('pk'), **row.get('fields')))
                case 'shop':
                    session.add(Shop(id=row.get('pk'), **row.get('fields')))
                case 'stock':
                    session.add(Stock(id=row.get('pk'), **row.get('fields')))
                case 'sale':
                    session.add(Sale(id=row.get('pk'), **row.get('fields')))
        session.commit()


def find_books(target):
    with Session() as session:
        q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        q = q.join(Publisher).join(Stock).join(Shop).join(Sale)
        if target.isdigit():
            return q.filter(Publisher.id == target).all()
        else:
            return q.filter(Publisher.name.like(target)).all()





