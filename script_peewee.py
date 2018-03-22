from peewee import *

db = MySQLDatabase('pur_beurre_db', user='script',
    password="SUPERmotdepasse3000", host="127.0.0.1")

class FoodSubstituted(Model):
    """This class is the 'food_substituted' table for the MySQL database"""

    product_name = CharField(max_length=50)
    substituted_product_name = CharField(max_length=50)
    description = TextField()
    stores = CharField(max_length=50)
    link = CharField(max_length=200)

    class Meta:
        database = db

db.connect()
db.create_tables([FoodSubstituted])

aliment1 = FoodSubstituted.create(product_name="Nutella",
    substituted_product_name="Pâte aux noisettes", description="Blablabla",
    stores="Carrefour", link="https://fr.openfoodfacts.org")

db.close()