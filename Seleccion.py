cnt=0

def seleccion(arreglo):
	aux=arreglo[:]
	global cnt
	for a in range(0,len(arreglo)-1):
		valor=a
		for b in range(a+1,len(arreglo)):
			cnt=cnt+1
			if arreglo[b]<arreglo[valor]:
				valor=b
			if valor!=a:
				aux=arreglo[a]
				arreglo[a]=arreglo[valor]
				arreglo[valor]=aux
	return cnt

import random
m = random.sample(range(0,300),100)
print(m)
msorted=seleccion(m)
print(cnt)
print(msorted)
