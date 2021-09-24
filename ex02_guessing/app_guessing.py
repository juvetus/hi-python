from random import randint
nombre_a_deviner = str(randint(1,100))
#print(nombre_a_deviner)

print('Hello , Vous devez deviner un nombre entre 1 et 100')
print('Vous avez 8 essais')


nombre_essais = 8
i=0

while i < nombre_essais:
	essai = input('Entrez un nombre ({0} ere essai) :'.format(i+1))
	if essai < nombre_a_deviner:
		print('Le nombre à devener est plus grand {0}'.format(essai))
		print('essaie encore')
	elif essai > nombre_a_deviner:
		print('Le nombre à deviner est plus petit que {0}'.format(essai))
	elif essai == nombre_a_deviner:
		print('Bravo vous avez Gagner en {0} essai(s)'.format(i+1))
		break
	i +=1

if essai != nombre_a_deviner:
	print('Vous avez perdu')
	print('Le nombre à deviner etait: {0}'.format(nombre_a_deviner))
print('Fin du Jeu')