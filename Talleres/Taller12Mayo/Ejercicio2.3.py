import pandas as pd
def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>=3].sort_values(ascending=False)

notas = {'Juan':5, 'Maria':4.5, 'Pedro':2, 'Carmen': 4.5, 'Luis':5}
print(aprobados(notas))