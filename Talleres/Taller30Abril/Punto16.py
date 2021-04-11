print("Solo se calcula en el cuadrante positivo del plano cartesiano, recuerde que x1 y y1 deben ser menores a x2 y y2, los puntos no deben estar ubicados en la misma recta y!")
x1 = float(input("Ingrese X1: "))
y1 = float(input("Ingrese Y1: "))
x2 = float(input("Ingrese X2: "))
y2 = float(input("Ingrese Y2: "))
d = ((x2-x1)**2+(y2-y1)**2)**0.5
print("La distancia entre los puntos es:",d)