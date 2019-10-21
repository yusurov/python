#!/usr/bin/env python
annee = int(input("type the year : "))
if (annee%4 == 0) and ( annee%100!=0 or annee%400==0 ):
    print("c'est une annee bisextile")
else:
    print("c'est une annee ne pas bisextile")

