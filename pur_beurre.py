"""
This is the main script of the project. Double-click on it to start the
program.
"""

#Standard library
import time

#External library

#Local library
from import_data_from_the_API_to_the_database.create_database import db, Category, FoodSubstituted
from functions import *

print("""Bonjour cher(e) utilisateur(trice) ! Que puis-je faire pour vous aujourd'hui...""")

ACTIVE = True
while ACTIVE :
    choice = input("""1 - Quel aliment souhaitez-vous remplacer ?\n2 - Retrouver mes aliments substitués.""")

    if choice == "1":
        with db:
            categories = Category.select()

        selected_category = select(categories, "Catégories :")

        with db:
            list_food = FoodSubstituted.select().join(Category).where(Category.id == selected_category.id)

        selected_food = select_food(list_food, """Aliments de la categorie '{}'' :""".format(selected_category.name))

        display_food(response_food)

        save_substitute(response_food)

        while True:
            print("""Voulez-vous revenir à l'écran d'accueil (=tapez 1) ou quittez le programme (=tapez 2)?""")
            choice = input()
            try:
                choice = int(choice)
            except ValueError:
                print("""Vous n'avez pas entré un nombre. Veuillez recommencer...""")
            else:
                if choice == 1:
                    break
                elif choice == 2:
                    ACTIVE=False
                    break
                else:
                    print("""Vous n'avez pas entré un nombre correct. Veuillez recommencer...""")
    elif choice == "2":
        pass
        ACTIVE=False
    else:
        print("""Oops, vous n'avez pas entré une commande valide. Veuillez recommencer...""")      

print("""Au revoir cher(e) utilisateur(trice) ! A bientôt !""")
time.sleep(2)