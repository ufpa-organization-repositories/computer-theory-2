def join_adjacent_nodes(conjuntos_vertices):

    #adiciona o primeiro conjunto ao conjunto de nos adjacentes
    aux = [conjuntos_vertices[0]]
    percorrido = []
    nos_processados = {}

    #numero de conjunto de nos adjacentes
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

# conjuntos_vertices = ['ABC', 'ADE', 'FG', 'GH', 'IB', 'WXF', 'XY', 'AZ']
# nos_adjacentes = join_adjacent_nodes(conjuntos_vertices)
# print(conjuntos_vertices)
# print(nos_adjacentes)

# aux = [[5, 'AD'], [6, 'DF'], [7, 'AB'], [7, 'BE'], [8, 'BC'], [8, 'EF'], [9, 'BD'], [9, 'EG'], [11, 'FG'], [15, 'DE']]
# aux.remove([5, 'AD'])
# print(aux)

"""
teste da remocao das arestas
"""


# arestas = [
#             [7, 'AB'],
#             [5, 'AD'],
#             [8, 'BC'],
#             [9, 'BD'],
#             [7, 'BE'],
#             [5, 'CE'],
#             [15, 'DE'],
#             [6, 'DF'],
#             [8, 'EF'],
#             [9, 'EG'],
#             [11, 'FG']
# ]
#
# conjuntos_vertices = ['AD', 'CE', 'DF', 'AB', 'BE']
# nos_adjacencentes = join_adjacent_nodes(conjuntos_vertices)
# print('CONJUNTO VERTICES: ', conjuntos_vertices)
# print('NOS ADJACENTES: ', nos_adjacencentes)
# aux = arestas.copy()
# arestas_a_remover = []
#
# aresta_in_same_set = bool
# for adjacencia in nos_adjacencentes:
#     print('ADJACENCIA: ', adjacencia)
#     print('ARESTAS')
#     for aresta in arestas:
#
#         no1, no2 = aresta[1][0], aresta[1][1]
#         print(aresta)
#
#         if no1 in adjacencia and no2 in adjacencia:
#             print('ARESTA A SER REMOVIDA: ', aresta)
#             arestas_a_remover.append(aresta)
#             aux.remove(aresta)
#
# print(arestas)
# print('->>> ',arestas_a_remover)
# print(aux)