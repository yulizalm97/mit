import numpy as np

#la media es el promedio de un conjunto de datos. se calcula sumando todos los  y dividiendola entre el numero total de los mismos.
#se calcula utilizando la función np.mean()
datos= np.array([1,3,6,9,15])
media=np.mean(datos)
print(media)

#la desviación estándar es una medida de dispersión que indica qué tan dispersos están los datos con respecto a la media. un valor alto indica mayor disperción mientras que un valor bajo indica mayor agrupación alrededor de la media
#se calcula utilizando la función np.std()

desviacion_estandar=np.std(datos)
print(desviacion_estandar)

#El valor máximo es el número más grande en el conjunto de datos y el valor mínimo es el número más pequeño.
#se calculan utilizando las funciones np.max() y np.min(), respectivamente. 

valor_maximo=np.max(datos)
valor_minimo=np.min(datos)
print(valor_maximo,valor_minimo)

#La mediana es el valor central de un conjunto de datos cuando los datos están ordenados. Si hay un numero par de valoresla mediana es el promedio de los dos valores centrales
#se calcula utilizando la función np.median()

mediana=np.median(datos)
print(mediana)