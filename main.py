import models
from peewee import fn
from datetime import datetime


__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

db = models.SqliteDatabase('betsywebshop.db')
models = models.product_models(db)
list(models.items())

def populate_test_database():
    db.create_tables([models.User, models.Product, models.Tag, models.ProductTag])

    
def store_data():
    models.User.create(
        user_name='Kevin',
        first_name='Kevin',
        last_name='Soetosenojo',
        address='Rinus michelslaan 2E',
        postal_code='1061MB',
        city='Amsterdam',
        country='The Netherlands',
        iban='secret')

    models.User.create(
        user_name='AH',
        first_name='Albert',
        last_name='Heijn',
        address='Osdorp 21',
        postal_code='1066FX',
        city='Amsterdam',
        country='The Netherlands',
        iban='NVT')

    models.Product.create(
        product_name='Lays',
        description='Chips',
        unit_price=2.49,
        number_in_stock=1000)

    models.Product.create(
        product_name='Pindakaas',
        description='Calve Pindakaas',
        unit_price=3.89,
        number_in_stock=1000)

    models.Product.create(
        product_name='Yoghurt Gums',
        description='Katja Yoghurt gums snoep',
        unit_price=1.95,
        number_in_stock=1000)

    models.Tag.create(tag_text='bed')
    models.Tag.create(tag_text='fed')
    models.ProductTag.create(
        tag='lays',
        product_name='Lays')
    models.ProductTag.create(
        tag='calve',
        product_name='Pindakaas')
    models.ProductTag.create(
        tag='yoghurt gums',
        product_name='Yoghurt Gums')


def search(term):
    for product in models.Product.select().where(fn.Lower(
        models.Product.product_name.contains(term.lower()))):
        print(product.product_name)
        
def list_products_per_tag(tag_id):
    list_of_products_per_tag = []
    query = models.Product.select().join(models.ProductTag).join(models.Tag).where(models.Tag.tag_text == tag_id)
    print(query)
    for product in query:
        print(product.product_name)
    
def add_product_to_catalog(user_id, product):
    new_product = models.Product.create(
        product_name=product['product_name'],
        description=product['description'],
        unit_price=product['unit_price'],
        number_in_stock=product['number_in_stock'])
    models.Ownership.create(user_name=user_id, product=new_product)
    
def remove_product(user_id, product_id):
    owner = models.Ownership.get_or_none(
        models.Ownership.user_name == user_id and
        models.Ownership.product == product_id)
    if owner:
        owner.delete_instance()

   

def update_stock(product_id, new_quantity):
    query = models.Product.update(
        number_in_stock=new_quantity).where(
        models.Product.product_name == product_id)
    query.execute()


def purchase_product(product_id, buyer_id, quantity):
    models.Transaction.create(
        buyer=buyer_id,
        product_name=product_id,
        number_sold=quantity,
        datetime_sold=datetime.now()
    )

    sold_product = models.Product.get(
                   models.Product.product_name == product_id)
    new_quantity = sold_product.number_in_stock - quantity
    update_stock(product_id, new_quantity)
    add_product_to_catalog(buyer_id, sold_product)
    query = (models.Ownership
             .update(number_owned=models.Ownership.number_owned + quantity)
             .where(models.Ownership.user_name == buyer_id,
                    models.Ownership.product_name == product_id))
    query.execute()
