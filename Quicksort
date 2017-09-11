cnt = 0

def quicksort(arr):
    global cnt
    if arr==[]:
        return []
    m=arr[0]
    left=[]
    right=[]
    for k in arr[1:]:
        if k<m:
            left.append(k)
        else:
            right.append(k)
        cnt+=1
    return quicksort(left)+[m]+quicksort(right)

import random
a = random.sample(range(0,1000),200)
print(a)
asorted=quicksort(a)
print(cnt)
print(asorted)
