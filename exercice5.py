#!/usr/bin/env python

def compte_lignes(contenu):
	nb_lignes = len(contenu.split("\n"))
	return nb_lignes

def compte_mots(ligne):
	nb_mots = len(ligne.split(" "))
	return nb_mots

def compte_mots_et_lignes(contenu):
	nb_mots = 0
	nb_lignes = compte_lignes(contenu)
	for ligne in contenu.split("\n"):
		nb_mots += compte_mots(ligne)
	print("mots : "+str(nb_mots)+" lignes : "+str(nb_lignes))

with open("./text.txt", "r") as f:
	contenu_fichier = f.read()
compte_mots_et_lignes(contenu_fichier)










