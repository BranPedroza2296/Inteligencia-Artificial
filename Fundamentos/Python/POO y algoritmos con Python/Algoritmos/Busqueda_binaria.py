import random #Importamos la bilbioteca random

#La complejidad algoritmica es O(logn)

def busqueda_binaria(lista, comienzo, final, objetivo): #Declaramos la funcion con sus parametros
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final -1]}')
    if comienzo > final:
        return False #Le condicionamos que si el comienzo de la lista es mayor que el final simplemente no se va a encontrar el elemento que se busca

    medio = (comienzo + final) //2 #El simbolo // indica division de enteros. La variable guarda el proceso de dividir la lista en 2 partes para la busqueda

    if lista[medio] == objetivo:
        return True #Se crea la condicion, en caso de que el elemento buscado este justo en el medio de la lista, el objetivo fue encontrado
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio +1 , final, objetivo) #La condiciones que, en caso de que el elemento no se encuentre en medio, se ba buscando en la segunda mitad de la lista
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo)#La condicion que, en caso de que el elemento no se encuentre en medio, se busca en la primera mitad de la lista

#Asi, se va dividiendo en dos partes la lista una y otra vez por recursividad, con el nuevo parametro de la variable medio, hasta encontrar el objetivo, en caso de que se encuentre



if __name__ == '__main__': #Inicializamos la funcion main
    
    tamano_lista = int(input('Por favor indique el tamanio de la lista ')) #El usuario asigna el tamanio de la lista guardandolo en la variable
    objetivo = int(input('Que numero desea encontrar ')) #El usuario asigna el objetivo guardandolo en la varibale

    lista = sorted([random.randint(0, 100) for i in range (tamano_lista)]) #Se crea la variable lista, la cual contiene una lista ordenada gracias al sorted. Los numeros de la lista surgen de la funcion randint contenida el la biblioteca random. le decimos que sean numeros del 1 al 100 colocados uno a uno hasta el rango de la lista asignada previamente

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo) #Se declara la variable, la cual contiene la funcion de busqueda binaria con sus parametros

    print(lista) #imprimimos la lista por curiosos
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') #Imprimimos el objetivo mas el condicional que depende de la variable encontrado
