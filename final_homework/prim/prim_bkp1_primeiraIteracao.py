#TODO: cria nó
#TODO: arestas
#TODO: peso das arestas
import random
nos = 'ABCDEFG'
print('NÓS: ', nos)

arestas = [['AB', 7],
           ['AD', 5],
           ['BC', 8],
           ['BD', 9],
           ['BE', 7],
           ['CE', 5],
           ['DE', 15],
           ['DF', 6],
           ['EF', 8],
           ['EG', 9],
           ['FG', 11]]
grafo ={}
for aresta in arestas:
    grafo[aresta[0]] = aresta[1]

print('GRAFO: ', grafo)

#TODO: algoritmo parte 1 - escolha do pivô

# i_aresta = random.randrange(0, len(arestas))
# pivo = arestas[i_aresta][0][random.randint(0, 1)]
# print('\ni_areta: {}\naresta: {}\npivo: {}'.format(i_aresta, arestas[i_aresta], pivo))

pivo = 'D'
print('\npivo: {}'.format(pivo))

#TODO: algoritmo parte 2 - selecionar aresta e adicioná-la ao conjunto de arestas do subgrafo(árvore mínima)
menor_peso = None
menor_aresta = None

nos_processados = [pivo]
arestas_processadas = {}
iteracao = 0

for no in nos_processados:
    for aresta in arestas:
        if not aresta[0] in arestas_processadas:
            if no in aresta[0]:
                if menor_peso == None:
                    menor_peso = aresta[1]
                    menor_aresta = aresta[0]

                elif aresta[1] < menor_peso:
                    menor_peso = aresta[1]
                    menor_aresta = aresta[0]

arestas_processadas[menor_aresta] = menor_peso
print('ARESTA DE MENOR PESO SELECIONADA: ', menor_peso, menor_aresta)
print('ARESTAS PROCESSADAS: ', arestas_processadas)

#TODO: algoritmo parte 3 - adciona vértice aos processados
no1, no2 = menor_aresta[0], menor_aresta[1]
print('NÓS DA ARESTA SELECIONADA: ', no1, no2)

if not no1 in nos_processados:
    nos_processados.append(no1)

if not no2 in nos_processados:
    nos_processados.append(no2)

print('NÓS PROCESADOS: ', nos_processados)

#TODO: algoritmo parte 4 - checa se todos os vértices foram processados
if len(nos_processados) == len(nos):
    print('TODOS OS NÓS FORAM PROCESSADOS')
else:
    print('RESTAM {} NÓS'.format(len(nos) - len(nos_processados)))


