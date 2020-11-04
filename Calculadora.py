from math import sin, cos, tan, exp, log

def apply_function(f, n):
    '''
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    '''
    functions = {'sen':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():
    '''
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. 
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sen, cos, tan, exp o log).
        n: Es un entero positivo.
    '''
    f = input('Introduce la función a aplicar (sen, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()