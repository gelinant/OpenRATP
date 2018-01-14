# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:37:25 2018

@author: gelina
"""

import projet
import GUI

def buildhisto(code):
    dic = projet.valid_parstation_parjour('valid1.csv')
    l= projet.weekdaydetection(dic)
    if code[0:2] == 'se':
        moy = projet.moyennesurannee(l[0])
    if code[0:2] == 'we':
        moy = projet.moyennesurannee(l[1])
    l = projet.split_hist_data(moy, 12000)
    if code[2:3] == '1':
        GUI.build_histo(l[0])
    if code[2:3] == '2':
        GUI.build_histo(l[1])



def buildmap(code):
    dic = projet.valid_parstation_parjour('valid1.csv')
    l= projet.weekdaydetection(dic)
    if code == 'se':
        moy = projet.moyennesurannee(l[0])
    if code == 'we':
        moy = projet.moyennesurannee(l[1])
    geo = projet.build_stations_coordonates("gares.csv")
    md = projet.build_map_data(geo,moy)
    GUI.build_map(md)




