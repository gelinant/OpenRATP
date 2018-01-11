# -*- coding: utf-8 -*-
"""
Created on Jan 02 17:15:42 2017

@author: Antoine Gélin
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def build_map(dico):
    """
    Construit la carte des stations

    Args:
     

    Returns:
     

    >>> 
    
    """
  #   MY_MAP = Basemap(lon_0=2.579747,lat_0=48.8411547,width=9999,height=9999,
  # resolution='c', projection='merc', epsg=27571)

 #     MY_MAP = Basemap(lon_0=2.344589,lat_0=48.851824,width=9999,height=9999,
 # rsphere=(6378137.00, 6356752.3142), resolution='i', projection='merc',area_thresh = 0.1, epsg=27571)


    # MY_MAP = Basemap(llcrnrlon=1.450561, llcrnrlat=48.136375, urcrnrlon=3.550762, urcrnrlat=49.240305,
 # rsphere=(6378137.00, 6356752.3142), resolution='i', projection='merc',area_thresh = 0.1, epsg=27571)

    MY_MAP = Basemap(llcrnrlon=-2.5, llcrnrlat=45, urcrnrlon=2.5, urcrnrlat=50,
 rsphere=(6378137.00, 6356752.3142), resolution='i', projection='merc',area_thresh = 0.1, epsg=27571)
    # les coordonnées sont centrées sur l'ile de France sur un e projection mercator. on peut faire varier la resolution de l'image générée

    # UTILISER DES SHAPEFILES OU PLUS SIMPLEMENT UTILISER UNE VUE EN LIGNE TYPE GMAPS OU OPENSTREETMAPS SERAIT PLUS PERTINENT
    # RESOLUTION TROP PETITE


    
    # MY_MAP.drawparallels()
    # MY_MAP.drawmeridians()
    
    MY_MAP.drawrivers()
    MY_MAP.arcgisimage(xpixels =1500 , verbose = True)
    plt.show()








def build_histo(dico):
    """
    Construit la carte des stations

    Args:
     

    Returns:
     

    >>> 
    
    """

    # the histogram of the data
    n, bins, patches = plt.hist(list(dico.values()),bins=30,edgecolor="k")

    # add a 'best fit' line
    
    

    plt.xlabel('Nombre de voyageurs')
    plt.ylabel('nombre de stations ayant x voyageurs')
    plt.title("Histogramme de l'utilisation des stations")
    plt.grid(True)

    plt.show()





def main():
    build_map()
    pass

if __name__ == '__main__':
    main()