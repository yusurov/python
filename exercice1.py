#!/usr/bin/env python3
import random
noms = ["nom1", "nom2", "nom3"]
prenom = ["prenom3", "prenom2", "prenom1", "prenom4"]
print (noms[0] + " " + prenom[4])
print (noms[1] + " " + prenom[1])
print (noms[2] + " " + prenom[0])
id_noms_aleatoire = random.randint(0,len(noms)-1)
id_prenom_aleatoire = random.randint(0,len(prenom)-1)
print(noms[id_noms_aleatoire]+" "+prenom[id_prenom_aleatoire])

