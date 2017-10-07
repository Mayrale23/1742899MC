cnt = 0

def burbuja(arreglo):
    aux=arreglo[:]
    global cnt
    for a in range(len(arr)):
        for b in range(0,len(arreglo)-a-1):
            if(aux[b]>aux[b+1]):
                  aux[b],aux[b+1]=aux[b+1],aux[b]
                  cnt+=1
    return aux

import random
m = random.sample(range(0,300),100)
print(m)
rsorted=burbuja(m)
print(cnt)
print(msorted)
