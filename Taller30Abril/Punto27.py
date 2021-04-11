arrayNotas=[]
i=0
while(i<5):
    nota = float(input("Ingrese la nota: "))
    if 0.0<= nota <=5.0:
        arrayNotas.append(nota)
        i+=1
    else:
        print("Entrada no válida!")
        continue
notafinal = (arrayNotas[0]*0.15) + (arrayNotas[1]*0.20) + (arrayNotas[2]*0.15) + (arrayNotas[3] * 0.30) + (arrayNotas[4] * 0.20)
print("La nota final es:",notafinal)

if notafinal <= 2:
    print("Perdida sin recuperación")
elif 2<notafinal<3:
    print("Perdida con recuperación")
elif 3<=notafinal<4.5:
    print("Pasó")
else:
    print("Excelente estudiante")