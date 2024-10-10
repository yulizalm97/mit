#vamos a crear un arreglo

import numpy as np #np de numpy

arreglo=np.array([1,2,3,4,5,])

#print(arreglo)

#arreglos de ceros de 3 elementos

ceros=np.zeros(3)
#print(ceros)

#arreglo de 4x4

unos=np.ones((4,4))
#print(unos)

#arreglos con valores de 0 al 9

rango=np.arange(10)
#print(rango)

#arreglos con 5 valores en un rango de 0 a 1
valores=np.linspace(0,1,5)
#print(valores)

valoresx=np.round(valores).astype(int)
print(valoresx)