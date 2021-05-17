#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
plt.plot([0,10], [0,10], color='blue', linewidth=3, label='línea')
plt.legend()
plt.show()


# In[4]:


import matplotlib.pyplot as plt
 
import numpy as np # Importamos numpy como el alias np
 
a = np.linspace(0,20,50)
 
b= np.sin(a)
 
c=plt.plot(a, b, 'c-3', linewidth = 2)
 
c=plt.plot(a+0.2, b-1, 'r-o', linewidth = 2)
 
plt.xlabel("Tiempo (s)", fontsize = 20)
 
plt.ylabel(r"$y (\mu m)$", fontsize = 24, color = 'blue')
 
plt.text(5, 7, "Más texto", fontsize = 12)
 
plt.title("velocidad (m/s)", fontsize = 20)
 
plt.legend( ('Etiqueta1', 'Etiqueta2', 'Etiqueta3'), loc = 'upper left')
 
plt.grid(True)
 
plt.savefig('figura3.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
 
plt.show()


# In[5]:


import matplotlib.pyplot as plt
 
import numpy as np # Importamos numpy como el alias np
 
a = np.linspace(0,20,50)
 
b= np.sin(a)
 
plt.figure()
 
# plot 1
 
plt.subplot(2,2,1)
 
plt.plot(a, b,'r')
 
# Segunda grafica
 
plt.subplot(2,2,2)
 
plt.plot(a+2, b*25,'g')
 
# Tercera grafica
 
plt.subplot(2,2,3)
 
plt.plot(b, a,'b')
 
# Cuarta grafica
 
plt.subplot(2,2,4)
 
plt.plot(a, b,'k')
 
# Mostramos en pantalla
 
plt.show()


# In[6]:


import numpy as np
 
import matplotlib.pyplot as plt
 
plt.figure()
 
x = np.arange(-5, 5, 0.01)
 
y = np.arange(-5, 5, 0.01)
 
X, Y = np.meshgrid(x, y)
 
# Definimos cos (x^3 + y^2)
 
fxy = np.cos(X**3+Y**2)
 
plt.imshow(fxy);
 
plt.colorbar();
 
plt.show()


# In[7]:


a = [3, 4, 5, 6]
b = [5, 6, 3, 4]
plt.plot(a, b)
plt.show()


# In[8]:


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
# Tipo de figura
ax = fig.gca(projection='3d')

# Datos
X = np.arange(-4, 4, 0.3)
Y = np.arange(-4, 4, 0.3)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Graficamos o trazamos la superficie
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')

# Personalizamos el ejex z
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Agregamos una barra de colores para que asigne valores a los colores.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


# In[9]:


5.3 
#Definir los datos
a = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]

#Configurar las características del gráfico
plt.hist(a, bins, histtype = 'bar', rwidth = 0.8, color = 'lightgreen')

#Definir título y nombres de ejes
plt.title('Histograma')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar figura
plt.show()


# In[10]:


#Definir los datos
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]

#Configurar las características del gráfico
plt.scatter(x1, y1, label = 'Datos 1',color = 'red')
plt.scatter(x2, y2,label = 'Datos 2', color = 'purple')

#Definir título y nombres de ejes
plt.title('Gráfico de dispersión')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda y figura
plt.legend()
plt.show()


# In[11]:


#Definir los datos
dormir =[7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar =[7,8,7,2,2]
recreación = [8,5,7,8,13]
divisiones = [7,2,2,13]
actividades = ['Dormir','Comer','Trabajar','Recreación']
colores = ['red','purple','blue','orange']

#Configurar las características del gráfico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90, shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')

#Definir título
plt.title('Gráfico circular')

#Mostrar figura
plt.show()


# In[12]:


plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45],'g--d')


# In[13]:


import matplotlib.pyplot as plt
plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
plt.show()


# In[ ]:




