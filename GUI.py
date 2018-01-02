# -*- coding: utf-8 -*-
"""
Created on Jan 02 17:15:42 2017

@author: Antoine Gélin
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


def build_map():
    """
    Construit la carte des stations

    Args:
     

    Returns:
     

    >>> 
    
    """
    MY_MAP = Basemap(llcrnrlon=1.450561, llcrnrlat=48.136375, urcrnrlon=3.550762, urcrnrlat=49.240305,
    rsphere=(6378137.00, 6356752.3142), resolution='i', projection='merc')
    # les coordonnées sont centrées sur l'ile de France sur un e projection mercator. on peut faire varier la resolution de l'image générée
    MY_MAP.bluemarble()
    # blue marble est l'image satelite de la NASA
    MY_MAP.drawcoastlines()
    MY_MAP.drawmapboundary(fill_color='aqua')
    MY_MAP.drawrivers()
    plt.show()









def main():
    build_map()
    pass

if __name__ == '__main__':
    main()