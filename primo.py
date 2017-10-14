contador=0
def primo (n):
	global contador
	contador=0
	for i in range(2, round(n**(1/2)+1)):
		contador+=1
		if n%i==0:
			return("no es primo")
	return ("es primo")
