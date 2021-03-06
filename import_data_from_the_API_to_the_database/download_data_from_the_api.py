"""
This script downloads all the data we need and saves them in a MySQL database.

First, it does an HTTP request to the openfoodfacts API. Then, it finds a
new healthy substitution. And then, it saves the data in the database with
the ORM called 'peewee'.
"""

#External library
import requests

#Local library
from create_database import db, Category, FoodSubstituted
from functions import *

#Some constants
URL_CATEGORY = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
URL_FOOD = "https://fr.openfoodfacts.org/api/v0/produit/{}.json"

LIST_DOWNLOAD = [["boissons-sucrees", "5449000000439", "3228886043714", "0613008730758"],
                 ["produits-a-tartiner-sucres", "4008400401621", "3045320001549"],
                 ["snacks-sales", "3168930001003", "3168930008934", "3018930004934"],
                 ["snacks-sucres", "7610400087803", "5410041010800", "3175680012937"],
                 ["viennoiseries", "3256540000698", "9551429722918", "3564709015446"],
                 ["plats-prepares-surgeles", "3596710406388", "3760197632602", "3292590819705"],
                 ["biscuits-et-gateaux", "7622300292508", "7622300476144", "7622210477439"],
                 ["cereales-pour-petit-dejeuner", "3494690021013", "5050083712296"],
                 ["pates-alimentaires", "3266140059453", "3240931541815", "3240931537139"],
                 ["pizzas", "7613036218153", "3242272503057", "3242272348559"]]

#Connect to the MySQL database
db.connect()

for category in LIST_DOWNLOAD:

    category_name = category.pop(0)

    #Save the data in the database with a transaction
    with db.atomic() as transaction:
        new_category = Category.create(name=category_name)

    for id_food in category:

        #An HTTP request to get the information about the food
        data = requests.get(URL_FOOD.format(id_food))

        #If there is a problem with the request
        if data.status_code != 200:
            print("""Warning ! There is a problem with the HTTP request to the API for food.
                Food id : {}""".format(id_food))
        else:
            data = data.json()["product"]
            #Assign some variables
            food_name = assign_a_value(data, ["product_name_fr", "product_name"])
            nutriscore = data["nutrition_grades"]
            list_already_substituted = [food.substituted_product_name for food
                                        in FoodSubstituted.select()]

            #Find a new healthy substitution
            dict_data = find_a_substitute(URL_CATEGORY, category_name, nutriscore,
                                          list_already_substituted)

            #Assign more variables
            substitute_name = assign_a_value(dict_data, ["product_name_fr", "product_name"])
            substitute_name = shorten_string(substitute_name)
            description = assign_a_value(dict_data, ["generic_name_fr", "generic_name"])
            stores = assign_a_value(dict_data, ["stores"])
            link = "https://fr.openfoodfacts.org/produit/" + dict_data["code"]

            #Save the data in the database with a transaction
            with db.atomic() as transaction:
                new_food = FoodSubstituted.create(name=food_name,
                                                  substituted_product_name=substitute_name,
                                                  description=description, stores="",
                                                  link=link, id_category=new_category)

            #The code below is necessary beacause the API contains some errors.
            try:
                new_food = FoodSubstituted.update(stores=stores).where(FoodSubstituted.name
                                                                       == new_food.name)
                new_food.execute()
            #No exception type specified because the API contains too often some new errors
            except:
                pass

#Close the connection with the MySQL database
db.close()
