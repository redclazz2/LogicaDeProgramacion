contar = 0
grado =  float(input("Introduzca la nota de un estudiante (-1 Para salir)"))
while grado != -1:
    total = total + grado
    contar += 1
    print("Introduzca la nota de un estudiante (-1 Para salir):")
    grado = float(input())
promedio = total / contar
print("Promedio de ntoas del grado escolar es:",promedio)