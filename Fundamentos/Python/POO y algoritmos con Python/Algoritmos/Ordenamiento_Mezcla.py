import random #Importamos la biblioteca random

#Complejidad algoritmica O(nlogn)

def ordenamiento_mezcla(lista): #Declaramos la funcion con el parametro necesario
    if len(lista) > 1: #Condicionamos que si el tamanio de la lista es mayor 1 proceda a lo siguiente
        medio = len(lista) // 2 #asignamos una variable medio, que tome la longitud de la lista y la divida en enetros, eso hace el sigo //
        izquierda = lista[:medio] #Asignamos una variable, que tome los valores de la lista del 0 a la primer mitad
        derecha = lista[medio:] #Asignamos una variable que contenga los valores desde la mitad hasta su final

        print(izquierda, '*' * 5, derecha) #Imprimimos ambas listas para saber su funcionamiento

        ordenamiento_mezcla(izquierda) #Volvemos a llamar la funcion solamente con la parte izquierda
        ordenamiento_mezcla(derecha) #Volvemos a llamar la funcion, solamente con la parte derecha

        i = 0
        j = 0
        k = 0
        #Declaramos tres variables inicializadas en 0 que nos van a servir como iteradores

        while i < len(izquierda) and j < len(derecha): #Mientras la variable i sea menor al tamanio de la lista izquierda y la variable j sea mayor a la longitud de la lista derecha, podemos entrar al ciclo
            if izquierda[i] < derecha[j]: #Si el contenido de la lista izquierda en la posicion i es menor al contenido de la lista derecha en la posicion j continuamos
                lista[k] = izquierda[i] #Asignamos que, el contenido dela lista en la posicion k, sea igual al contenido de la lista en la posicion i
                i += 1 #Le sumamos 1 a la variable i
            else: #Si no se cumple la condicion
                lista[k] = derecha[j] 
                j += 1 #hacemos justo el mismo proceso anterior pero con el contenido de la lista derecha en la posicion j

            k += 1 #Le sumamos 1 a la variable k para que no sea un ciclo infinito

        while i < len(izquierda): #Mientras que la variable i sea menor a la longitud de la lista izquierda, podemos continuar
            lista[k] = izquierda[i]# Asignamos que, el contenido dela lista en la posicion k, sea igual al contenido de la lista en la posicion i
            i += 1
            k += 1 #Le sumamos una unidad a las variables

        
        while j < len(derecha): # Mientras que la variable i sea menor a la longitud de la lista derecha, podemos continuar
            lista[k] = derecha[j] # Asignamos que, el contenido dela lista en la posicion k, sea igual al contenido de la lista en la posicion j
            j += 1
            k += 1 #Le sumamos una unidad a las variables


        print(f'izquierda {izquierda}, derecha {derecha}') 
        print (lista)
        print('-' * 50) #Imprimimos las 3 listas para saber como se estan ejecutando y lo separamos los procesos con 50 simbolos *


    return lista #Retornamos la lista




if __name__ == '__main__': #Inicializamos la funcion principal
    
    tamano_lista = int(input('Por favor, ingrese el tamanio de la lista ')) #Le pedimos al usuario que declare el tamanio de la lista

    lista = [random.randint(0 , 100) for i in range(tamano_lista)] #Creamos la lista a partir de la funcion randint que viene en la bibioteca random, con numeros del 0 al 100 a partir del rango que nos asigno el usuario
    print(lista) #Imprimimos la lista
    print('-' * 20) #Imprimimos el simbolo - 20 veces

    lista_ordenada = ordenamiento_mezcla(lista) #Asignamos una variable que contenga la funcion del ordenamiento de la lista
    print(lista_ordenada) #Imprimimos la lista ordenada

