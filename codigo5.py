#Vamos a aprender operadores lógicos en Python
#Operadores lógicos: and, or, not

#Condicionales: if, elif, else

edades = [15, 22, 18, 30, 25, 12, 17]
nombres = ['Ana', 'Luis', 'Carlos', 'Marta', 'Sofía', 'Jorge', 'Lucía']
#Nos preguntamos si hay alguien con la mayoría de edad
mayoria_edad = 18

#Podemos enumerar los elementos de una lista
for i,edad in enumerate(edades):
 if edad >= mayoria_edad:
        print(f'La persona {nombres[i]} es mayor de edad con {edad} años.')
 else:
        print(f'La persona {i+1} es menor de edad con {edad} años.')
 print('hello world')

#Los bucles tienen if, else, y elif. Vamos a hacer un ejemplo que combine las tres
#Buscamos una persona con una edad entre 10 y 20 años
for i,edad in enumerate(edades):
    if edad < 10:
        print(f'La persona {nombres[i]} es un niño con {edad} años.')
    elif edad >= 10 and edad < 20:
        print(f'La persona {nombres[i]} es un adolescente con {edad} años.')
    else:
        print(f'La persona {nombres[i]} es un adulto con {edad} años.')

#Podemos romper los bucles con break
for i,edad in enumerate(edades):
    if edad >= 18:
        print(f'La primera persona mayor de edad es {nombres[i]} con {edad} años.')
        break
#Podemos saltar a la siguiente iteración con continue
for i,edad in enumerate(edades):
    if edad < 18:
        continue
    print(f'La persona {nombres[i]} es mayor de edad con {edad} años.')
#Podemos usar else al final de un bucle for
for i,edad in enumerate(edades):
    if edad < 18:
        print(f'La persona {nombres[i]} es menor de edad con {edad} años.')
else:
    print('Hemos terminado de revisar todas las edades.')

#Podemos revisar datos con los operadores lógicos
#Buscamos personas con edades entre 15 y 25 años
for i,edad in enumerate(edades):
    if edad >= 15 and edad <= 25:
        print(f'La persona {nombres[i]} tiene una edad entre 15 y 25 años: {edad} años.')

