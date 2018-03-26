#Local library
from import_data_from_the_API_to_the_database.create_database import db, Category, FoodSubstituted

def valid_input(list_objects, data_input):
    """This functions checks if the input is valid or not."""
    
    is_valid = False
    try:
        data_input = int(data_input)
    except ValueError:
        print("""Vous n'avez pas saisi un nombre. Veuillez recommencer...""")
    else:
        if data_input not in [elt.id for elt in list_objects]:
            print("""Vous avez saisi un nombre incorrect. Veuillez recommencer...""")
        else:
            is_valid = True

    return is_valid

def select(list_objects, message):
    """pass"""

    while True:
        print(message)
        for elt in list_objects:
            print("""{} - {}""".format(elt.id, elt.name))
        choice = input("""Votre choix : """)
        if valid_input(list_objects, choice) == True:
            break

    return [elt for elt in list_objects if elt.id == int(choice)][0]

def display_food(food):
    """This function displays all the information saved in the database about
    the selected food."""

    print("""Voici le résultat de votre sélection :""")
    print("""Aliment à substituer : {}. Substitut plus sain : {}.""".format(food.product_name, food.substituted_product_name))

    if food.description != "":
        print("""Voici une description plus complète du substitut : {}""".format(food.description))
    
    if food.stores != "":
        print("""Vous pouvez trouvez ce produit dans le(s) magasin(s) suivant(s) : {}""".format(food.stores))

    print("""Pour plus d'informations, voici la page complète du substitut : {}""".format(food.link))

def save_substitute(food):
    """pass"""

    if food.is_saved == True:
        print("""Ce substitut est déjà enregistré dans vos favoris.""")
    else:
        print("""Ce substitut n'est pas encore enregistré dans vos favoris.""")
        print("""Voulez-vous l'enregistrer (=tapez 1) ou non (=tapez 2) ? """)
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("""Vous n'avez pas saisi un nombre. Veuillez recommencer...""")
        else:
            if choice == 1:
                db.connect()
                modified_food = FoodSubstituted.update(is_saved=True).where(FoodSubstituted.id == food.id)
                modified_food.execute()
                db.close()
                print("""Ce subsitut est maintenant dans vos favoris.""")
            elif choice == 2:
                print("""Très bien, le substitut ne sera pas enregistré dans vos favoris.""")
            else:
                print("""Vous avez saisi un nombre incorrect. Veuillez recommencer...""")




#Mettre le texte dans les input    