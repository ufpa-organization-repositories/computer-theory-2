import random
def choose_pivot(nos):
    i = random.randrange(0, len(nos))
    pivo = nos[i]
    return pivo

def get_min_weight_in_not_processed_adjacent_arrows(adjacencias):
    menor_peso = None

    for aresta, peso in adjacencias.items():
        if menor_peso == None:
            menor_peso = peso

        elif peso < menor_peso:
            menor_peso = peso

    return menor_peso

def get_pivo_adjacent_arrows(pivo, arestas):
    arestas_adjacentes_pivo = {}
    for aresta in arestas:
        no1, no2 = aresta[0][0], aresta[0][1]
        if pivo == no1 or pivo == no2:
            arestas_adjacentes_pivo[aresta[0]] = aresta[1]

    return arestas_adjacentes_pivo

def get_node_adjacent_arrows(nos, arestas, adjacencia_corrente, arestas_processadas):
    # adiciona todas as arestas adjacentes que encontrar, pois a lista de arestas processadas esta vazia
    for no in nos:
        if arestas_processadas != {}:
            for aresta in arestas:
                if not aresta[0] in arestas_processadas.keys():
                    no1, no2 = aresta[0][0], aresta[0][1]
                    if (no == no1 or no == no2):
                        adjacencia_corrente[aresta[0]] = aresta[1]

        # adiciona as arestas adjacentes nao processadas
        else:

            for aresta in arestas:
                if not aresta[0] in arestas_processadas.keys():
                    no1, no2 = aresta[0][0], aresta[0][1]
                    if (no == no1 or no == no2) and not aresta[0] in arestas_processadas.keys():
                        adjacencia_corrente[aresta[0]] = aresta[1]

    adjacencia_corrente_temp = adjacencia_corrente.copy()

    for adjacencia in adjacencia_corrente_temp.keys():
        # if adjacencia in arestas_processadas.keys():
        if adjacencia[0] in nos_processados and adjacencia[1] in nos_processados:
            del adjacencia_corrente[adjacencia]

    return adjacencia_corrente

def get_not_pocessed_arrows_with_min_weigth_between_not_processed_adjacent_arrows(peso, adjacencia):
    arestas_menor_peso = []

    for aresta, peso in adjacencia.items():
        if peso == menor_peso:
            arestas_menor_peso.append(aresta)

    aresta_menor_peso = random.choice(arestas_menor_peso)
    return aresta_menor_peso

def add_nodes_to_processed(menor_aresta, nos_processados):
    no1, no2 = menor_aresta[0], menor_aresta[1]

    if not no1 in nos_processados:
        nos_processados.append(no1)

    if not no2 in nos_processados:
        nos_processados.append(no2)

    return nos_processados

def add_arrow_to_processed(aresta, peso, arestas_processadas):
    arestas_processadas[aresta] = peso
    return arestas_processadas

def check_if_all_nodes_are_processed(nos, nos_processados):
    end = False
    if len(nos_processados) == len(nos):
        print('TODOS OS NÓS FORAM PROCESSADOS')
        end = True
    else:
        print('RESTAM {} NÓS'.format(len(nos) - len(nos_processados)))
        end = False

    return end

nos = 'ABCDEFG'
arestas_adjacentes_nao_processadas = {}
arestas_processadas = {}

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
print('GRAFO: ', arestas)

pivo = choose_pivot(nos)
# pivo = 'D'
print('PIVO: ', pivo)
nos_processados = [pivo]
end = check_if_all_nodes_are_processed(nos, nos_processados)
iteracao = 1

while not end:
    print('\nITERACAO: ', iteracao)
    arestas_adjacentes_nao_processadas = get_node_adjacent_arrows(nos_processados, arestas, arestas_adjacentes_nao_processadas,
                                                                  arestas_processadas)

    print('ARESTAS ADJACENTES: {}'.format(arestas_adjacentes_nao_processadas))

    menor_peso = get_min_weight_in_not_processed_adjacent_arrows(arestas_adjacentes_nao_processadas)
    aresta_menor_peso = get_not_pocessed_arrows_with_min_weigth_between_not_processed_adjacent_arrows(menor_peso, arestas_adjacentes_nao_processadas)
    print('menor peso: {}\naresta_menor_peso: {}'.format(menor_peso, aresta_menor_peso))

    nos_processados = add_nodes_to_processed(aresta_menor_peso, nos_processados)
    arestas_processadas = add_arrow_to_processed(aresta_menor_peso, menor_peso, arestas_processadas)
    print('ARESTAS PROCESSADAS: ', arestas_processadas)
    print('NOS PROCESSADOS: ', nos_processados)
    end = check_if_all_nodes_are_processed(nos, nos_processados)
    print('end: ', end)
    iteracao += 1

print(arestas_processadas)
