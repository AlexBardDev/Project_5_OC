"""
This script contains 5 functions. 4 of them are used by 'pur_beurre.py'. But
the first one is used in this script to check if the inouts are valid or not.
"""

def valid_input(data_input):
    """This function checks if the input is valid or not. It takes the input
    and it returns a boolean."""

    is_valid = False
    try:
        data_input = int(data_input)
    except ValueError:
        print("""Vous n'avez pas saisi un nombre. Veuillez recommencer...""")
    else:
        is_valid = True

    return is_valid

def user_selection(list_objects, message):
    """This function helps the user to make a choice. It displays all the
    possibilities and returns the user's choice. It takes a list of objects
    and a message to display. It returns the object selected by the user."""

    while True:

        #Display the possibilities
        print(message)
        for i, elt in enumerate(list_objects):
            print("""{} - {}""".format(i+1, elt.name))

        #The user enters an input
        choice = input("""Votre choix : """)

        #Check that the input is correct. If not, it restarts the loop
        if valid_input(choice) == True:
            if int(choice) in range(1, len(list_objects)+1):
                break
            else:
                print("""Vous avez saisi un nombre incorrect. Veuillez recommencer...""")

    return list_objects[int(choice)-1]

def display_food(food):
    """This function displays all the information saved in the database about
    the selected product. It takes 1 parameter : an object coming from the
    database."""

    print("""Voici le résultat de votre sélection :""")
    print("""Aliment à substituer : {}. Substitut plus sain : {}."""
          .format(food.name, food.substituted_product_name))

    if food.description != "":
        print("""Voici une description plus complète du substitut : {}""".format(food.description))

    if food.stores != "":
        print("""Vous pouvez trouvez ce produit dans le(s) magasin(s) suivant(s) : {}"""
              .format(food.stores))

    print("""Pour plus d'informations, voici la page complète du substitut : {}"""
          .format(food.link))

def save_substitute(food):
    """This function check if the substitute is saved in the bookmarks or not.
    If not, it gives the possibility to save it. It takes 1 parameter : a
    'food' object coming from the database. It retuns a boolean."""

    change = False

    #Is already saved in the bookmarks
    if food.is_saved == True:
        print("""Ce substitut est déjà enregistré dans vos favoris.""")
    #Is not already saved
    else:
        while True:
            #The user entres something
            choice = input("""Ce substitut n'est pas encore enregistré dans vos favoris.
                           \nVoulez-vous l'enregistrer (=tapez 1) ou non (=tapez 2) ? """)

            #Check if the input is valid
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
    """This function takes no parameters and returns a boolean. With this
    function, we know if the user wants to leave the program or continue."""

    while True:
        #The users enters the choice
        choice = input("""Voulez-vous revenir à l'écran d'accueil (=tapez 1)
                       \nou quittez le programme (=tapez 2) ? """)

        #Check that the input is valid
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
