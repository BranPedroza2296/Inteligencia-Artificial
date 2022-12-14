def divisors(num):
    try:
        if num < 0:
            raise ValueError("ingresa un número positvo")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False



def run():

    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print('Debes ingresar un numero')


if __name__ == '__main__':
    run()
