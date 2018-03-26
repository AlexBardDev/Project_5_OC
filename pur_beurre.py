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
    print("""1 - Quel aliment souhaitez-vous remplacer ?\n2 - Retrouver mes aliments substitués.""")
    choice = input()

    if choice == "1":
        with db:
            categories = Category.select()

        selected_category = select(categories, "Catégories :")

        with db:
            list_food = FoodSubstituted.select().join(Category).where(Category.id == selected_category.id)

        selected_food = select(list_food, """Aliments de la categorie '{}'' :""".format(selected_category.name))

        display_food(selected_food)

        if save_substitute(selected_food) == True:
            with db:
                modified_food = FoodSubstituted.update(is_saved=True).where(FoodSubstituted.id == selected_food.id)
                modified_food.execute()

        if finish() == True:
            ACTIVE = False

    elif choice == "2":
        with db:
            list_saved_sub = FoodSubstituted.select().where(FoodSubstituted.is_saved == True)

        selected_sub = select(list_saved_sub, "Vos aliments favoris sont :")

        display_food(selected_sub)

        if finish() == True:
            ACTIVE = False
    else:
        print("""Oops, vous n'avez pas entré une commande valide. Veuillez recommencer...""")      

print("""Au revoir cher(e) utilisateur(trice) ! A bientôt !""")
time.sleep(2)