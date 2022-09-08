'''Ejemplos

Ejemplos de aplicación para la librería

'''

'''Datos de ejemplo. Cada elemento de la lista es un vertice o via.
Contiene dos nodos y valor'''

'''
Proyecto funciones para manejo de redes mesh en python.
Por ahora es ineficiente, porque los datos no están encadenados,
en cada paso debe volver a explorar todo el listado, puede ser
rápido mientras sea pequeño y quepa completo en memoria ram.

La red mesh se guarda como una lista de vertices "vias".
Los vertices pueden estar repetidos, incluso pueden
conectar un nodo con el mismo


Problema de la ruta mas corta
Ruta mas corta desde i hasta f

Distancia a hasta b = 5
Distancia a hasta c = 3
Distancia d hasta b = 3
Distancia c hasta b = 8
Distancia a hasta i = 2
Distancia e hasta f = 2
Distancia e hasta d = 5
Distancia e hasta c = 6...

'''

from pymesh import *


distancias = [
['a','b',5],
['a','c',3],
['d','b',3],
['c','b',8],
['a','i',2],
['e','f',2],
['e','d',5],
['e','c',6],
['b','c',2],
['e','d',2],
['c','b',2],
['f','d',2],
['d','d',3],
['k','k',3],  #Nodo aislado del resto de la malla, ¿Que hacemos con el?
]



print("Ejemplo de datos de red:   ",distancias)
print("Listado nodos de la red:   ", nodos(distancias))
print("Listado de vias nulas      ", nulas(distancias))
print("Via que conecta a y b:     ", primer_trecho(distancias, 'a','b')) 
print("Via que conecta f y e:     ",primer_trecho(distancias, 'f','e'))
print("Vias duplicadas            ", busca_duplicados(distancias))
print("Vias directas entre i y f: ", directos(distancias, 'i', 'f'))
print("Vias directas entre a y b: ", directos(distancias,'a','b'))
print("Vias directas entre d y e: ", directos(distancias, 'd', 'e'))
print("Vias que llegan a 'a':     ", conecta(distancias, 'a'))
print("Vias que llegan a 'e':     ", conecta(distancias, 'e'))
print("Vias que llegan a 'k':     ", conecta(distancias, 'k'))
print("Nodos vecinos de 'a':      ", vecinos(distancias, 'a'))
print("Nodos vecinos de 'b':      ", vecinos(distancias, 'b'))
print("Nodos vecinos de 'i':      ", vecinos(distancias, 'i'))
print("Nodos vecinos de 'd':      ", vecinos(distancias, 'd'))
print("Nodos vecinos de 'k':      ", vecinos(distancias, 'k'))
print("Vias a dos pasos de 'a':   ", a2pasos(distancias, 'a'))
print("Vecinos de vecinos de 'a': ", vecinos_de_vecinos(distancias, 'a'))
print("Vecinos de vecinos de 'k': ", vecinos_de_vecinos(distancias, 'k'))
print("Vecinos de vecinos de 'f': ", vecinos_de_vecinos(distancias, 'a'))
print("Nodos alcanzables desde 'a':", nodos_alcanzables(distancias, 'a'))
print("Nodos alcanzables desde 'k':", nodos_alcanzables(distancias, 'k'))
print("A cuantos pasos de i está f:", a_cuantos_nodos(distancias, 'i', 'f'))

