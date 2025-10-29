import scipy as sp
from scipy import integrate, optimize, linalg, interpolate
import numpy as np

#Ejemplo 1: Integración numérica usando scipy.integrate
# Definimos una función

#Mi función se llamará f(x) = sin(x)
f = lambda x: np.sin(x)

#1.1. Integramos f(x) desde 0 hasta pi
result, error = integrate.quad(f, 0, 2*np.pi)

#1.2. Imprimimos el resultado
print(f'La integral de sin(x) desde 0 hasta pi es aproximadamente {result}')

#Ejemplo 2. Encontrar raíces de una función
#Las raíces se obtienen con scipy.optimize
#2.1. Definimos la función

g = lambda x: x**3 - 2*x - 5
#2.2. Encontramos una raíz cerca de x=2
#método 1
root1 = optimize.root_scalar(g, bracket=[-10,10])
print(f'Una raíz de la función g(x) = x^3 - 2x - 5 es aproximadamente {root1.root}')

#2.3. Comprobamos visualmente la raíz
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)

#Evaluamos la función g en los puntos x
y = g(x)
plt.plot(x, y, label='g(x) = x^3 - 2x - 5')

#Puedo meter una línea horizontal en y=0
plt.axhline(0)
plt.show()

#Scipy se puede usar para diagonalizar matrices
#Ejemplo 3: Diagonalización de matrices
#3.1. Definimos una matriz
A = np.array([[4, -2],
              [1,  1]])

vals, vecs = linalg.eig(A)
print('Los valores propios de la matriz A son:', vals)
print('Los vectores propios de la matriz A son:\n', vecs)

#linalg también sirve para productores escalares, sistemas de ecuaciones, etc.

#example 4. Interpolación de datos
#Definimos algunos datos
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

#4.1. Creamos una función de interpolación
interp_func = interpolate.interp1d(x_data, y_data, kind='cubic')

#Dibujamos los datos originales y la interpolación
x_new = np.linspace(0, 5, 100)
y_new = interp_func(x_new)
plt.plot(x_data, y_data, 'o', label='Datos originales')
plt.plot(x_new, y_new, '-', label='Interpolación cúbica')
plt.legend()
plt.show()
