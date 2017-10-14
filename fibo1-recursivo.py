contador=0
def fibo1(n):
	global contador
	contador+=1
	if n==0 or n==1:
		return(1)
	return(fibo1(n-2)+fibo1(n-1))
