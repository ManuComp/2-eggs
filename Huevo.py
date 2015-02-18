import random 

def optimo (n):
	k = 1
	while k**2+ k < 2*n:
		k += 1
	return k

def aventar(n):
	aux = optimo(n)
	aux2 = optimo(n)-1
	rom = random.randrange (1, n+1)
	for i in range (1, optimo(n)+1):
		if aux < rom:
			aux += aux2
			aux2 = aux2-1
		else:
			m = aux -aux2
			while m < rom:
				m += 1
			return m

print (aventar(100))
