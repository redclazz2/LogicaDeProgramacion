import pandas as pd
datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
datos = pd.DataFrame(datos)
print(datos)

def balance(dataframe,meses):
    dataframe['Balance'] = dataframe.Ventas - dataframe.Gastos
    return dataframe[dataframe.Mes.isin(meses)].Balance.sum()

print(balance(datos,["Enero","Abril"]))

#This code sends to the function the dataframe with the months to check, it's important to notice how they need to be passed as a []
#Inside the function a new section 'balance' is created in which we get a result from subtracting the outcome from the income
#Lastly, it returns the sum of the balance found in the months specified when the func was called.