import peewee
import datetime
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


db = SqliteExtDatabase('betsywebshop.db', pragmas={
    'journal_mode': 'wal', 
    'cache_size': -64 * 1000, 
    'synchronous': 0})


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(unique=True)
    first_name = CharField()
    last_name = CharField()
    address = TextField()
    postal_code = CharField()
    city = CharField()
    country = CharField()  
    billing_info = CharField()  


class Product(BaseModel):
    name = CharField(unique=True)
    description = CharField()
    unit_price = DecimalField(decimal_places=2, max_digits=10)
    quantity = IntegerField()  


class Ownership(BaseModel):
    user = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    number_owned = IntegerField()  


class Tag(BaseModel):
    tag_text = CharField(unique=True)


class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)


class Transaction(BaseModel):
    buyer = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    number_sold = IntegerField()
    datetime_sold = DateTimeField(default=datetime.datetime.now)


    
    
