contar = 0
grado = float(input("Ingrese la nota del estudiante: "))
while grado != -1:
    total = total + grado
    contar += 1
    grado = float(float("Ingrese la nota del estudiante: "))
else:
    promedio = total / contar
    print("Promedio de notas del grado escolar: ",promedio)