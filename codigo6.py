#VAmos a estudiar matplotlib
import matplotlib.pyplot as plt
import numpy as np

#vamos a dibujar la sucesión de Fibonacci
#Lo primero será definir la función que calcula los números de Fibonacci
def fibonacci(n): #Función que devuelve el array con los n primeros números de Fibonacci
    f0, f1 = 1,1
    lista_fib = []
    lista_fib.append(f0)
    lista_fib.append(f1)
    if n <= 2: return(lista_fib)
    else:
        for i in range(2,n):
            fn = f0 + f1
            lista_fib.append(fn)
            f0 = f1
            f1 = fn
    return(lista_fib)

#LLamamos a la función
n = 10
fib = fibonacci(n)
print(fib)

#Ahora vamos a dibujar los valores de Fibonacci
#1. Creamos una figura
fig = plt.figure(figsize=(10,6)) #Tamaño de la figura en pulgadas
#2. Creamos un eje
fig_ax = fig.add_axes([0.1,0.1,0.8,0.8]) #Ejes que ocupan toda la figura
#3. Dibujamos en el eje
#Para dibujar hay que usar la sintaxis ax.plot(x,y). Donde x e y son listas.
x = np.arange(n) #Lista con los valores del eje x
y = fib          #Lista con los valores del eje y
fig_ax.plot(x,y, '-o', color = 'red', linewidth=2, markersize=8) #Dibujamos con línea roja y marcadores en los puntos

#Ahora vamos a dibujar sobre Fibonacci una función exponencial para comparar
y2 = []
for i in range(n):
    y2.append(2**i) #Función exponencial 2^n
fig_ax.plot(x,y2, '-o', color = 'blue', linewidth=2)

#Añadimos etiquetas y título
fig_ax.set_xlabel('n (posición en la sucesión)', fontsize=14)
fig_ax.set_ylabel('Valor', fontsize=14)
fig_ax.set_title('Sucesión de Fibonacci vs Función Exponencial', fontsize=16)
plt.show()
