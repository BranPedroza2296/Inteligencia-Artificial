from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs): #Escribimos asi los parametros para indicarle que no importan los parametros
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time #Le agregamos ls funcion a esta nueva funcion
def random_func():
    for _ in range(1, 10000000):
        pass


random_func()