# funcao recursiva que busca palavras em um texto
import time


entrada = input("Entre com o texto: ")
palavra = input("Entre com a palavra a ser buscada: ")		

index = -1
contador = 0
n_ocorrencias = 0

def buscar(texto, palavra, index, contador):
	global n_ocorrencias

	if  index +1 != len(texto):
		# print('Buscando palavra')
		index = index + 1

		if texto[index] == palavra[contador]:
			contador = contador + 1
			# print("caractere encontrado: ", texto[index])
			
			if contador == len(palavra):
				# print("Palavra encontrada")
				n_ocorrencias = n_ocorrencias + 1
				contador = 0										

		else:
			# print("caractere nao encontrado")
		 	contador = 0		 	

		buscar(texto, palavra, index, contador)

	else:
		print("n_ocorrencias:", n_ocorrencias)


	return n_ocorrencias

tempo_inicial = time.time()
buscar(entrada, palavra, index, contador)
print("--- %s segundos ---" % (time.time() - tempo_inicial))
