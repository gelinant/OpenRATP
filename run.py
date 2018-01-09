# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:37:25 2018

@author: gelina
"""

import projet
import GUI






def main():
    dic = projet.valid_parstation_parjour('validations.csv')
    l= projet.weekdaydetection(dic)
    moy = projet.moyennesurannee(l[0])
    l = projet.split_hist_data(moy, 12000)
    
    GUI.build_histo(l[0])
    GUI.build_histo(l[1])
    return moy
    #geo = build_stations_coordonates(dic)
    pass

if __name__ == '__main__':
    main()