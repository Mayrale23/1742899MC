class Fila:
	def __init__(self):
		self.fila=[]
	def obt(self):
		return self.fila.pop()
	def met(self,e):
		self.fila.insert(0,e)
	@property
	def lon (self):
		return len(self.fila)

class Grafo:
 
    def __init__(self):
        self.M = set() 
        self.R = dict() 
        self.vecinos = dict() 
 
    def agregar(self, m):
        self.M.add(m)
        if not m in self.vecinos: 
            self.vecinos[m] = set() 
 
    def conect(self, m, a, peso=1):
        self.agregar(m)
        self.agregar(a)
        self.R[(m, a)] = self.R[(a, m)] = peso 
        self.vecinos[m].add(a)
        self.vecinos[a].add(m)

 def B_F_S(g,ni):
	visit=[]
	f=Fila()
	f.met(ni)
	while(f.lon>0):
		na=f.obt()
		visit.append(na)
		ra=g.vecinos[na]
		for nodo in ra:
			if nodo not in visit:
				f.met(nodo)
	return visit
