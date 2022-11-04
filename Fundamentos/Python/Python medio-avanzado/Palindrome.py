def is_palindrome(string: str) -> bool: #le decimos que el parametro es string y que tiene que retornar un booleano
    string = string.replace(' ', '').lower() #quitamos los espacios con la funcion replace, y la funcion lower lo que hace es quitar las mayusculas
    return string == string[::-1] #retornamos el string de manera inversa


def run():
    print(is_palindrome("ana")) #Nos marca un error 


if __name__ == '__main__':
    run()


#mypy (nombre del archivo) --check-untyped-defs  = Al escribirlo en la consola, podemos ver que el error cambia mostrando un error de tipado
