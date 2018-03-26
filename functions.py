#Local library
from import_data_from_the_API_to_the_database.create_database import db, Category, FoodSubstituted

def valid_input(data_input):
    """This functions checks if the input is valid or not."""
    
    is_valid = False
    try:
        data_input = int(data_input)
    except ValueError:
        print("""Vous n'avez pas saisi un nombre. Veuillez recommencer...""")
    else:
        is_valid = True

    return is_valid

def select(list_objects, message):
    """pass"""

    while True:
        print(message)
        for i, elt in enumerate(list_objects):
            print("""{} - {}""".format(i+1, elt.name))
        choice = input("""Votre choix : """)
        if valid_input(choice) == True:
            if int(choice) in range(1, len(list_objects)+1):
                break
            else:
                print("""Vous avez saisi un nombre incorrect. Veuillez recommencer...""")

    return list_objects[int(choice)-1]

def display_food(food):
    """This function displays all the information saved in the database about
    the selected food."""

    print("""Voici le résultat de votre sélection :""")
    print("""Aliment à substituer : {}. Substitut plus sain : {}.""".format(food.name, food.substituted_product_name))

    if food.description != "":
        print("""Voici une description plus complète du substitut : {}""".format(food.description))
    
    if food.stores != "":
        print("""Vous pouvez trouvez ce produit dans le(s) magasin(s) suivant(s) : {}""".format(food.stores))

    print("""Pour plus d'informations, voici la page complète du substitut : {}""".format(food.link))

def save_substitute(food):
    """pass"""

    change = False

    if food.is_saved == True:
        print("""Ce substitut est déjà enregistré dans vos favoris.""")
    else:
        while True:
            choice = input("""Ce substitut n'est pas encore enregistré dans vos favoris.\nVoulez-vous l'enregistrer (=tapez 1) ou non (=tapez 2) ? """)
            if valid_input(choice) == True:
                if choice == "1":
                    print("""Ce subsitut est maintenant dans vos favoris.""")
                    change = True
                    break
                elif choice == "2":
                    print("""Très bien, le substitut ne sera pas enregistré dans vos favoris.""")
                    break
                else:
                    print("""Vous avez saisi un nombre incorrect. Veuillez recommencer...""")

    return change

def finish():
    """pass"""

    while True:
        choice = input("""Voulez-vous revenir à l'écran d'accueil (=tapez 1)\nou quittez le programme (=tapez 2) ? """)
        if valid_input(choice) == True:
            if choice == "1":
                response = False
                break
            elif choice == "2":
                response = True
                break
            else:
                print("""Vous n'avez pas entré un nombre correct. Veuillez recommencer...""")

    return response



#Mettre le texte dans les input    