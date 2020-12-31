#funcao recursiva escavar
#a pá escavadeira só escava 10 metros cúbicos por vez

import time


rejeitos = int(input('Entre com a quantidade de metros cúbicos de rejeitos: '))
n_escavacoes = 0

def escavar(rejeitos):
	global n_escavacoes

	rejeitos = rejeitos - 10
	n_escavacoes += 1

	if rejeitos > 0:
		escavar(rejeitos)
	else:				
		print("Escavou em", n_escavacoes, "pazada(s)")

	return n_escavacoes

tempo_inicial = time.time()
escavar(rejeitos)
print("--- %s segundos ---" % (time.time() - tempo_inicial))