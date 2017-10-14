contador=0
def fibo2(n):
	va=0
	vp=1
	vap=1
	global contador
	if(n==0 or n==1):
		return(1)
	for i in range (2,n+1):
		contador+=1
		va=vp+vap
		vap=vp
		vp=va
	return va
