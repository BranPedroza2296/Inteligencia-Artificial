
def morral(tamano_morral, pesos, valores, n): #Creamos nuestra funcion con sus parametros
    
    if n == 0 or tamano_morral == 0: #Si nuestra variable n es 0 o el tamanio del morral es 0 simplemente retornamos un 0
        return 0
    
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1) #Si la lista en la siguiente posicion de n es mayor al tamanio del morral, retornamos la funcion con los parametros, pero, disminuimos el valor de n para que revise el siguiente elemento de la lista 
    
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
               morral(tamano_morral, pesos, valores, n - 1)) #la funcion max, escoge el valor mas alto posible de una comparacion, en caso de que escoja la primera opcion, restamos ese valor y le restamos el peso al morral, dejandonos menos espacio, en caso de que escoja la segunda opcion, simplemente nos recorremos a la siguiente opcion para que la revise
    
   


if __name__ == '__main__': #Inicializamos la funcion pincipal
    valores = [60, 100, 120] #Creamos una lista con sus respectivos valores
    pesos = [10, 20, 30] #Creamos una lista con sus respectivos pesos
    tamano_morral = 50 #Creamos una variable que contiene el limite del morral
    n = len(valores) #Creamos una variable que tiene la longitud de la variable valores
    
    
    resultado = morral(tamano_morral, pesos, valores, n) #Guardamos la funcion morral en una variable
   
    print(resultado) #Imprimimos la variable resultado
    
    