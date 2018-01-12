# -*- coding: utf-8 -*-
"""
Created on Jan 02 17:15:42 2017

@author: Antoine Gélin
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.mlab as mlab
from matplotlib import cm as cmap
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

 #    MY_MAP = Basemap(lon_0=2.344589,lat_0=44.851824,width=99999,height=99999,
 # rsphere=(6378137.00, 6356752.3142), resolution='l', projection='merc',area_thresh = 0.1, epsg=27571)


    MY_MAP = Basemap(llcrnrlon=-0.5, llcrnrlat=48.5, urcrnrlon=0.5, urcrnrlat=49.240305,
 rsphere=(6378137.00, 6356752.3142), resolution='l', projection='merc',area_thresh = 0.1, epsg=27571)

 #    MY_MAP = Basemap(llcrnrlon=-2.5, llcrnrlat=45, urcrnrlon=2.5, urcrnrlat=50,
 # rsphere=(6378137.00, 6356752.3142), resolution='l', projection='merc',area_thresh = 0.1, epsg=27571)
    # les coordonnées sont centrées sur l'ile de France sur un e projection mercator. on peut faire varier la resolution de l'image générée

    # UTILISER DES SHAPEFILES OU PLUS SIMPLEMENT UTILISER UNE VUE EN LIGNE TYPE GMAPS OU OPENSTREETMAPS SERAIT PLUS PERTINENT
    # RESOLUTION TROP PETITE


    
    # MY_MAP.drawparallels()
    # MY_MAP.drawmeridians()
    lon = []
    lat = []
    poids = []
    for station in dico:
        poids.append(station[0])
        lon.append(station[1][1])
        lat.append(station[1][0])
    X_COORD, Y_COORD = MY_MAP(lon, lat)
    CMAP = plt.cm.get_cmap('Oranges')




    MY_MAP.drawrivers()
    MY_MAP.arcgisimage(xpixels =1600 , verbose = True, service= 'ESRI_StreetMap_World_2D')
    heatmap, xedges, yedges = np.histogram2d(lon, lat, bins=200)
    SCA = MY_MAP.scatter(X_COORD, Y_COORD, s=100, marker='o', c=poids, cmap=CMAP)
    plt.colorbar(SCA)
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