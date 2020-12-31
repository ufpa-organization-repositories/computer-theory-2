import random

def create_graph(arestas):
    grafo = {}
    for aresta in arestas:
        grafo[aresta[0]] = aresta[1]
    return grafo

def choose_pivot(nos):
    i = random.randrange(0, len(nos))
    pivo = nos[i]
    return pivo

def add_edge_to_processed(nos_processados):
    menores_arestas = []

    menor_peso = None
    menor_aresta = None

    for no in nos_processados:
        for aresta in arestas:
            novo_no = ''
            if aresta[0][0] == no:
                novo_no = aresta[0][1]
            else:
                novo_no = aresta[0][0]

            if not novo_no in nos_processados and not novo_no == '':
                if no in aresta[0]:

                    # if menor_peso == None:
                    #     menor_peso = aresta[1]
                    #     menores_arestas.append(aresta[0])
                    #
                    # elif aresta[1] < menor_peso:
                    #     menores_arestas.append(aresta[0])
                    #     menor_peso = aresta[1]

                    if menor_peso == None:
                        menor_peso = aresta[1]
                        menor_aresta = aresta[0]

                    elif aresta[1] < menor_peso:
                        menor_peso = aresta[1]

                    #     menor_aresta = aresta[0]
    # i = random.randrange(0, len(menores_arestas))
    # menor_aresta = menores_arestas[i]

    return menor_aresta, menor_peso

def add_nodes_to_processed(menor_aresta, nos_processados):
    no1, no2 = menor_aresta[0], menor_aresta[1]

    if not no1 in nos_processados:
        nos_processados.append(no1)

    if not no2 in nos_processados:
        nos_processados.append(no2)

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

grafo = create_graph(arestas=arestas)
print('GRAFO: ', grafo)

# pivo = choose_pivot(nos)
pivo = 'D'
print('\npivo: {}'.format(pivo))

nos_processados = [pivo]
arestas_processadas = {}

end = check_if_all_nodes_are_processed(nos_processados=nos_processados, nos=nos)
contador = 1

while not end:
    print('\nITERAÇÂO: ', contador)
    menor_aresta, menor_peso = add_edge_to_processed(nos_processados=nos_processados)
    arestas_processadas[menor_aresta] = menor_peso
    print('ARESTA DE MENOR PESO SELECIONADA: ', menor_peso, menor_aresta)
    print('ARESTAS PROCESSADAS: ', arestas_processadas)

    add_nodes_to_processed(menor_aresta=menor_aresta, nos_processados=nos_processados)
    print('NÓS PROCESADOS: ', nos_processados)

    end = check_if_all_nodes_are_processed(nos_processados=nos_processados, nos=nos)
    print('end: ', end)
    contador += 1