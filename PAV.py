from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)


def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    def vecinoMasCercano(self):
        ni = random.choice(list(self.V))
        result=[ni]
        while len(result) < len(self.V):
            ln = set(self.vecinos[ni])
            le = dict()
            res =(ln-set(result))
            for nv in res:
                le[nv]=self.E[(ni,nv)]
            menor = min(le, key=le.get)
            result.append(menor)
            ni=menor
        return result
        
        

    
			
g= Grafo()
g.conecta('NL','TAM',286)
g.conecta('NL','SLP',564)
g.conecta('NL','CHIA',1773)
g.conecta('NL','CHIHU',852)
g.conecta('NL','BC',1607)
g.conecta('NL','ZAC',511)
g.conecta('NL','GUE',1306)
g.conecta('NL','SIN',1141)
g.conecta('NL','QUER',756)
g.conecta('SLP','TAM',416)
g.conecta('SLP','CHIA',1230)
g.conecta('SLP','CHIHU',1018)
g.conecta('SLP','BC',1719)
g.conecta('SLP','ZAC',194)
g.conecta('SLP','GUE',764)
g.conecta('SLP','SIN',994)
g.conecta('SLP','QUER',208)
g.conecta('TAM','CHIA',1327)
g.conecta('TAM','CHIHU',1107)
g.conecta('TAM','BC',1778)
g.conecta('TAM','ZAC',600)
g.conecta('TAM','GUE',1160)
g.conecta('TAM','SIN',1397)
g.conecta('TAM','QUER',610)
g.conecta('CHIA','CHIHU',2249)
g.conecta('CHIA','BC',2738)
g.conecta('CHIA','ZAC',1423)
g.conecta('CHIA','GUE',1140)
g.conecta('CHIA','SIN',2110)
g.conecta('CHIA','QUER',1038)
g.conecta('CHIHU','BC',923)
g.conecta('CHIHU','ZAC',832)
g.conecta('CHIHU','GUE',1786)
g.conecta('CHIHU','SIN',1191)
g.conecta('CHIHU','QUER',1233)
g.conecta('BC','ZAC',1547)
g.conecta('BC','GUE',2182)
g.conecta('BC','SIN',993)
g.conecta('BC','QUER',1876)
g.conecta('ZAC','GUE',962)
g.conecta('ZAC','SIN',806)
g.conecta('ZAC','QUER',412)
g.conecta('GUE','SIN',1612)
g.conecta('GUE','QUER',562)
g.conecta('SIN','QUER',1117)

print(g.kruskal())
#print(g.shortest('c'))


#print(g)
k = g.kruskal()
print([print(x, k.E[x]) for x in k.E])

for r in range(10):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)

vmc = g.vecinoMasCercano()
print(vmc)
c=0
for f in range(len(vmc) -1):
    c += g.E[(vmc[f],vmc[f+1])]
    print(vmc[f], vmc[f+1], g.E[(vmc[f],vmc[f+1])] )
    
c += g.E[(vmc[-1],vmc[0])]
print(vmc[-1], vmc[0], g.E[(vmc[-1],vmc[0])])
print('vmc costo',c)


data =['NL','SLP','TAM','CHIA','CHIHU','BC','ZAC','GUE','SIN','QUER']
tim=time.clock()
per = permutation(data)
vm, rm= 100000000000,[]
for e in per:
    #print(e)
    c=0
    for f in range(len(e) -1):
        c += g.E[(e[f],e[f+1])]
        #print(e[f], e[f+1], g.E[(e[f],e[f+1])] )
        
    c += g.E[(e[-1],e[0])]
    #print(e[-1], e[0], g.E[(e[-1],e[0])])
    if c < vm:
        vm,rm= c,e
    #print('e costo',c)
print(time.clock()-tim)
print('minimo exacto',vm,rm)
