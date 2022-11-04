import random #Importamos la libreria random

#Su complejidad algoritmica es O(n**2)

def ordenamiento_por_insercion(lista): #Definimos la funcion con su parametro

    for indice in range(1, len(lista)): #Iniciamos un ciclo el cual el indice va recorriendo de uno en uno desde la posicion 1, no la 0, hasta el ultimo elemento, el cual es el tamanio de la lista
        valor_actual = lista[indice] #Se crea una variable con el valor de la lista en la posicion del indice
        posicion_actual = indice #Se crea una variable con el valor del indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual: #MIentras la posicion actual sea mayor que 0 y mayor al valor de la posicion actual de la lista que cumpla con que es mayor al valor actual, se procede al ciclo
            lista[posicion_actual] = lista[posicion_actual - 1] #Asigno el valor de la lista anterior para asi recorrerme a la izquierda
            posicion_actual -= 1 #Resto una posicion para revisar el siguiente nuermo a la izquierda

        lista[posicion_actual] = valor_actual #Se guarda el numero del valor actual en el numero que se encuentra en la posicion actual de la lista

    return lista #Retornamos la lista ordenada

if __name__ == '__main__': #DEclaramos una funcion main

    tamano_lista = int(input('Por favor, introduce el tamanio de la lista ')) #Lepedimos al usuario que asigne el tamanio de la lista
    lista = [random.randint(0 , 100) for i in range(tamano_lista)] #Creamos la lista a partir de numeros aleatorios del 1 al 100 en la funcion randint contenida en la biblioteca random, por cada numero contenido en el rango de la lista que ingreso el usuario
    print(lista)#Imprimimos la lista sin ordenar
    lista_ordenada = ordenamiento_por_insercion(lista) #Guardamos en una variable la lista ya ordenada
    print(lista_ordenada) #Imprimimos la lista ya ordenada