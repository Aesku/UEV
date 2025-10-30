#Aprender comandos de numpy
import numpy as np

#Numpy puede manipular listas, pero por decfecto trabaja con arrays
a = [1,2,3,4,5]
array_a = np.array(a)
x = np.array([[1,2.0],[0,0],(1+1j,3.)]) #
print(x)

#Crear arrays con numpy de x filas e y columnas
b = np.zeros((3,4)) #Array de ceros
print(b)

#Generar array con valores ordenados
array_2 = np.arange(100) #Array con valores del 0 al 99
print(array_2)

array_3 = np.arange(0,100,2)
print(array_3) #Array con valores pares del 0 al 98

#Función linspace
array_4 = np.linspace(0,10,5) #Array con 5 valores
print(array_4)

array_5 = np.linspace(0,10,5,endpoint=False) #Array con 5 valores sin incluir el 10
print(array_5)
