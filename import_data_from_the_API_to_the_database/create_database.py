"""
This script creates the tables and the constraints for the MySQL database.

I use the ORM called 'peewee' instead of a basic driver python-mysql because
with 'peewee', my code is more portable.
"""

#External library
from peewee import *

#Create the 'database object' for the MySQL database
db = MySQLDatabase('pur_beurre_db', user='script',
                   password="SUPERmotdepasse3000", host="127.0.0.1")

class Category(Model):
    """This class is the 'category' table for the MySQL database"""

    name = CharField(max_length=40)

    class Meta:
        database = db

class FoodSubstituted(Model):
    """This class is the 'foodsubstituted' table for the MySQL database"""

    name = CharField(max_length=50)
    substituted_product_name = CharField(max_length=50)
    description = TextField()
    stores = CharField(max_length=50)
    link = CharField(max_length=200)
    id_category = ForeignKeyField(Category)
    is_saved = BooleanField(default=False)

    class Meta:
        database = db

#Create the tables in the MySQL database
db.connect()
db.create_tables([FoodSubstituted, Category])
db.close()
