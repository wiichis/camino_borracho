
from borracho import Lucheins
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show


def caminata(campo, pasos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Will')
    origen = Coordenada(0, 0)
    campo.anadir_borracho(borracho, origen)

    coordenada_x=[]
    coordenada_y=[]

    coordenada_x.append(origen.x)
    coordenada_y.append(origen.y)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        coordenada_x.append(campo.obtener_coordenada(borracho).x)
        coordenada_y.append(campo.obtener_coordenada(borracho).y)

    return (coordenada_x, coordenada_y)

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend_label='distancia media')

    show(grafica)

def main(pasos, tipo_de_borracho):
    campo = Campo()
    coordenada_x, coordenada_y = caminata(campo, pasos, tipo_de_borracho)
    graficar(coordenada_x, coordenada_y)


if __name__ == '__main__':
    
    pasos = 1000
    main(pasos, Lucheins)