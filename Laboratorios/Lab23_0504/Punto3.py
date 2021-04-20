nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1+nota2+nota3)/3
if promedio >= 7:
    print("Promocionado")
if 4<=promedio<7:
    print("Regular")
if promedio<4:
    print("Reprobado")