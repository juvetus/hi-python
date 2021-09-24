import random
# Bibliotheque utliser pour choisir les mots aleatoire

 
name = input("Quel est votre nom? ")
# Ici je demande à l'utilisateur de rentrer son nom
 
print("Bonne Chance ! ", name)
 
words = ['soleil', 'ordinateur', 'science', 'programmation',
         'python', 'mathematiques', 'joueur', 'condition',
         'nuage', 'eau', 'planche', 'geeks']
 

#Cette function va choisir un mot aleatoirement dans notre liste

mot = random.choice(words)
 
 
print("Devinez les mots")
 
suppositions = ''
 
# Ici le nombre de tours
tours = 12
 
 
while tours > 0:
     
    # compte le nombre de fois qu'un utilisateur échoue
    failed = 0
     
    # tous les caractères de l'entrée
    # mot en prenant un à la fois.
    for char in mot:
         
        # compare ce caractaire avec celui
        # supposer
        if char in suppositions:
            print(char)
             
        else:
            print("_")
             
            # Pour chaque echec noua allons ecrementé de 1
            
            failed += 1
             
 
    if failed == 0:
       
        print("Vous avez Gagné")
         
        # Ceci imprime le mot correct
        print("Le mot est: ", mot)
        break
     
    # Si l'utilisateur a saisi la mauvaise lettre, alors
    # il demandera a l'utilisateur d'entrée une nouvelle lettre
    deviner = input("deviner une lettre:")
     
    # chaque caractère d'entrée sera stocké dans les suppositions
    suppositions += deviner
     
    # vérifier l'entrée avec le caractère dans le mot
    if deviner not in mot:
         
        tours -= 1
         
        # si le caractère ne correspond pas au mot
        # alors "Wrong" sera donné en sortie
        print("Wrong")
         
        # cela imprimera le nombre de
        # tourne à gauche pour l'utilisateur
        print("Vous avez", + tours, 'plus de suppositions')
         
         
        if tours == 0:
            print("Vous avez perdu")