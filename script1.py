import requests
from script_peewee import db, FoodSubstituted


r = requests.get("https://fr.openfoodfacts.org/api/v0/produit/3229820793665.json")

if r.status_code == 200:
    nom = r.json()["product"]["product_name_fr"]
    nom_generic = r.json()["product"]["generic_name_fr"]
    magasin = r.json()["product"]["stores"]
else:
    print("erreur")

db.connect()

aliment2 = FoodSubstituted.create(product_name=nom,
    substituted_product_name="inconnu", description="Blablabla",
    stores=magasin, link="https://fr.openfoodfacts.org")

db.close()
