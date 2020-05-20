# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:08:03 2020

@author: Steven Rubio
"""


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#   Datos descargados de:
#   https://www.mspas.gob.gt/index.php/noticias/covid-19/casos
df = pd.ExcelFile('infocovid19.xlsx')

S1 = df.parse('evolución de casos')

x = S1['Fecha']
y = S1['Casos activos']
z = S1['Casos fallecidos']


#   Funcion para generar el tiempo que a pasado para duplicar los casos
def DuplicaC(List, Vo):
    casos = [(Vo)]
    tiempo = [0]
    contador = 0
    longl = len(List)
    
    for i in range(longl):
        ultimo =  2*casos[-1]
        if(List[i]>=ultimo):
            tiempo.append((contador))
            casos.append(ultimo)
            contador = 0
        else:
            if(List[i]!=0):    contador=contador+1
            
    print('Actual: ')
    print(ultimo,contador)
    return casos,tiempo,ultimo,contador
    


val,tmp,ult,cnt         = DuplicaC(y,1)
val2,tmp2,ult2,cnt2     = DuplicaC(z,2)

fig1 , ax = plt.subplots(1,2)

#Plot the data
ax[0].semilogx(val, tmp, label='Casos Activos')
ax[0].semilogx(val2, tmp2, label='Casos Fallecidos',color='r')

ax[0].semilogx((val[-1],ult),(tmp[-1],cnt),'bo--')
ax[0].annotate('Valor actual', xy=((ult, cnt)), xytext=((ult-1800, cnt-3)),
              arrowprops=dict(facecolor='black', shrink=0.05))

ax[0].semilogx((val2[-1],ult2),(tmp2[-1],cnt2),'ro--')

ax[1].semilogx(x, y)
# Add a legend
ax[0].legend()

#Nombre
ax[1].set_title('Casos Activos Covid-19 Guatemala')
ax[0].set_title('Duplicación de Casos Covid-19 Guatemala')

#Show the plot
plt.show()

