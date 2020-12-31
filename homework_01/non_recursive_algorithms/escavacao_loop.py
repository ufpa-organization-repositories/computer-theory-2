#funcao recursiva escavar
#a pá da escavadeira só escava 10 metros cúbicos por vez

import time

n_escavacoes = 0

rejeitos = int(input('Entre com a quantidade de metros cúbicos de rejeitos: '))

tempo_inicial = time.time()
while (rejeitos >0):
	rejeitos = rejeitos - 10
	n_escavacoes += 1	

print("Escavou em", n_escavacoes, "pazada(s)")
print("--- %s segundos ---" % (time.time() - tempo_inicial))

