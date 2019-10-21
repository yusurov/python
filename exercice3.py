#!/usr/bin/env python

var = 'adroit#0a3#1vroom#b52#1colorant#e111'
text = (var.split('#'))
results = []

#print(text)

for i in text: 

#if end of the word end in numbers or others signes
#	if i[-1] in "0123456789":

#find if end of word is digit
#	if i[-1].isdigit(): 

	if i[0].isalpha():
#find the t in the last sing of the word 
#	if i[-1] == 't': #find the t in the last sing of the word 
		print(i)
#to seperate the resultat with ;
#print(";".join(text))	
