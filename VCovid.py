# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:08:03 2020

@author: Steven Rubio
"""


import pandas as pd
from pandas import ExcelFile
import matplotlib.pyplot as plt

#   Datos descargados de:
#   https://www.mspas.gob.gt/index.php/noticias/covid-19/casos
df = pd.ExcelFile('infocovid19.xlsx')

S1 = df.parse('evolución de casos')

x = S1['Casos recuperados']
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
            
    print('Siguiente valor: '+str(ultimo)+'. Días hasta el momento: '+str(contador))
    return casos,tiempo,ultimo,contador
    


val , tmp,  ult,  cnt   = DuplicaC(y,1)
val2, tmp2, ult2, cnt2  = DuplicaC(z,2)
val3, tmp3, ult3, cnt3  = DuplicaC(x,4)

fig1 , ax = plt.subplots(1,2,figsize=(18, 10))

#Modifico los fonts

#Opciones con: print(plt.style.available)
plt.style.use('tableau-colorblind10')

#Plot the data
#Primer plot
ax[0].set_ylim([0, 20])
ax[0].semilogx(val, tmp, label='Casos Activos',color='b')
ax[0].semilogx(val2, tmp2, label='Casos Fallecidos',color='r')
ax[0].semilogx(val3, tmp3, label='Casos Recuperados',color='g')

ax[0].semilogx((val[-1],ult),(tmp[-1],cnt),'bo--')
ax[0].annotate('Valor actual', xy=((ult, cnt)), xytext=((ult-1800, cnt-3)),
              arrowprops=dict(facecolor='black', shrink=0.05))
ax[0].semilogx((val2[-1],ult2),(tmp2[-1],cnt2),'ro--')
ax[0].semilogx((val3[-1],ult3),(tmp3[-1],cnt3),'go--')

#Nombre
ax[0].set_title('Duplicación de Casos Covid-19 Guatemala 2020-05-19')
ax[0].set(xlabel='Total de Casos',ylabel='Días')

# Add a legend
ax[0].legend()

#Segundo plot
S2 = df.parse('Casos por día')
x = S2['Casos por día']
z = S2['Casos recuperados']
y = S2['Casos fallecidos']

ax[1].plot(range(len(x)), x,label='Casos Nuevos')
ax[1].plot(range(len(y)), y,label='Casos Fallecidos')
ax[1].plot(range(len(z)), z,label='Casos Recuperados')

#Nombre
ax[1].set_title('Casos por día Covid-19 Guatemala 2020-05-19')
ax[1].set(xlabel='Días desde el caso 1',ylabel='Casos por día')

# Add a legend
ax[1].legend()

#Show the plot
plt.show()

#Guardando el plot
plt.savefig('C:/Users/HRV/Desktop/Post-U/Scripts/Covid-19-GT/boom.png')

