"""
This is the main script of the project. Double-click on it to start the
program.
"""

#Standard library
import time

#Local library
from import_data_from_the_API_to_the_database.create_database import db, Category, FoodSubstituted
from functions import user_selection, display_food, save_substitute, finish

print("""Bonjour cher(e) utilisateur(trice) ! Que puis-je faire pour vous aujourd'hui...""")

#The loop of the program
ACTIVE = True
while ACTIVE:

    print("""1 - Quel aliment souhaitez-vous remplacer ?\n2 - Retrouver mes aliments substitués.""")
    choice = input()

    #If the user wants to find a new substitute
    if choice == "1":
        #Get all the categories from the database
        with db:
            categories = Category.select()

        #The user selects a category
        selected_category = user_selection(categories, "Catégories :")

        #Get all products related to the right category
        with db:
            list_food = FoodSubstituted.select().join(Category).where(Category.id ==
                                                                      selected_category.id)

        #The user selects food
        selected_food = user_selection(list_food,
                                       """Aliments de la categorie '{}'' :""".format(selected_category.name))

        #Display the data
        display_food(selected_food)

        #Save the product in the bookmarks if necessary
        if save_substitute(selected_food) == True:
            with db:
                modify_food = FoodSubstituted.update(is_saved=True).where(FoodSubstituted.id ==
                                                                          selected_food.id)
                modify_food.execute()

        #Finish the program or restart at the begin
        if finish() == True:
            ACTIVE = False

    #If the user wants to see all already subsituted products
    elif choice == "2":
        #Get all bookmarks
        with db:
            list_saved_sub = FoodSubstituted.select().where(FoodSubstituted.is_saved == True)

        #The user selects the bookmark that he wants
        selected_sub = user_selection(list_saved_sub, "Vos aliments favoris sont :")

        #Display th data
        display_food(selected_sub)

        #Finish the program or restart at the begin
        if finish() == True:
            ACTIVE = False

    #If the input is not valid
    else:
        print("""Oops, votre commande n'est valide. Veuillez recommencer...""")

#The end of the program
print("""Au revoir cher(e) utilisateur(trice) ! A bientôt !""")
time.sleep(2)
