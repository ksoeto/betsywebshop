__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
import peewee

db = SqliteDatabase('betsywebshop.db')
models = product_models(db)
list(models.items())

def database():
    user = Table('person', ('id', 'first', 'last'))
    user_id = Table('note', ('id', 'product_id', 'content', 'timestamp'))
    Reminder = Table('reminder')
    models.db.connect()
    
    
def search(term):
    for product in models.Product.select().where(models.Product.name ** f"%{term}%"):
            print(product.name)
   

def list_user_products(user_id):
    with models.db:
        user_id = Table('note', ('id', 'product_id', 'content', 'timestamp'))
    
    product, created = Product.get_or_create(
    product_name=product_name,
    description_name=description_name,
    defaults={'tv': samsung, 'favorite_color': 'black','price':500})
    
    product, created = Product.get_or_create(
    product_name=product_name,
    description_name=description_name,
    defaults={'playstation': sony, 'favorite_color': 'black','price':600})
    
    product, created = Product.get_or_create(
    product_name=product_name,
    description_name=description_name,
    defaults={'phone': samsung, 'favorite_color': 'red','price':300})
    
    product, created = Product.get_or_create(
    product_name=product_name,
    description_name=description_name,
    defaults={'microwave': samsung, 'favorite_color': 'black','price':100})
    
    product, created = Product.get_or_create(
    product_name=product_name,
    description_name=description_name,
    defaults={'musicbox': jbl, 'favorite_color': 'grey','price':250})
        
def list_products_per_tag(tag_id):
    list_of_products_per_tag = []
    query = models.Product.select(models.Product).join(models.Tag).join(models.Product).where(models.Product_Tag.id == tag_id)
    print(query)
    for product in query:
        print(product)
    
    
def add_product_to_catalog(user_id, product):
    if request.method == "POST":
        form = ProductListForm(request.POST)
        if form.is_valid():
            pl = form.save(commit=False)
            pl.update_user = request.user
            pl.save()
            return redirect(reverse("productdb:list-product_lists"))
   

def update_stock(product_id, new_quantity):
    query = product.update(counter=Stat.counter + 1).where(Stat.url == request.url)
    query.execute()


def purchase_product(product_id, buyer_id, quantity):
    query = models.Product.select(models.Product).join(models.Tag).join(models.Product).where(models.Product_Tag.id == tag_id)
    print(query)
    for product in query:
        print(product)


def remove_product(product_id):
    products.delete().where(Contacts.Name=='product').execute()
