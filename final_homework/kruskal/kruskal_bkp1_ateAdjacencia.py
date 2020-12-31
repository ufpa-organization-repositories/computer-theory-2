import random
from trabalhoFinal.kruskal.teste import join_adjacent_nodes
arvore_geradora_minima = {}

#TODO: lista de arestas
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

#TODO: ordena as arestas
arestas = sorted(arestas)
print('ARESTAS: ', arestas)

#TODO: conjunto de vertices. Cada conjunto
nos = 'ABCDEFG'

# conjuntos_vertices = {}
conjuntos_vertices = []

# for no in nos:
#     conjuntos_vertices[no] = no

print('CONJUNTOS VERTICES: ', conjuntos_vertices)

#TODO: pegar menor custo
def get_min_weight(arestas):
    menor_peso = arestas[0][0]
    return menor_peso

menor_peso = get_min_weight(arestas)
print('MENOR PESO: ', menor_peso)

#TODO: pegar arestas menor_peso
def get_arrows_with_min_weigth(peso, arestas):
    arestas_menor_peso = []
    for aresta in arestas:
        if aresta[0] == menor_peso:
            arestas_menor_peso.append(aresta[1])

    return arestas_menor_peso

arestas_menor_peso = get_arrows_with_min_weigth(menor_peso, arestas)
print('ARESTAS MENOR PESO: ', arestas_menor_peso)

def get_arrow_with_min_weigth_from_min_weight_arrows_list(min_weight_arrows):
    aresta_menor_peso = random.choice(min_weight_arrows)
    return aresta_menor_peso

aresta_menor_peso = get_arrow_with_min_weigth_from_min_weight_arrows_list(arestas_menor_peso)
print('ARESTA MENOR PESO: ', aresta_menor_peso)

#TODO: remover a aresta selecionada da lista de arestas
arestas_processadas = []
arestas.remove([menor_peso, aresta_menor_peso])
arestas_processadas.append(aresta_menor_peso)
print('ARESTAS ATUALIZADAS: ', arestas)

#TODO: checar se a aresta de menor custo conecta vértices do mesmo conjunto de vértices
# def check_if_arrow_join_vertices_in_same_set(aresta_menor_peso, conjuntos_vertices):
#     same_set = bool
#     no1, no2 = aresta_menor_peso[0], aresta_menor_peso[1]
#     if conjuntos_vertices == {}:
#         same_set = False
#         # conjuntos_vertices['1'] = []
#         # conjuntos_vertices['1'].append(no1)
#         # conjuntos_vertices['1'].append(no2)
#
#     else:
#         for keys, conjunto_vertices in conjuntos_vertices.items():
#             if no1 in conjunto_vertices and no2 in conjunto_vertices:
#                 same_set = True
#             else:
#                 same_set = False
#
#     return same_set

# same_set = check_if_arrow_join_vertices_in_same_set(aresta_menor_peso, conjuntos_vertices)
# print('ARESTA COM NOS NO MESMO SET: ', same_set)

#TODO: adcionar aresta ao conjunto de vertices
def insert_arrow_into_vertices_sets(aresta_menor_peso, conjuntos_vertices):
    no1, no2 = aresta_menor_peso[0], aresta_menor_peso[1]
    conjuntos_vertices.append(str(no1 + no2))
    # if conjuntos_vertices == {}:
    #     conjuntos_vertices['1'] = []
    #     conjuntos_vertices['1'].append(no1)
    #     conjuntos_vertices['1'].append(no2)
    #
    # else:
    #     for key, conjunto_vertices in conjuntos_vertices.items():
    #         if no1 in conjunto_vertices or no2 in conjunto_vertices:
    #             conjuntos_vertices[key].append(no1)
    #             conjuntos_vertices[key].append(no2)

    return conjuntos_vertices

conjuntos_vertices = insert_arrow_into_vertices_sets(aresta_menor_peso, conjuntos_vertices)
print('CONJUNTOS VERTICES: ', conjuntos_vertices)

#TODO: adicionar aresta a arvore
arvore_geradora_minima[menor_peso] = aresta_menor_peso
print('ARVORE: ', arvore_geradora_minima)

# #TODO: pega os conjuntos adjacentes para posteriormente unificá-los
# def get_adjacency_sets_by_nodes(conjuntos_vertices, arvore_geradora_minima):
#     adjacencia = {}
#
#     for aresta in arvore_geradora_minima.values():
#         for key, conjunto_vertices in conjuntos_vertices.items():
#             for vertice in conjunto_vertices:
#                 if vertice in aresta:
#                     try:
#                         adjacencia[vertice].append(key)
#                     except:
#                         adjacencia[vertice] = [key]
#
#
#
#     return adjacencia
#
# adjacencia = get_adjacency_sets_by_nodes(conjuntos_vertices, arvore_geradora_minima)
# print('ADJACENCIA: ', adjacencia)
#
# #TODO: juntar os dois conjuntos em que o vertice faz adjacencia
# def join_sets_that_vertice_make_adjacency(adjacencia):
#     conjuntos_a_juntar = {}
#     for conjunto, nos in adjacencia.items():
#         for conjunto_temp, nos_temp in adjacencia.items():
#             for no in nos:
#                 if no in nos_temp:
#                     try:
#                         conjuntos_a_juntar[no].append(conjunto)
#                     except:
#                         conjuntos_a_juntar[no] = [conjunto]
#
#     aux = {}
#     for conjunto, nos in conjuntos_a_juntar.items():
#         for no in nos:
#             try:
#                 if not no in aux[conjunto]:
#                     aux[conjunto].append(no)
#             except:
#                 aux[conjunto] = [no]
#
#     conjuntos_a_juntar = aux
#
#     return conjuntos_a_juntar
#
# conjuntos_a_juntar = join_sets_that_vertice_make_adjacency(adjacencia)
# print('CONJUNTOS A JUNTAR: ', conjuntos_a_juntar)
#
# #TODO: juntar conjuntos adjacentes
# # def join_adjacent_sets(conjuntos_a_juntar):
# #     conjuntos_integrados = {}
# #     for no, conjunto in conjuntos_a_juntar.items():
# #         try:
# #             conjuntos_integrados[conjunto].append(no)
# #         except:
# #             conjuntos_integrados[conjunto] = [no]
# #
# #         print(no, conjunto)
# #
# #     return conjuntos_integrados
# #
# # conjuntos_vertices = join_adjacent_sets(conjuntos_a_juntar)
# # print('CONJUNTO VERTICES INTEGRADO: ', conjuntos_vertices)

#TODO: agrupar nos adjacentes
nos_adjacentes = join_adjacent_nodes(conjuntos_vertices)
print('NOS ADJACENTES: ', nos_adjacentes)