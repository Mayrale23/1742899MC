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
        self.E[(m, a)] = self.E[(a, m)] = peso 
        self.vecinos[m].add(a)
        self.vecinos[a].add(m)
