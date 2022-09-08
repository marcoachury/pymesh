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
            if malla[via][1] != nodo:  #Elimina vias que apuntan al mismo nodo
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

# OJO ESTA FUCION NO ESTÁ COMPLETA    
    '''
    #agrego las vias paso 2
    for nodo1 in paso1:
        segundos.append([nodo1, conecta(malla, nodo1)])
    return segundos
    
'''

'''Nodos_alcanzables(malla, nodo)
Calcula los nodos que son alcanzables en ese numero de pasos
devuelve una lista.  Desde el 'nodo', que el punto donde inicia la busqueda
Los siguientes elementos son sublistas con los elementos alcanzables
en cada paso adicional.

Entonces la salida es una lista que contiene...:
[0] es el nodo de origen
[1] devuelve los nodos alcanzables en un paso (es lo mismo que la funcion vecinos)
[2] Alcanzabeles en dos pasos (como en la funcion vecinos_de_vecinos)
[3] Alcanzables en 3 pasos
...


'''
def nodos_alcanzables(malla, nodo):   
    alcanzados=[nodo]
    #Elemento 0 es el nodo de origen. (Nivel 0)
    
    nivel=vecinos(malla, nodo)  #(Nivel 1) Segundo elemento, los vecinos directos
    if len(nivel) == 0:
        #print("DEBUG: nivel: ", nivel)
        return alcanzados  #?? Or return -1
    
    alcanzados.append(nivel)   
    i=1 # Ya está lleno el nivel 1
    while (1==1):
        #print("[Debug: Dentro del While]")
        nivel=[] #Se vacía para empezar de nuevo cada que vez que avanza un nivel
        temp=[]
        i=i+1 #Nivel que vamos a llenar, empezará desde el nivel 2
        for j in alcanzados[i-1]:  #Estos son los del nivel anterior, de 1 en adelante
            temp = vecinos(malla, j) #Buscar vecinos del nivel anterior para llenar nivel actual
            #print("DEBUG: i, j, Temp=", i, j, temp)
                          
            for k in temp: #Para cada uno de los recien hayados
                if nivel.count(k)==0 and alcanzados[i-1].count(k)==0 and alcanzados[i-2].count(k)==0 and k!=nodo:
                    nivel.append(k) #Eliminar repetidos
        print (len(nivel), alcanzados)
        
        if len(nivel)==0:        # Si no se encuentra nada nuevo...
            return alcanzados    # Salir entregando lo encontrado hasta ahora
        alcanzados.append(nivel) # Si se encontraron nuevos, agregarlos y seguir el ciclo


''' A cuantos pasos del nodo1 está el nodo2'''
def a_cuantos_nodos(malla, nodo1, nodo2):
    alcanzados = nodos_alcanzables(malla, nodo1)
    for i in range (1, len(alcanzados)+1):
        for j in range(len(alcanzados[i])):
            if alcanzados[i][j] == nodo2:
                return i
    
    



