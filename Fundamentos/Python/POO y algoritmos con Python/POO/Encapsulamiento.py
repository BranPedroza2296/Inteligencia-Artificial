class CasillaDeVotacion():
    def __init__(self, identificador, pais,region):
        self._identificador = identificador #El guin bajo indica que es protegido
        self._pais = pais
        self._region = region
        

    @property #Podemos cambiarl los valores a partir del decorador property
    def region(self):
        return self._region

    @region.setter
    def region(self, nregion):
        self._region = nregion
        print(self._region) #Aqui cambiamos el nombre y lo mostramos en pantalla
        


if __name__ == '__main__':
    
    casilla = CasillaDeVotacion(123, 'Ciudad de Mexico', 'Morelos')
    print(casilla.region)
    casilla.region = 'CDMX'
    
   
