nombresLista = ["Cero","Uno","Dos","Tres","Cuatro","Cinco","Seis","Siete","Ocho","Nueve","Diez"]
i = int(input("Ingrese el número, debe ser mayor o igual a 0 y menor o igual a 10: "))

if i>=0 or i<=10:
    print(nombresLista[i])
else:
    print("Error,número no válido.")