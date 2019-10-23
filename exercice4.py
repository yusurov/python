#!/usr/bin/env python

saisie = input()

#creation dictionaire
def count_voyelles(phrase):
#avec les cles aeyuio
	voyelles = {'a':0, 'e':0, 'y':0, 'u':0, 'o':0, 'i':0}
#creer un boucle pour sortire tout les voyelles de text
	for lettre in phrase:
#compter tout les quelle il a trouver dans text
		if lettre in voyelles:
			voyelles[lettre]+=1
#pour vaoir le resultat de def count_voyelles
	return voyelles

#saisie = input()
print(count_voyelles(saisie))

