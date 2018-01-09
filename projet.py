# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:38:20 2017

@author: gelina
"""

import csv
import datetime
import urllib.request
import urllib
import json
import config
import math


def valid_parstation_parjour(FICHIER):
	"""
     Compte le nombre de validations total pour n'importe quel jour
     donné en une sation donnée
 
     Args:
         le fichier csv des données
 
     Returns:
         dictionaire des données

	 >>> d = valid_parstation_parjour('validations.csv'):
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











def weekdaydetection(dico):
	"""
     sépare le jeu de donnée en 2 : les jours de la semaine et les autres
 
     Args:
         le dictionaire créé par la fonction valid_parstation_parjour
 
     Returns:
         liste de 2 dictionaires des données
         le 1er element (l[0]) de la liste est les jours de le semanine
         le 2eme (l[1]) les jours en weekend

	 >>> d = valid_parstation_parjour('validations.csv'):
     >>> l = weekdaydetection(d)
	 >>> '2017-01-01' in l[0]
	 False
	 >>> '2017-01-02' in l[1]
	 False
	 >>> '2017-01-03' in l[0]
	 True
	 >>> '2017-02-12' in l[1]
	 True

     """
	l = list()
	weekday = dict()
	weekend = dict()
	#On crée ici deux dictionaires et une liste
	# Les deux dictionaires contiennent soit les elements des jours qui tombent pendant une semeine ou ceux qui tombent un weekend

	for day in dico.keys():
		dayofweek = datetime.date(int(day[0:4]),int(day[5:7]),int(day[8:10])).isoweekday()
		# pour chaque date on va extraire de la string l'année, le mois et le jour
		# on construit avec cela un objet date et on appelle son attribut isoweekday ( pour lundi, 7 pour dimanche)


		if dayofweek < 6: 
			weekday[day] = dico[day]
			#si c'est un jour de semaine, le ranger dans le dictionnaire semaine

		else :
			weekend[day] = dico[day]
			# si c'est un jour de WE , le ranger dans le dico weekend

	l.append(weekday)
	l.append(weekend)

	#on met les deux dico dans l et on retourne la liste
	return l



def moyennesurannee(dico):

	moyennesta = dict()
	for day in dico.keys():
		for station in dico[day].keys():
			if station in moyennesta:
				moyennesta[station] += dico[day][station]
			else:
				moyennesta[station] = dico[day][station]

	for station in moyennesta.keys():
		moyennesta[station] = math.ceil(moyennesta[station]/len(dico.keys()))

	return moyennesta



def proportionnavigo_station():

	print(todo)








def build_histo():

	print(todo)



def build_stations_coordonates(dico):

	#TODO : ERROR HANDLING
	#IDEE : utiliser les données du STIF plutot que Google Maps (plus precis)

	randomday = list(dico.keys())[0] # on cherche un jour au hasard dans notre jeu de donnée
	stations_loc = dict()
	apikey = config.API_GMAPS_GEOCODE # on recupere la clef d'api du fichier de config.py
	baseURL = 'https://maps.googleapis.com/maps/api/geocode/json?key='+apikey+'&address='

	for station in dico[randomday].keys(): # on extrait la liste des noms des stations
		URL = baseURL + urllib.parse.quote(station) #On forme une URL complete et dans un format correct ( remplacer les espaces et caracs spéciaux )
		URLObject = urllib.request.urlopen(URL)
		data = json.loads(URLObject.read().decode()) # on ouvre et convertit le JSON

		if data['status'] != "OK":
			print("l'api n'a pu localiser",station) # on cherche le code de retour pour voir si tout c'est bien passé
		
		else:
			lati = data['results'][0]['geometry']['location']['lat'] #on extraie latitude et longitude dans des variables
			longi= data['results'][0]['geometry']['location']['lng']
			stations_loc[station]=[lati,longi] # On stocke les coordonées de la station dans le dictionaire

	return stations_loc










def main():
    dic = valid_parstation_parjour('validations.csv')
    l= weekdaydetection(dic)
    moy = moyennesurannee(dic)
    print (moy)
    #geo = build_stations_coordonates(dic)
    pass

if __name__ == '__main__':
    main()