import requests
from script_create_database import db, Category, FoodSubstituted

URL_CATEGORY = "https://fr.openfoodfacts.org/categorie/{}/{}.json"
URL_FOOD = "https://fr.openfoodfacts.org/api/v0/produit/{}.json"

LIST_DOWNLOAD = [["boissons-sucrees", "5449000000439", "3228886043714", "0613008730758"],
["produits-a-tartiner-sucres", "4008400401621", "3045320001549"],
["snacks-sales", "3168930001003", "3168930008934", "3018930004934"],
["snacks-sucres", "7610400087803", "5410041010800", "3175680012937"],#2ieme
["viennoiseries", "3256540000698", "9551429722918", "3564709015446"],
["plats-prepares-surgeles", "3596710406388", "3760197632602", "3292590819705"],
["biscuits-et-gateaux", "7622300292508", "7622300476144", "7622210477439"],
["cereales-pour-petit-dejeuner", "3494690021013", "5050083712296"],
["pates-alimentaires", "3266140059453", "3240931541815", "3240931537139"],
["pizzas", "7613036218153", "3242272503057", "3242272348559"]]

db.connect()

for category in LIST_DOWNLOAD:
    category_name = category.pop(0)
    with db.atomic() as transaction:
        new_category = Category.create(name=category_name)
    for id_food in category:
        data = requests.get(URL_FOOD.format(id_food))
        try:
            assert data.status_code == 200
        except AssertionError:
            print("Warning ! There is a problem with the HTTP request for food to the API. Food id : {}".format(id_food))
        else:
            try:
                food_name = data.json()["product"]["product_name_fr"]
            except:
                food_name = data.json()["product"]["product_name"]
            nutriscore = data.json()["product"]["nutrition_grades"]
            page = 1
            substitute_data = requests.get(URL_CATEGORY.format(category_name, str(page)))
            try:
                assert substitute_data.status_code == 200
            except AssertionError:
                print("""Warning ! There is a problem with the HTTP request for the category to the API.
                    Category : {}""".format(category_name))
            else:
                i = 0
                while True:
                    if i == 19:
                        page += 1
                        substitute_data = requests.get(URL_CATEGORY.format(category_name, str(page)))
                        try:
                            assert substitute_data.status_code == 200
                        except AssertionError:
                            print("""Warning ! There is a problem with the HTTP request for the category to the API.
                                Category : {}""".format(category_name))
                        i = 0
                    try:
                        possible_sub_nutriscore = substitute_data.json()["products"][i]["nutrition_grades"]
                    except:
                        i += 1
                    else:
                        if ord(possible_sub_nutriscore) < ord(nutriscore):
                            possible_sub_name = substitute_data.json()["products"][i]["product_name_fr"]
                            if possible_sub_name in [food.substituted_product_name for food in FoodSubstituted.select()]:
                                i += 1
                            else:
                                break
                        else:
                            i += 1
                code = substitute_data.json()["products"][i]["code"]
                substitute_name = substitute_data.json()["products"][i]["product_name_fr"]
                if len(substitute_name) >= 50:
                    list_words = substitute_name[:50].split()
                    del list_words[-1]
                    substitute_name = " ".join(list_words)
                try:
                    description = substitute_data.json()["products"][i]["generic_name_fr"]
                except:
                    description = ""
                try:
                    stores = substitute_data.json()["products"][i]["stores"]
                except:
                    stores = ""
                link = "https://fr.openfoodfacts.org/produit/" + code

                with db.atomic() as transaction:
                    new_food = FoodSubstituted.create(product_name=food_name, substituted_product_name=substitute_name,
                        description=description, stores=stores, link=link, id_category=new_category)

db.close()