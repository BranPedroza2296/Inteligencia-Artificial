from time import sleep
import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1 #retorna el valor pero pausando la funcion
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

#Version compacta:
#/def fibonacci_gen():
    #a, b = 0, 1
    #while True:
        #yield a
        #a, b = b, a+b





if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(.5)