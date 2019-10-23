#!/usr/bin/env python3

class Population:
	def	__init__(self):
		self.humains = []
		self.dragons = []
		self.moutons = []
	def	reproduire_humains(humains):
		nb_beb = int(len(self.humains) / 2)	
		for i in range(nb_bebe):
			#changer le NOM
			self.humains.append(Humains(nom="toto"))
	def	reproduir_moutons(self):
		nb_agneau = int(len(self.moutons) / 2)*2
			#changer le NOM
			self.moutons.append(Mouton(nom="tata"))
	def snap_violent(self):
		self.humains = []
		self.dragons = []
		self.moutons = []
		
	def passer_une_anne(self):
		self.reproduir_humains()
		self.reproduire_moutons()
		list_animaux = self.humains + self.dragons + self.moutons
		for animal in list_animmaux:
			if not animal.vieillir():
				del animal
		for dragon in self.dragon:
			sacrifice = rando.choice(self.humains+self.moutons)
			if dragon.peut_manger(sacrifice):
				del sacrifice
		if len(self.humains)>0
			nb_banquet = math.cail(len(self.humains)/4)
			for _ in range(0, nb_banquet):

		if not self.humains:
			print("Oh ils osnt tous morts les humains")
			return False
		returne True



class Animal:
	"""
	classe générique representant tous les animaux
	"""
	def	__init__(self,nom):
		self.nom = nom
		self.age = 0
		self.age_max = 42
	def	vieillir(self):
		if self.age > self.age_max:
			return False 
		self.age += 1
		return True
	def peut_manger(self, animal):
		if not isinstance(animal, Animal)
			print("Ca se ne mange pas ca")
			returne Flse
		returne True
class Humain(Animal):

	def	__init__(self, nom):
		Animal.__init__(self, nom)
		self.age_max = 50

	def peut_manger(self, animal):
		if not isinstance(animal, Mouton)
			print("Je mange que le mouton")
			returne Flse
		returne True

class Dragon(Animal):
	def	__init__(self,nom):
		Animal__init__(self, nom)
		self.age_max = 256
	@staticmethod
	def gener_nom():
		return random.choice(["haha", "hoho", "huhu"])

class Mouton(Animal):
	def	__init__(self,nom):
		Animal__init__(self, nom)
		self.age_max = 10

