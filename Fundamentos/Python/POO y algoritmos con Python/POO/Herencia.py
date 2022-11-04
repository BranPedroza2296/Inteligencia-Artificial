
class Rectangulo:

    def __init__ (self, base: int, altura: int) ->int:
        self.base = base
        self.altura = altura

    def area(self)->int:
        return self.base * self.altura

    
class Cuadrado(Rectangulo): #Con esto se crea la sub clase cuadrado la cual es una extension de la super clase rectangulo, con esto la clase cuadrado tiene sus instancias

    def __init__(self, lado): #Aqui definimos que la instanica recibe una variable llamada lado
        super().__init__(lado, lado) #al poner la palabra reservada "super" se inician las variables de base y alturas referidas a la superclase rectangulo

    
if __name__ == '__main__':
    
    rectangulo = Rectangulo(3, 4) #definimos los parametros de la base y la altura indicandolos directamente, se veria el mismo resultado si solo se escribiera el 3 y el 4 en los parametros
    
    print(rectangulo.area())

    cuadrado = Cuadrado(lado= 5)
    print(cuadrado.area()) #hereda la instncia de area que era en su principio del rectangulo
