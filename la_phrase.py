#!/usr/bin/env python3
import re

def verif_mot(mot):
	return re.match("[A-Z0-9]\w*", mot)

def verif_phrase(phrase):
	mots = phrase.split(" ")
	for mot in mots:
		if verif_mot(mot):
			continue
		else:
			return False
	return True
	
toto = input("Entrez : ")
print(verif_phrase(toto))
#print("toto")
