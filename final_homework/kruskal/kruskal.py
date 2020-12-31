import random

def get_min_weight(arestas):
    menor_peso = arestas[0][0]
    return menor_peso

def get_arrows_with_min_weigth(peso, arestas):
    arestas_menor_peso = []
    for aresta in arestas:
        if aresta[0] == menor_peso:
            arestas_menor_peso.append(aresta[1])

    return arestas_menor_peso

def get_arrow_with_min_weigth_from_min_weight_arrows_list(min_weight_arrows):
    aresta_menor_peso = random.choice(min_weight_arrows)
    return aresta_menor_peso

def join_adjacent_nodes(conjuntos_vertices):
    # adiciona o primeiro conjunto ao conjunto de nos adjacentes
    aux = [conjuntos_vertices[0]]
    percorrido = []
    nos_processados = {}

    # numero de conjunto de nos adjacentes
    len_aux = 1

    # executa enquanto o numero de conjunto de nos adjacentes aumentar
    # adiciona o primeiro novo conjunto não incluso que encontrar

    while 1:
        for i, conjunto in enumerate(conjuntos_vertices):
            if not conjunto in percorrido:
                percorrido.append(conjunto)

            # varre os nos de cada conjunto
            for i_no, no in enumerate(conjunto):
                nos_processados[no] = False
                # print(i_no, no)

                # verifica se o no pertence a um conjunto já percorrido
                # for j, conjunto_percorrido in enumerate(conjuntos_vertices[:i + 1]):
                for j, conjunto_percorrido in enumerate(conjuntos_vertices):

                    if no in conjunto_percorrido and not i == j:
                        # if no in conjunto_percorrido:

                        # print(no,' PERTENCE A UM CONJUNTO JA PERCORRIDO')

                        # adiciona o no ao conjunto de nos adjacentes
                        for index, elem in enumerate(aux):
                            if no in elem:
                                for a in conjunto:
                                    if not a in aux[index]:
                                        # aux[index] = aux[index] + conjunto.replace(no, '')
                                        aux[index] = aux[index] + conjunto.replace(no, '')

        # print(aux)

        # adiciona o próximo conjunto nao incluso que encontrar
        for conjunto in conjuntos_vertices:

            conjunto_incluso = False

            for vertice in conjunto:
                for conjunto_aux in aux:
                    for vertice_aux in conjunto_aux:
                        # print(vertice, vertice_aux)
                        if vertice == vertice_aux:
                            conjunto_incluso = True

            if not conjunto_incluso:
                aux.append(conjunto)

        # print(aux)

        # verifica se o numero de conjuntos de nos adjacentes aumentou
        # caso nao tenha sido alterado, entao todas as nós adjacentes já foram agrupados

        if len_aux == len(aux):
            stop = True

            # so para a juncao dos nos adjacentes quando todos os nos processados forem inseridos
            for key, value in nos_processados.items():
                for conjunto_aux in aux:
                    for vertice_aux in conjunto_aux:
                        if vertice_aux == key:
                            nos_processados[key] = True

            for key, value in nos_processados.items():
                if not value == True:
                    stop = False

            if stop:
                break

        else:
            len_aux = len(aux)

    return aux

def remove_arrows_which_conect_nodes_in_same_set(arestas, nos_adjacentes):
    # aux = arestas.copy()

    arestas_a_remover = []

    aresta_in_same_set = bool
    for adjacencia in nos_adjacentes:
        # print('ADJACENCIA: ', adjacencia)
        # print('ARESTAS')
        for aresta in arestas:

            no1, no2 = aresta[1][0], aresta[1][1]
            # print(aresta)

            if no1 in adjacencia and no2 in adjacencia:
                print('--------->ARESTA A SER REMOVIDA: ', aresta)
                arestas_a_remover.append(aresta)
                # aux.remove(aresta)
    try:
        for aresta in arestas_a_remover:
            arestas.remove(aresta)
    except:
        pass
    return arestas


# IMPLEMENTACAO
arvore_geradora_minima = {}
print('ARVORE GERADORA MINIMA: ', arvore_geradora_minima)

nos = 'ABCDEFG'
print('NOS: ', nos)

arestas = [[7, 'AB'],
           [5, 'AD'],
           [8, 'BC'],
           [9, 'BD'],
           [7, 'BE'],
           [5, 'CE'],
           [15, 'DE'],
           [6, 'DF'],
           [8, 'EF'],
           [9, 'EG'],
           [11, 'FG']]
arestas = sorted(arestas)
print('ARESTAS: ', arestas)
arestas_processadas = []

conjuntos_vertices = []
print('CONJUNTOS VERTICES: ', conjuntos_vertices)

# INICIO DA BUSCA DAS ARETAS
iteracao = 1
nos_adjacentes = []

while not arestas == []:
    print('\nITERECAO: ', iteracao)
    menor_peso = get_min_weight(arestas)
    print('MENOR PESO: ', menor_peso)

    arestas_menor_peso = get_arrows_with_min_weigth(menor_peso, arestas)
    print('ARESTAS MENOR PESO: ', arestas_menor_peso)

    aresta_menor_peso = get_arrow_with_min_weigth_from_min_weight_arrows_list(arestas_menor_peso)
    print('ARESTA MENOR PESO: ', aresta_menor_peso)

    arvore_geradora_minima[arvore_geradora_minima.__len__() + 1] = [menor_peso, aresta_menor_peso]
    print('ARVORE ATUALIZADA: ', arvore_geradora_minima)

    # conjuntos_vertices = insert_arrow_into_vertices_sets(aresta_menor_peso, nos_adjacentes)
    conjuntos_vertices.append(aresta_menor_peso)
    print('CONJUNTOS VERTICES ATUALIZADO: ', conjuntos_vertices)

    nos_adjacentes = join_adjacent_nodes(conjuntos_vertices)
    print('NOS ADJACENTES: ', nos_adjacentes)

    try:
        arestas.remove([menor_peso, aresta_menor_peso])
        print('ARESTA DE MENOR PESO REMOVIDA: ', arestas)
    except:
        pass

    arestas = remove_arrows_which_conect_nodes_in_same_set(arestas, nos_adjacentes)
    print('ARESTAS SEM LACOS: ', arestas)

    iteracao += 1

print('\n\nARVORE GERADORA MINIMA OBTIDA: ', arvore_geradora_minima)
