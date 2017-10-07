class Pila:
	def __init__(self):
		self.pila=[]
	def obt (self):
		return self.pila.pop()
	def met (self,e):
		self.pila.append(e)
	@property
	def lon (self):
		return len (self.pila)
    
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
        
   def D_F_S(g,ni):
	visit=[]
	f=Pila()
	f.met(ni)
	while(f.lon>0):
		na=f.obt()
		visit.append(na)
		ra=g.vecinos[na]
		for nodo in ra:
			if nodo not in visit:
				f.met(nodo)
	return visit
     
