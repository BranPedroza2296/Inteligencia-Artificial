import time #Nos permite medir el tiempo
import sys
sys.setrecursionlimit(30000) 

def factorial(n): #La funcion nos permite que entre un numero n
    respuesta = 1 #Asignamos el valor de la variable en 1

    while n > 1: #Mientras n sea mayor a uno, se repite el siclo while
        respuesta *= n #Multiplicamos n por si misma y lo almacenamos en la variable respuesta
        n -= 1 #luego le restamos 1 a la variable n
        
    return respuesta #Se retorna la respuesta del factorial que paso por la funcion 


def factorial_recursivo(n): #Definimos la funcion que recibe un numero n
    if n ==1:
        return 1 #Le asignamos la condicion que si n es 1, regrese el valor mismo de 1

    return n * factorial_recursivo(n - 1) #En caso de que el valor no sea 1, multiplicamos el valor de n por el valor de n asignado en la funcion menos 1 y pedimos que retorne ese nuevo valor 


if __name__ == '__main__': #Inicializamos una funcion principal
    
    n = 5000 #Asignamos que el valor de n vale 1000

    comienzo = time.time() #Asignamos a la variable comienzo una funcion time que esta dentro de la biblioteca time
    factorial(n) #Pedimos el factorial de 1000
    final = time.time() #Asignamos a la variable final la funcion time contenida el la bilbioteca time
    print(final - comienzo) #Restamos el resultado de las 2 variables para medir el tiempo de ejecucion

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo) #Se repite todo el proceso de arriba, per ahora con la reasignacion de las variables y con la funcion recursiva, esto con el objetivo de comparar la rapidez de cada funcion
    




