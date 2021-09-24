from random import randint
#créer une liste d'options de jeu
t = ["Rock", "Paper", "Scissors"]

#attribuer une lecture aléatoire à l'ordinateur
ordinateur = t[randint(0,2)]

#définir le Joueur sur False
joueur = False

while joueur == False:
#set joueur to True
    joueur = input("Rock, Paper, Scissors?")
    if joueur == ordinateur:
        print("Lien avec l'oridinateur!")
    elif joueur == "Rock":
        if ordinateur == "Paper":
            print("Tu as perdu!", ordinateur, "couvre", joueur)
        else:
            print("Vous avez gagner!", joueur, "écrase", ordinateur)
    elif joueur == "Paper":
        if ordinateur == "Scissors":
            print("Tu as perdu!", ordinateur, "couper", joueur)
        else:
            print("Vous avez gagner!", joueur, "couvre", ordinateur)
    elif joueur == "Scissors":
        if ordinateur == "Rock":
            print("Tu as perdu...", ordinateur, "écrase", joueur)
        else:
            print("Vous avez gagner!", joueur, "couper", ordinateur)
    else:
        print("Ce n'est pas un jeu valide. Vérifie ton orthographe!")
    #joueur a été défini sur True, mais nous voulons qu'il soit False afin que la boucle continue
    joueur = False
    ordinateur = t[randint(0,2)]