# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:07:21 2020

@author: HRV
"""


# library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Lectura de Datos
df = pd.ExcelFile('infocovid19.xlsx')
S0 = df.parse('evolución de casos')

#Plot con los datos originales
Y1 =    S0['Casos fallecidos']
Y2 =    S0['Casos recuperados']
X =     S0['Fecha']

Y = (Y1,Y2)
#Creacion del plot 1. 
fig1 , ax = plt.subplots(1,1,figsize=(14, 5))
# create your palette
pal = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]
plt.stackplot(X,Y, labels=['Casos Fallecidos','Casos recuperados'], colors=pal, alpha=0.4 )

#Nombre
plt.title('Evolución casos recuperados y fallecidos Covid-19 Guatemala')
ax.set(ylabel='Casos',xlabel='Fecha')
ax.legend(loc='upper left')

plt.show()
 
#Plot con porcentajes
YP1 = []
YP2 = []
XP = []
for i in range(len(Y1)):
    a = Y1[i]+Y2[i]
    if(a!= 0):
        YP1.append(Y1[i]/a)
        YP2.append(1-(Y1[i]/a))
        XP.append(i)
      
YP = (YP1,YP2)  
#Letalidad de casos cerrados
prom = max(Y1)/(max(Y1)+max(Y2))
labelProm = 'Promedio ('+str(round(prom,2))+')'

fig2 , ax = plt.subplots(1,1,figsize=(14, 5))
# create your palette
pal = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]
plt.stackplot(XP,YP, labels=['Casos Fallecidos','Casos recuperados'], colors=pal, alpha=0.4 )
plt.hlines(prom,min(XP),max(XP), colors='k', linestyles='dashdot', label=labelProm )
plt.legend(loc='upper left')

#Nombre
plt.title('Letalidad de casos cerrados Covid-19 Guatemala')
ax.set(ylabel='Porcentaje',xlabel='Días desde el caso 1')

plt.show()
 
      
      