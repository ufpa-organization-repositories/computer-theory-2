import random
from trabalhoFinal.kruskal.teste import join_adjacent_nodes

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

def insert_arrow_into_vertices_sets(aresta_menor_peso, conjuntos_vertices):
    n1_in = False
    n2_in = False

    no1, no2 = aresta_menor_peso[0], aresta_menor_peso[1]
    for conjunto in conjuntos_vertices:
        for no in conjunto[1]:
            if no1 == no: n1_in = True
            if no1 == no: n2_in = True

    if not (n1_in and n2_in):
        conjuntos_vertices.append(str(no1 + no2))

    return conjuntos_vertices

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

    # if aresta_menor_peso in arestas:
    #     arvore_geradora_minima[arvore_geradora_minima.__len__() + 1] = [menor_peso, aresta_menor_peso]
    #     print('ARVORE ATUALIZADA: ', arvore_geradora_minima)

    # conjuntos_vertices = nos_adjacentes


    # if iteracao == 3:
    #     print(iteracao)
        # break

    iteracao += 1

print('\n\nARVORE GERADORA MINIMA OBTIDA: ', arvore_geradora_minima)