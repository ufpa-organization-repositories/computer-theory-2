# sistema que verifica se uma funcão não é aproximada com a outra

import time

fibonacci = 0
aux = 0

x = int(input("Entre com o inteiro da série de fibonacci: "))

tempo_inicial = time.time()
for i in range(x):
	fibonacci += i + 1

print('fibonacci: ', fibonacci)
print("--- %s segundos ---" % (time.time() - tempo_inicial))


	