
class Automovil:
    def __init__(self, modelo, marca, color): #Se inicializa la clase y sus variables, siempre seguir esta sintaxis
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'#se inicializa una variable privada lo sabemos por el guion bajo
        self._motor = Motor(cilindros=4) #le asignamos el valor de 4 a los cilindros directamente que se anadieron primero en la clase motor

    def acelerar(self, tipo= 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en_movimiento'

class Motor:
    def __init__(self, cilindros, tipo= 'gasolina'): #se inicializa la variable tipo ya con un valor
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass