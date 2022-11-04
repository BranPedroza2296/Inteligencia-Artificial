class Coordenada: #se inicializa una clase 
   
    def __init__(self, x, y): #siempre que se incia una clase comenzamos con init entre giones bajos, ademas de la palabra self y los parametros 
        self.x = x
        self.y= y #se crean las instancias de la clase

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2 #tanto otra coordenada como self.x y self.y son ivariables de la instancia
        return (x_diff + y_diff)**0.5 #devolvemos la operacion de las variables


if __name__ == '__main__': #esto inicializa la funcion main
    coord_1 = Coordenada(3, 30)#aqui se crea el objeto con la clase que desarrollamos anteriormente osease la instanica
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))#se imprime el resultao que usan los moldes mencionados arriba, coord1 usa el primer molde y coord2 el segundo molde
    print(isinstance(coord_2,Coordenada))#aqui preguntamos si esas coordenadas son instancias de coordenadas
