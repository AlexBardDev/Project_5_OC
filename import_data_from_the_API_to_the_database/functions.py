"""
This scripts contains 4 functions used for downloading data from the API.
"""

#External library
import requests

def give_a_name(data):
    """This function takes 1 parameter : an HTTP request object. It returns
    the name of the product."""

    #Try to assign a value
    try:
        name = data.json()["product"]["product_name_fr"]
    #If the key 'product_name_fr' doesn't exist
    except KeyError:
        name = data.json()["product"]["product_name"]

    return name

def find_a_substitute(url, category_name, nutriscore, list_already_substituted_food):
    """This function finds a new substitution. It takes 4 parameters : an url for
    the HTTP request, the category name of the product, the nutriscore of the
    product and a list of all the substitution. It returns the right HTTP request
    object and an index i."""

    #Some variables for this function
    page = 1
    i = 0

    #Get the information about the category with an HTTP request
    substitute_data = requests.get(url.format(category_name, str(page)))

    #If there is a problem with the HTTP request
    if substitute_data.status_code != 200:
        print("""Warning ! There is a problem with the HTTP request to the API for the category.
            Category : {}""".format(category_name))
    else:
        #A loop for finding a new healthy substitution
        while True:

            #It is the end of the page
            if i == 19:
                #Get the following page
                page += 1
                substitute_data = requests.get(url.format(category_name, str(page)))
                #If there is a problem with the HTTP request
                if substitute_data.status_code != 200:
                    print("""Warning ! There is a problem with the HTTP request to the API for the
                        category. Category : {}""".format(category_name))
                #Start again with the first product
                i = 0

            #Try to get the nutriscore of healthier food
            try:
                possible_sub_nutriscore = substitute_data.json()["products"][i]["nutrition_grades"]
            #This product doesn't have a nutriscore. So, we go further.
            except KeyError:
                i += 1
            #Check that the nutriscore is better and that the substitution is a new aliment
            else:
                if ord(possible_sub_nutriscore) < ord(nutriscore):
                    possible_sub_name = substitute_data.json()["products"][i]["product_name_fr"]
                    if possible_sub_name in list_already_substituted_food:
                        i += 1
                    else:
                        break
                else:
                    i += 1

    return substitute_data, i

def shorten_string(string):
    """This function take a string as a parameter. It returns a shorter
    string that fits in the database."""

    #Cut the final part of the string
    list_words = string[:50].split()
    del list_words[-1]
    new_string = " ".join(list_words)

    return new_string

def assign_a_value(data, i, keys):
    """This function takes 3 parameters : an HTTP request object, a number and
    a list of strings. These strings should be the keys of the 'json'
    dictionnary. It returns the assigned value from the dictionnary or an
    empty string."""

    #An empty string
    content = ""

    #Try to find a value using the keys of the dictionnary
    for key in keys:
        try:
            content = data.json()["products"][i][key]
        except KeyError:
            pass
        else:
            break

    return content
