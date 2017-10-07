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
