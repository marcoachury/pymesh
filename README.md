# pymesh
Intento de crear funciones para analizar una red mesh.   Function to analize mesh net.  (WARNING Spanish inside!)

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
Distancia e hasta c = 6

'''

'''Datos de ejemplo. Cada elemento de la lista es un vertice o via.
Contiene dos nodos y valor'''
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
