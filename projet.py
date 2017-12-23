# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:38:20 2017

@author: gelina
"""

import csv


def valid_parstation_parjour(FICHIER):
	"""
     Compte le nombre de validations total pour n'importe quel jour
     donné en une sation donnée
 
     Args:
         le fichier csv des données
 
     Returns:
         dictionaire des données

	 >>> valid_parstation_parjour(validations.csv):
     >>> d['2017-05-10']['LES HALLES']
	 41413
     """
	with open(FICHIER, 'r') as f:
		r = csv.reader(f,delimiter=';')
		l = list(r) # l'itérable est converti en liste
		
		d = dict() # on costruit un dictionnaire qui mettra en relation un jour et toutes les données de ce jour
		for line in l[1:]:
		     if(line[0] in d):
		             d[line[0]]+= [[line[4],line[6],line[7]]] #on ajoute si la date est deja dans le dictionaire
		     else:
		             d[line[0]]= [[line[4],line[6],line[7]]] # on crée l'entrée sinon
		
		for date in d.keys():
		     s = dict() # on crée un nouveau dictionaire par jour qui assosiera les stations et leur nbre de visiteur
		     for line in d[date]:
		         if(line[0] in s):
		                 if (line[2] == 'Moins de 5'):
		                 	s[line[0]]+=4
		                 	# le STIF met la mention moins de 5 pour des raisons d'anonymat
		                 else:
		                 	s[line[0]]+=int(line[2]) #on ajoute si le dictionnaire contient deja la station pour ce jour
		         else:
		                 if (line[2] == 'Moins de 5'):
		                 	s[line[0]]=4
		                 	# le STIF met la mention moins de 5 pour des raisons d'anonymat
		                 else:
		                 	s[line[0]]=int(line[2]) # on definit la station dans le dictionnaire sinon
		     d[date] = s 
		return d





def main():
    valid_parstation_parjour('validations.csv')
    pass

if __name__ == '__main__':
    main()