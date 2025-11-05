#Vamos a resolver una EDO con el método de Euler
#El primer paso será definir la función que está en la EDO

#Si la EDO es dy/dx = f(t,y), definimos f(t,y)

def f(t,y):
    return -2*t*y

#Definimos la función de Euler
def Euler(f, t0, y0, h, n_steps):
    #Inicializamos las listas
    t_list, y_list = [t0], [y0]

    #Implementamos el método de Euler
    #lista_i = [0,1,2,3,4,5,6,7,8,9,...,Nsteps]
    lista_i = list(range(n_steps))
    for i in lista_i:
        t_old = t_list[-1]
        y_old = y_list[-1]
        #Aplicamos la fórmula de Euler
        t_new = t_old + h #Incrementamos el mallado en t
        y_new = y_old + h * f(t_old, y_old) #Calculamos
 
        #Añadimos los nuevos valores a las listas
        t_list.append(t_new)
        y_list.append(y_new)
    return t_list, y_list

#La solución serán dos listas
#Una lista contendrá los valores de t
#Otra lista contendrá los valores de y, correspondientes
#a cada valor de t. 
#y_list[i] corresponderá a t_list[i]

#Solución 1.
#Definimos las condiciones iniciales
t0 = 0.0  #Valor inicial de t
y0 = 1.0  #Valor inicial de y
h = 0.1   #Paso de integración. Luego probaremos con otros valores
n_steps = 50  #Número de pasos de integración.

t_list, y_list = Euler(f, t0, y0, h, n_steps)

#Mostramos los resultados
#Conviene hacer un dibujo
#Llamaremos a pyplot
from matplotlib import pyplot as plt
#import matplotib.pyplot as plt

plt.plot(t_list, y_list, label = 'Caso 1')

#Solución 2.
#Definimos las condiciones iniciales
t0 = 0.0  #Valor inicial de t
y0 = 2.0  #Valor inicial de y
h = 0.1   #Paso de integración. Luego probaremos con otros valores
n_steps = 50  #Número de pasos de integración.

t_list, y_list = Euler(f, t0, y0, h, n_steps)
plt.plot(t_list, y_list, label = 'Caso 2')

#Solución 3.
#Definimos las condiciones iniciales
t0 = 0.0  #Valor inicial de t
y0 = 2.0  #Valor inicial de y
h = 0.0001   #Paso de integración. Luego probaremos con otros valores
n_steps = 10000  #Número de pasos de integración.

t_list, y_list = Euler(f, t0, y0, h, n_steps)
plt.plot(t_list, y_list, label = 'Caso 3')

plt.legend()
plt.show()