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

    MY_MAP = Basemap(llcrnrlon=1.5, llcrnrlat=48.5, urcrnrlon=2.8, urcrnrlat=49.240305,
 rsphere=(6378137.00, 6356752.3142), resolution='l', projection='merc', epsg=4326)
    # MY_MAP = Basemap(llcrnrlon=-10, llcrnrlat=40, urcrnrlon=10, urcrnrlat=55,
    #                  rsphere=(6378137.00, 6356752.3142), resolution='l',
    #                  projection='merc', epsg=4326 )

    lon = []
    lat = []
    poids = []
    for station in dico:
        poids.append(station[0])
        lon.append(station[1][0])
        lat.append(station[1][1])
    MIN_POIDS = min(poids)
    X_COORD, Y_COORD = MY_MAP(lon, lat)
    CMAP = plt.cm.get_cmap('cool')
    SIZE = (np.array(poids)-MIN_POIDS+1)*20
    MY_MAP.arcgisimage(xpixels =1600 , verbose = False, service= 'ESRI_StreetMap_World_2D')
    heatmap, xedges, yedges = np.histogram2d(lon, lat, bins=200)
    SCA = MY_MAP.scatter(X_COORD, Y_COORD, s=10, marker='o', c=poids, cmap=CMAP)
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