import random

#La complejidad algoritmica es O(n) ya que tenemos un solo ciclo que recibe un n

def busqueda_lineal(lista, objetivo): #Definimos una funcion que reciba una lista y un objetivo
    match = False #Asignamos a la variable el valor de False
    for elemento in lista: #Se abre un ciclo que revisa uno por uno cada elementi en la lista
        if elemento == objetivo: 
            match = True #Se condiciona que si el elemento es igual a el objetivo buscado, el valor de la variable match, cambia a True
            break #Paramos el ciclo en caso de encontrar el resultado
    
    return match #Retornamos el valor de la variable match

if __name__ == '__main__': #DEclaramos una funcion main
    tamano_lista = int(input('Por favor, introduce el tamanio de la lista ')) #Lepedimos al usuario que asigne el tamanio de la lista
    objetivo = int(input('Indique el numero que desea encontrar ')) #Le pedimos al usuario que asigne el numero que desea encontrar

    lista = [random.randint(0 , 100) for i in range(tamano_lista)] #Creamos la lista a partir de numeros aleatorios del 1 al 100 en la funcion randint contenida en la biblioteca random, por cada numero contenido en el rango de la lista que ingreso el usuario

    encontrado = busqueda_lineal(lista, objetivo) #Definimos una variable que contenga la funcion de busqueda_lineal con todo y sus parametros
    print(lista) #imprimimos la lista por mera curiosidad
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') #Concatenamos la impresion con la variable objetivo y ademas, abrimos una funcion condicional que nos diga si esta o no esta la variable encontrado en la lista 


