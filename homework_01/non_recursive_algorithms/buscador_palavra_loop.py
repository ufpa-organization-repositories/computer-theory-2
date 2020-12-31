# buscador de palavras em texto

import time

contador = 0
n_ocorrencias = 0

texto = input("Entre com o texto: ")
palavra = input("Entre com a palavra a ser buscada: ")		

print(len(palavra))

tempo_inicial = time.time()
for elem in texto:
	# print("elem", elem, type(elem))
		
	if elem == palavra[contador]:
		# print('Caractere encontrado')
		contador += 1

		if contador == len(palavra):
			# print("Palavra encontrada")
			n_ocorrencias +=1
			contador = 0
	else:		
		contador = 0
	

print('n_ocorrencias:', n_ocorrencias)
print("--- %s segundos ---" % (time.time() - tempo_inicial))