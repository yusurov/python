#!/usr/bin/env python3

class Plante:
	def 	_init__(self, racine, couleur):
		self.racine = racine
		self.couleur = couleur

	def	couper(self):
		self.racine = None

	def 	changer_couleur(self, couleur):
		self.couleur = couleur

	def	get_couleur(self, 
class Arbre():
	def	__init__(self, racine, feuillage):
	#Plante.__init__(self, racine, feuillage)

	def	get.racine = racine
		return self.racine

	def	hiver(self)
		self.couleur = None

class Fleur(Plante):
	def	 __init__(self, racine, petales, couleur):
		self.racine = racine	
		self.petales = petales
		self.color = couleur
	def	couper(self):
		self.racine = None
	def	retirer_petailes(self, nb_petales):
		self.petales = self.peatles-nb_petales
	def	changer_color(self, couleur):
		if couleur in ("bleu", "jeune", "vert"):
			self.color = couleur


fleur = Fleur("toto", 24, "bleue")
tulipe = Fleur("tata", 100, "blue")
tulipe.changer_color("orange")
print(tulipe.color)
	 		
