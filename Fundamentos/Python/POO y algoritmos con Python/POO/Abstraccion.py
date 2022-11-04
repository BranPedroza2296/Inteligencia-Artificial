
class  Lavadora: #Se crean funciones internas dentro de la clase, esto es la abstraccion
    
    def __init__ (self): #Puedo crear la clase sin metodos o nada en ella
        pass

    def lavar(self, temeratura = 'caliente'):
        self._llenar_tanque_de_agua(temeratura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self,tempertura):
        print(f'LLenando el tanque con agua {tempertura}')

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')   


if __name__ == '__main__':

    lavadora = Lavadora()
    lavadora.lavar()