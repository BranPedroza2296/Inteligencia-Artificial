from bokeh.plotting import figure, output_file, show #Importamos 3 funciones de la biblioteca bokeh que nos permiten poder ver nuestro grafico en html

if __name__ == '__main__':

    output_file('graficado_simple.html') #Creamos nuestro archivo html
    fig = figure() #Guardamos la funcion figure en una variable

    total_valores = int(input('Por favor, ingrese los valores que desea graficar ')) #Le pedimos al usuario que asigne los valores que desea en una variable
    x_valores = list(range(total_valores)) #Creamos una lista que se almacena en la variable, la cual tiene el tamanio asignado por el usuario anteriormente
    y_valores = [] #Inicialisamos una lista con cero elementos

    for x in x_valores: #creamos un ciclo que vaya recorriendo de uno en uno las posiciones de los valores de x
        val = int(input(f'Ingresa el valor de y para {x} ')) #Le pedimos al usuario que asigne los valores de y para cada x
        y_valores.append(val) #Los guardamos segun vayan siendo puestos por el usuario

    fig.line(x_valores, y_valores, line_width=2) #Le pedimos a la funcion line que haga la linea a partir de los valores de x y Y, y nos haga elancho de 2
    show(fig) #Muestra la grafica
