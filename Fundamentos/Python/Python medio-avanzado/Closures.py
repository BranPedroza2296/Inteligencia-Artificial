def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes repetir cadenas'
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5) #Guarda el numero 5 como parametro de n
    print(repeat_5('Wero ')) #Una vez guardado el 5 en la variable que contiene la funcion, entra el sgundo valor de tipo string, el cual hara que se complete la funcion


if __name__ == '__main__':
    run()
