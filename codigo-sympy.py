#Ahora vamos a ver cómo utilizar sympy para hacer cálculos simbólicos
import sympy as sym

#Definimos una variable simbólica
x, y = sym.symbols('x y') #Ponemos entre espacios los nombres de las variables
#Definimos una expresión simbólica

expr = sym.sin(x)**2 + sym.cos(x)**2

#Sympy nos permite simplificar expresiones
simplified_expression = sym.simplify(expr)  #Esto debería devolver 1

print(simplified_expression)

#Sympy sirve para derivar e integrar funciones analíticamente
#Vamos a integrar la función exponencial
f = sym.exp(-x**2)
integral_f = sym.integrate(f, (x, -sym.oo, sym.oo))  #Integral de -infinito a infinito
derivative_f = sym.diff(f, x)  #Derivada de f respecto a x

print(f'La integral de exp(-x^2) desde -∞ hasta ∞ es: {integral_f}')
print(f'La derivada de exp(-x^2) respecto a x es: {derivative_f}')

#Sympy también puede resolver ecuaciones simbólicamente
eq = sym.Eq(x**2 + 1, 0) #x^2 + 1 = 0
solutions = sym.solve(eq, x)  #Resolvemos para x
print(f'Las soluciones de la ecuación x^2 + 1 = 0 son: {solutions}')

#Sympy puede trabajar con matrices simbólicas
A = sym.Matrix([[0, 1], [0, 2]])
det_A = A.det()  #Determinante de la matriz A
print(f'El determinante de la matriz A es: {det_A}')
eigenvals_A = A.eigenvals()  #Valores propios de la matriz A
print(f'Los valores propios de la matriz A son: {eigenvals_A}')
eigenvects_A = A.eigenvects()  #Vectores propios de la matriz A
print(f'Los vectores propios de la matriz A son: {eigenvects_A}')

#sympy ya resuelve ecuaciones diferenciales

t = sym.symbols('t')
f = sym.Function('f')(t)
ode = sym.Eq(f.diff(t), -2*f)  #df/dt =
solution = sym.dsolve(ode, f)
print(f'La solución de la ecuación diferencial df/dt = -2f es: {solution}')