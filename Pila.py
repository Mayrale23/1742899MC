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
