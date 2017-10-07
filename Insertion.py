cnt=0
def metodo_insertion(arreglo):
	global cnt
	for num in range(1,len(arreglo)):
		valor=arreglo[num]
		i=num-1
		while i>=0:
			cnt+=1
			if valor<arreglo[i]:
				arreglo[i+1]=arreglo[i]
				arreglo[i]=valor
				i-=1
			else:
				break
	return arreglo


import random
m = random.sample(range(0,300),100)
print(m)
msorted=metodo_insertion(m)
print(cnt)
print(msorted)
