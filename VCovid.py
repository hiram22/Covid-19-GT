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


#   Funcion para generar el tiempo que a pasado para duplicar los casos
def DuplicaC(List, Vo):
    # ----------
    # Entradas:
    # List      = Lista con la cantidad de casos
    # Vo        = Valor inicial
    # ----------
    # Salidas:
    # casos     = Lista con el número de casos
    # tiempo    = Lista con el tiempo para cada número de casos
    # ultimo    = Siguiente número de casos a alcanzar
    # contador  = Tiempo actual en el número de casos
    # ----------
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
    
#Obtenemos última fecha registrada
S2 = df.parse('Casos por día')
f = S2['Fecha']
fecha = str(f[len(f)-1])
fecha = fecha[:10]
fecha = fecha[8:10]+fecha[4:8]+fecha[:4]
#Creacion del plot
fig1 , ax = plt.subplots(1,2,figsize=(14, 5))

#Modifico los fonts
#Opciones con: print(plt.style.available)
plt.style.use('bmh')

#Plot the data
#Primer plot
S1 = df.parse('evolución de casos')

x = S1['Casos recuperados']
y = S1['Casos activos']
z = S1['Casos fallecidos']

val , tmp,  ult,  cnt   = DuplicaC(y,1)
val2, tmp2, ult2, cnt2  = DuplicaC(z,2)
val3, tmp3, ult3, cnt3  = DuplicaC(x,4)

#ax[0].set_ylim([0, 20])
ax[1].semilogx(val, tmp, label='Casos Activos',color='#C725E1')
ax[1].semilogx(val2, tmp2, label='Casos Fallecidos',color='#25D8E1')
ax[1].semilogx(val3, tmp3, label='Casos Recuperados',color='g')

ax[1].semilogx((val[-1],ult),(tmp[-1],cnt),'o--',color='#C725E1')
ax[1].annotate('Valor actual', xy=((ult, cnt)), xytext=((ult-2000, cnt-2)),
              arrowprops=dict(facecolor='black', shrink=0.05))
ax[1].semilogx((val2[-1],ult2),(tmp2[-1],cnt2),'o--',color='#25D8E1')
ax[1].semilogx((val3[-1],ult3),(tmp3[-1],cnt3),'go--')

#Nombre
ax[1].set_title('Duplicación de Casos Covid-19 Guatemala ('+fecha+')')
ax[1].set(xlabel='Total de Casos',ylabel='Días')

# Add a legend
ax[1].legend()

#Segundo plot
x = S2['Casos por día']
z = S2['Casos recuperados']
y = S2['Casos fallecidos']


ax[0].plot(range(len(x)), x,label='Casos Nuevos')
ax[0].plot(range(len(y)), y,label='Casos Fallecidos',color='#25D8E1')
ax[0].plot(range(len(z)), z,label='Casos Recuperados',color='g')

#Nombre
ax[0].set_title('Casos por día Covid-19 Guatemala ('+fecha+')')
ax[0].set(xlabel='Días desde el caso 1 (13-03-2020)',ylabel='Casos')

# Add a legend
ax[0].legend(loc='upper left')

#Guardando el plot
#plt.savefig('C:/Users/HRV/Desktop/Post-U/Scripts/Covid-19-GT/boom.png')

fig2 , ax2 = plt.subplots(1,1,figsize=(8, 8))

#Tercer plot
df2 = pd.ExcelFile('Myinfocovid19.xlsx')
S2 = df2.parse('Casos por región')

r1 = S2['Region 1']
r2 = S2['Region 2']
r3 = S2['Region 3']
r4 = S2['Region 4']
r5 = S2['Region 5']
f2 = S2['Fecha']
f = range(len(f2))


ax2.semilogy(f, r1,label='Región 1',color = '#FB1D07')
ax2.semilogy(f, r2,label='Región 2',color = '#0A9B11')
ax2.semilogy(f, r3,label='Región 3',color = '#15378F')
ax2.semilogy(f, r4,label='Región 4',color = '#8D2294')
ax2.semilogy(f, r5,label='Región 5',color = '#07E0D6')

#Nombre
ax2.set_title('Total de casos por región')
ax2.set(ylabel='Cantidad de Casos',xlabel='Días a partir del 13-04-2020 ')        
plt.locator_params(axis='y', numticks=4)

# Add a legend
ax2.legend()

#Show the plot
plt.show()

#Guardando el plot
#plt.savefig('C:/Users/HRV/Desktop/Post-U/Scripts/Covid-19-GT/boom2.png')

