import random #Importamos la bilbioteca random

#Su complejidad algoritmica es de O(n**2)

def ordenamiento_burbuja(lista): #Declaramos la funcion con su parametro
    n = len(lista) #le asignamos a la variable n la longitud de la lista

    for i in range(n): #Se declara un ciclo que na de uno en uno por el tamanio de n
        for j in range(0, n - i - 1): #Dentro de el primer ciclo, revisa uno por uno nuevamente cada elemento, inicializando en 0 y llegando hasta la n menos el numero en que va i menos 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #En caso de que un elemento sea mayor al de su continuacion, se intercambian de valor

    return lista #Regresamos la lista ordenada



if __name__ == '__main__': #Inicializamos la funcion main
    
    tamano_lista = int(input('Por favor indique el tamanio de la lista ')) #El usuario asigna el tamanio de la lista guardandolo en la variable

    lista = [random.randint(0, 100) for i in range(tamano_lista)]  # Creamos la lista a partir de numeros aleatorios del 1 al 100 en la funcion randint contenida en la biblioteca random, por cada numero contenido en el rango de la lista que ingreso el usuario
    print(lista) #imprimimos la lista en desorden

    lista_ordenada = ordenamiento_burbuja(lista) #Le asignamos a una variable la lista ordenada
    print(lista_ordenada) #Imprimimos la lista ordenada
