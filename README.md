# pymesh
Function to analize mesh net.  (WARNING Spanish inside!)

Intento de crear funciones para analizar una red mesh.   

La red mesh se guarda como una lista de vertices "vias".
Los vertices pueden estar repetidos, incluso pueden
conectar un nodo con el mismo

La aplicación óptima es buscar las rutas mas cortas o las mas eficientes.

Datos de ejemplo actual

Via de a hasta b = 5
Via de a hasta c = 3
Via de d hasta b = 3
Via de c hasta b = 8
Via de a hasta i = 2
Via de e hasta f = 2
Via de e hasta d = 5
Via de e hasta c = 6
Via de b hasta c = 2
Via de e hasta d = 2
Via de c hasta b = 2
Via de f hasta d = 2
Via de d hasta d = 3
Via de k hasta k = 3

Los valor representan costo, distancia, tiempo, o cualquier otra variable 
que se debe tener en cuenta para optimizar el recorrido.


Estos datos se representan de esta manera:


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



A partir de esos datos se hacen los caculos mostrados en el ejemplo:



