#Definición de Listas
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
scores = []
#Explicación de la función del programa
print("Este programa permite ingresar las notas totales de cada curso para despues mostrarlas por pantalla:")
#Por cada elemento en la lista, se va a pedir el input de la nota.
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "? : ")  #Input
    scores.append(score)       #Añadiendo el valor a la lista de puntuaciones
for i in range(5):      #Por cada i en rango 0 a 5:
    if float(scores[i]) >= 3.0:         #Si la nota es >= 3 se añade un mensaje de que pasó, de otra manera se muestra que no.
        cadenaExtra = "has aprobado!"
    else:
        cadenaExtra = "No has aprobado..."
    print("En " + subjects[i] + " has sacado " + str(scores[i]), cadenaExtra)
