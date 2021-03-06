# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:13:11 2020

@author: Steven Rubio

Mapa de regiones COVID-19
"""

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
#from matplotlib.patches import PathPatch
import numpy as np

fig, ax = plt.subplots(figsize=(8,8))
#Nacional
m = Basemap(resolution='i', # c, l, i, h, f or None
    lat_0=14.6569, lon_0=-90.51,
    llcrnrlon=-92.93, llcrnrlat=13.15,urcrnrlon=-87.58, urcrnrlat=18.42,
    projection='tmerc')
    
m.drawmapboundary(fill_color='#EBEFEF')                  
#m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
#Leemos nuestra shapefile, no los activamos todos
m.readshapefile('Data/gtm/gtm_admbnda_adm0_ocha_conred_20190207', 'ej0',linewidth=1.5)
m.readshapefile('Data/gtm/gtm_admbnda_adm1_ocha_conred_20190207', 'ej1',drawbounds=True)

Region1 = ['Chimaltenango', 'Guatemala','Sacatepequez']
Region2 = ['Quetzaltenango', 'Totonicapan','Huehuetenango','San Marcos']
Region3 = ['Izabal','Zacapa','Chiquimula','Jalapa','El Progreso']
Region4 = ['Jutiapa','Santa Rosa','Escuintla','Suchitepequez','Retalhuleu']
Region5 = ['Alta Verapaz', 'Baja Verapaz', 'Peten','Quiche','Solola']
patches   = []

#Pintamos la region 1
for info, shape in zip(m.ej1_info, m.ej1):
    if info['ADM1_REF'] in Region1:
        patches.append( Polygon(np.array(shape), True) )
ax.add_collection(PatchCollection(patches, facecolor= '#FB1D07', edgecolor='k', linewidths=1., zorder=2,alpha=0.3))
ax.plot(440000, 440000,'*',color = '#FB1D07',alpha=0.3)
plt.text(445000, 436000,'Región 1',size=6)

patches   = []
#Pintamos la region 2
for info, shape in zip(m.ej1_info, m.ej1):
    if info['ADM1_REF'] in Region2:
        patches.append( Polygon(np.array(shape), True) )
ax.add_collection(PatchCollection(patches, facecolor= '#0A9B11', edgecolor='k', linewidths=1., zorder=2,alpha=0.3))
ax.plot(440000, 420000,'*',color = '#0A9B11',alpha=0.3)
plt.text(445000, 416000,'Región 2',size=6)

patches   = []
#Pintamos la region 3
for info, shape in zip(m.ej1_info, m.ej1):
    if info['ADM1_REF'] in Region3:
        patches.append( Polygon(np.array(shape), True) )
ax.add_collection(PatchCollection(patches, facecolor= '#15378F', edgecolor='k', linewidths=1., zorder=2,alpha=0.3))
ax.plot(440000, 400000,'*',color = '#15378F',alpha=0.3)
plt.text(445000, 396000,'Región 3',size=6)

patches   = []
#Pintamos la region 4
for info, shape in zip(m.ej1_info, m.ej1):
    if info['ADM1_REF'] in Region4:
        patches.append( Polygon(np.array(shape), True) )
ax.add_collection(PatchCollection(patches, facecolor= '#8D2294', edgecolor='k', linewidths=1., zorder=2,alpha=0.3))
ax.plot(440000, 380000,'*',color = '#8D2294',alpha=0.3)
plt.text(445000, 376000,'Región 4',size=6)

patches   = []
#Pintamos la region 5
for info, shape in zip(m.ej1_info, m.ej1):
    if info['ADM1_REF'] in Region5:
        patches.append( Polygon(np.array(shape), True) )
ax.add_collection(PatchCollection(patches, facecolor= 'yellow', edgecolor='k', linewidths=1., zorder=2,alpha=0.5))
ax.plot(440000, 360000,'*',color = 'yellow',alpha=0.5)
plt.text(445000, 356000,'Región 5',size=6)

ax.set_title('Regiones de Análisis')
plt.show()
