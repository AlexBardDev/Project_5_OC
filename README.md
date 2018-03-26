# Project_5_OC
This code uses the OpenFoodFacts API and a MySQL database to give a substitute to not healthy food and to register it. It's the 5th project to complete my degree with **OpenClassrooms**. 

For this project, a fictional start-up called "Pur Beurre" needs a program where people can find a more healthy substitute and register it.

# This repo
This repository contains 5 files and 1 folder. The files are :
  - .gitignore to ignore such elements as 'env/' or '__pycache__/'
  - README.md to give you information about the project.
  - requirements.txt to give you all the libraries that are used by the scripts.
  - pur_beurre.py to start the program. Just double-click on it.
  - functions.py to use some functions required for pur_beurre.py.

The folder is :
  - import_data_from_the_API_to_the_database : it contains the scripts that download the data and save them in the database.

# Quickstart
First, go inside the folder called *"import_data_from_the_API_to_the_database"*. Then, you have to be connected to a MySQL database. Do the queries that are in the *'pur_beurre_db.sql'*. It will creates the database and a specific user. After that, run *'create_database.py'*. It will creates all the tables and the constraints(=Primary Key, Foreign Key,...).

For this project, I use an ORM called *'peewee'*. The ORM is a better solution than only a basic *'python-mysql driver'* because with the ORM, the code is more portable. With 1 line, you can change easily the database to PostgreSQL for example. 

Finally, run *'download_data_from_the_API.py'*. It will automatically imports the data from the API to the MySQL database.

Now, go in the parent folder and run *'pur_beurre.py'*. With the user interface, you can choose food and the program will give you a better substitute. You can also register the substitute.

# Feature 1 : select food
When you start the program, 2 options will be displayed. Enters "1". Then, you will see ten different categories related to ten different numbers. Select the category you need by entering the right number.

Now, you should see a list of food. Again, enters the related number. And that's it ! You can see now all the information about the chosen product.

This "user path" is compulsory by OpenClassrooms.

# Feature 2 : Save a healthier substitute
When you see the information about a product and its substitute, you also have a message telling you if the substitute is already registered or not in your bookmarks.

If it's not, you can register the substitute in your bookmarks.