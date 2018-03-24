"""
This is the main script of the project. Double-click on it to start the
program.
"""
import time

print("""Bonjour cher(e) utilisateur(trice) ! Que puis-je faire pour vous aujourd'hui...""")

ACTIVE = True
while ACTIVE :
    print("""1 - Quel aliment souhaitez-vous remplacer ?""")
    print("""2 - Retrouver mes aliments substitués.""")
    choice = input()

    if choice == "1":
        pass
        ACTIVE=False
    elif choice == "2":
        pass
        ACTIVE=False
    else:
        print("""Oops, vous n'avez pas entré une commande valide. Veuillez recommencer...""")

print("""Au revoir cher(e) utilisateur(trice) ! A bientôt !""")
time.sleep(3)