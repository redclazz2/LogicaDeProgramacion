#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ejercicio 1
import numpy as np
print(np.__version__)


# In[2]:


#Ejercicio 2
import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)


# In[8]:


#Ejercicio 3 
import numpy as np
a = np.arange(2,11).reshape(3,3)
print(a)


# In[14]:


#Ejercicio 4
import numpy as np
a = np.zeros(10)
print('Original Array:\n',a)
a[6] = 11
print(a)


# In[17]:


#Ejercicio 5
import numpy as np
a = np.arange(12,38)
print(a)


# In[18]:


#Ejercicio 6
import numpy as np
a = np.arange(12,38)
print(a)
print(a[::-1])


# In[20]:


#Ejercicio 7
import numpy as np
a = [1,2,3,4]
print(a)
print(np.asfarray(a))


# In[23]:


#Ejercicio 8
import numpy as np
a = np.ones((5,5))
print(a)
a[1:-1,1:-1]=0
print(a)


# In[24]:


#Ejercicio 9
import numpy as np
a = np.ones((5,5))
print(a)
a = np.pad(a,pad_width=1,mode='constant',constant_values=0)
print(a)


# In[5]:


#Ejercicio 10
import numpy as np
x = np.zeros((8,8))
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# In[3]:


#Ejercicio 11
import numpy as np
my_list = [1,2,3,4,5,6,7,8]
print(np.asarray(my_list))
my_tuple = ([8,4,6],[1,2,3])
print(np.asarray(my_tuple))


# In[1]:


#Ejercicio 12
import numpy as np
a = np.array([1,2,3,4])
np.append(a,[[40,50,60],[70,80,90,10]])
print(a)


# In[2]:


#Ejercicio 13
a = np.empty((3,3))
print(a)
b = np.full((5,5),7)
print(b)


# In[4]:


#Ejercicio 14
a = np.array([34,23,12,54])
print(a)
print(5*a/6-5*32/9)


# In[6]:


#Ejercicio 15
import numpy as np
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)


# In[15]:


#Ejercicio 16
a = np.array([1,2,3,4,5,6])
print(np.size(a))
print(a.itemsize)
print(a.nbytes)


# In[17]:


#Ejercicio 17
array1 = [1,2,3,4]
array2 = [2,6,7,8]
print(np.in1d(array1,array2))


# In[18]:


#Ejercicio 18
array1 = [1,2,3,4]
array2 = [2,6,7,8]
print(np.intersect1d(array1,array2))


# In[22]:


#Ejercicio 19
a = np.array([10,10,20,20,30,30])
print(a)
print(np.unique(a))
b = np.array([[10,20,20,10],[30,30,40,40]])
print(b)
print(np.unique(b))


# In[32]:


#Ejercicio 20
a = np.array([10,20,30])
b = [0,1,2,3,4,5]
print(np.setdiff1d(a,b))


# In[34]:


#Ejercicio 21
a = [1,2,3,4,5]
b = [2,3,4,5,6]
print(np.setxor1d(a,b))


# In[35]:


#Ejercicio 22
print(np.union1d(a,b))


# In[36]:


#Ejercicio 23
import numpy as np
print(np.all([[True,False],[True,True]]))
print(np.all([[True,True],[True,True]]))
print(np.all([10, 20, 0, -50]))
print(np.all([10, 20, -50]))


# In[37]:


#Ejercicio 24
import numpy as np
print(np.any([[False,False],[False,False]]))
print(np.any([[True,True],[True,True]]))
print(np.any([10, 20, 0, -50]))
print(np.any([10, 20, -50]))


# In[38]:


#Ejercicio 25
import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)
print("Repeating 2 times")
x = np.tile(a, 2)
print(x)
print("Repeating 3 times")
x = np.tile(a, 3)
print(x)


# In[ ]:




