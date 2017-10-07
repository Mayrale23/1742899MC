contador=0
def minimo(arr):
  m=arr[0]
  global contador
  for a in arr:
      contador+=1
      if(a<m):
          m=a
 return m
 
 def ordenar(arr)
    aux=arr[:]
    arrsort=[]
    for m in range(len(aux)):
        a=minimo(aux)
        aux.remove(a)
        arrsort.append(a)
    return arrsort
    
import random
r=random.sample(range(0,100)40)
print(r)
rsort=ordenar(r)
print(contador)
print(rsort)
