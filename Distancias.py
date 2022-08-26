'''
Proyecto libreria para manejo de redes mesh en python

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


'''lista_nodos(malla)
Encuentra la lista de todos los nodos existentes en una malla, sin duplicados'''
def nodos(malla):
    nodos=[]
    caminos = len(malla)
    for i in malla:
        #nodo1=i[0]
        #nodo2=i[1]
        if nodos.count(i[0])==0:
            nodos.append(i[0])
        if nodos.count(i[1])==0:
            nodos.append(i[1])
    return nodos

'''Busca las vias nulas, que no van a ninguna parte, que apuntan al mismo nodo
en todos algoritmos de rutas optimas, estas vias no deberían considerarse'''
def nulas(malla):
    nulos=[]
    for via in range(len(malla)):
        if malla[via][0]==malla[via][1]:
            nulos.append(via)
    return nulos

''' busca_duplicados
Devuelve la lista de vertices que repiten la
misma pareja de nodos'''
def busca_duplicados(malla):
    duplicados = []
    num_nodos = len(malla)
    for i in range (num_nodos):
        i0 = malla[i][0]
        i1 = malla[i][1]
        a = [i0,i1]
        b = [i1,i0]
        for j in range(i+1, num_nodos, 1):
            '''print (i,j)
            print (malla[j])
            print (malla[j][0:2])'''
            if ((malla[j][0:2] == a) or (malla[j][0:2] == b)):
                duplicados.append([i,j])
    return duplicados
    

''' primer_trecho()
Devuelve el primer vertice que encuentre conectando directamente
el nodo inicio y el nodo fin.  No devuelve el indice, pero
sirve para verificar rápido si existe vertice directo entre dos
nodos, lo reemplazare por algo mejor.
'''
def primer_trecho(malla, inicio, fin):
    for i in malla:
        if ((i[0:2] == [inicio, fin]) or (i[0:2]==[fin,inicio])):
            return i[2]


'''directos()
Devuelve una lista de los indices de los vertices directos
existentes entre dos nodos'''
def directos(malla, inicio, fin):
    encontrados=[]
    num_nodos = len(malla)
    for i in range (num_nodos):
        if ((malla[i][0:2] == [inicio, fin]) or (malla[i][0:2]==[fin,inicio])):
            encontrados.append(i)
    return encontrados

'''Conecta, lista de los indices de los vertices que conectan con un nodo especifico
pueden haber varios vertices apuntando al mismo nodo vecino, incluso nodos que apuntan a si mismo'''
def conecta(malla, nodo):
    conecta = []
    num_nodos = len(malla)
    for i in range (num_nodos):
        if ((malla[i][0] == nodo) or (malla[i][1] == nodo)):
            conecta.append(i)
    return conecta    

'''vecinos(malla, nodo)
devuelve la lista de los vecinos conectados al nodo en forma directa'''
def vecinos(malla, nodo):
    v1=[]
    vias = conecta(malla, nodo)
    if vias == []:  #Esto nunca debería pasar, un nodo desconectado de la red?
        return []  #devolver vacio o causar una excepcion?
    for via in vias:
        #print (via)
        if malla[via][0]==nodo:
            v1.append(malla[via][1])
        elif malla[via][1]==nodo:
            v1.append(malla[via][0])
        else:
            print("ERROR en vecinos()")  #Esto nunca debería ocurrir
            pass
    return v1


def vecinos_de_vecinos(malla,nodo):
    v1 = vecinos(malla, nodo)
    vecinos2 = []
    for v in v1:
        v2=vecinos(malla,v)
        for nodov2 in v2:
            #print("nodo v2: ", v2)
            if nodov2 != nodo:
                if vecinos2.count(nodov2)==0:
                    vecinos2.append(nodov2)
    return vecinos2

'''a2pasos (A dos pasos) calcula a que nodos se puede llegar en dos pasos
y la lista de las vias usadas en cada caso'''
def a2pasos(malla, inicio):
    rutas =[]
    segundos=[]
    #Empiezo con las vias a un paso
    paso1 = conecta(malla, inicio)
    for i in paso1:
        rutas.append( [i, malla[i] ] )
    return rutas

    
    '''
    #agrego las vias paso 2
    for nodo1 in paso1:
        segundos.append([nodo1, conecta(malla, nodo1)])
    return segundos
    
'''

            
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
print("Nodos vecinos de 'k':      ", vecinos(distancias, 'k'))
print("Vias a dos pasos de 'a':   ", a2pasos(distancias, 'a'))
print("Vecinos de vecinos de 'a': ", vecinos_de_vecinos(distancias, 'a'))
print("Vecinos de vecinos de 'k': ", vecinos_de_vecinos(distancias, 'k'))
print("Vecinos de vecinos de 'f': ", vecinos_de_vecinos(distancias, 'a'))


#Para ir desde i hasta f
'''caminar(distancias, inicio,fin)
mejor = primer_trecho(inicio, fin)
    if mejor !=[]
        print (mejor)
        mejor return 
'''
    
    
    



