#Manipulación de arrays con numpy
import numpy as np
a1 = np.arange(15)
##print(a1)

#Cambiar la forma del array
a2 = a1.reshape(3,5)
##print(a2)

#Dimensiones del array
##print(a2.ndim)
#Forma del array
##print(a2.shape)
#Tamaño del array
##print(a2.size)

#Un error seria array = np.array(1,2,3,4,5)
#Lo correcto sería
array = np.array([1,2,3,4,5])

#Utizilar numpy permite usar arrays como si fueran VECTORES o MATRICES
#Ejemplo de vectores en 2 dimensiones

v1 = np.array([1,2,0])
v2 = np.array([3,4,0])
sum_v1v2 = v1 + v2 #Suma de vectores
prod_v1v2 = v1 * v2 #Producto elemento a elemento
dot_v1v2 = np.dot(v1,v2) #Producto escalar
cross_v1v2 = np.cross(v1,v2) #Producto vectorial

'''
print('FROM HERE')
print(sum_v1v2)
print(prod_v1v2)
print(dot_v1v2)
print(cross_v1v2)
'''

#Producto matricial
m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
prod_m1m2 = np.dot(m1,m2)
#print(prod_m1m2)
#print(m1 @ m2) #Otra forma de hacer el producto matricial

#Inversa de una matriz
m3 = np.array([[1,2],[3,4]])
inv_m3 = np.linalg.inv(m3)
#otra forma de hacerlo
inv_m3_alt = np.inv(m3)
print(inv_m3)
print(inv_m3_alt)