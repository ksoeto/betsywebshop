# Models go here

import peewee
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


db = SqliteExtDatabase('betsywebshop.db', pragmas={
    'journal_mode': 'wal', 
    'cache_size': -64 * 1000, 
    'synchronous': 0})

class BaseModel(Model):
    class Meta:
        database = db

class User(Model):
    username = CharField()
    join_date = DateTimeField()
    about_me = TextField()
    
class product(BaseModel):
    name = charField()
    information= TextField()
    purchase = DatetimeField()
    quantity = IntegerField()
    price = DecimalField()
    
class tag(BaseModel):
    tag = ForeignField(product)
    
class transaction(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    purchased_date = DateTimeField(default=datetime.datetime.now)
    quantity = Integerfield()

    
    