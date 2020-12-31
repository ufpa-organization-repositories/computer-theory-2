# funcao fibonacci recursiva

import time

x = int(input("Entre com o inteiro da série de fibonacci: "))
fibonacci = 0
contador = -1

def fib(x, contador):
	global fibonacci

	# print('contador: ', contador)	
	if not contador == x:
		contador += 1						
		fibonacci += contador
		# print('fibonacci parcial: ', fibonacci)
		fib(x, contador)		
	else:
		print("fibonacci:", fibonacci)
		

	return fibonacci

tempo_inicial = time.time()
fib(x, contador)
print("--- %s segundos ---" % (time.time() - tempo_inicial))