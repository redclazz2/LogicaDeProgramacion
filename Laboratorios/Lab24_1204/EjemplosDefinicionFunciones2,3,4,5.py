#2
def suma(a,b):
    print(a+b)

suma(1,2)

#3
def suma(a,b=3):
    print(a+b)

suma(1)

#4
suma(b=2,a=2)

#5
result = suma(3,b=2)
#Devuelve 5

#result2 = suma(b=2,3)
#Marca error

#6
s = suma
result = s(1,2)
