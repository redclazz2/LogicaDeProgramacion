print("Ejercicio 10")

a,b,f = 0, 1, 0

for i in range(1,7):
    if f == 0:
        print(a)
        f +=1
    elif f == 1:
        print(b)
        f += 1
    else:
        a = a + b
        b = a + b
        print(a)
        print(b)