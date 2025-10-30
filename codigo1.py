import numpy

#Código para calcular la media de una lista de números

lista_numeros = [10, 20, 30, 40, 50]

#Media a mano
#Media = suma de los números / cantidad de números
#método 1: usando un bucle

suma = 0
for numero in lista_numeros:
    suma = suma + numero
cantidad = len(lista_numeros)
media_a_mano = suma / cantidad
print(media_a_mano)

#método 2: usando la función sum()
suma = sum(lista_numeros)
cantidad = len(lista_numeros)
media_a_mano = suma / cantidad
print(media_a_mano)

#Media usando numpy
media_numpy = numpy.mean(lista_numeros)
print(media_numpy)