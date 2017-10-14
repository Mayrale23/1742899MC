memo={}
contador=0
def fibo3(n):
	global memo 
	global contador
	contador+=1
	if n==0 or n==1:
		return(1)
	if n in memo:
		return memo[n]
	else:
		val=fibo3(n-2)+fibo3(n-1)
		memo[n]=val
		return val
