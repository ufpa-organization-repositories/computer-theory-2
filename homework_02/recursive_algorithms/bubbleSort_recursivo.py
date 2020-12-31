# usar recursividade
# ordenar do maior pro menor

lista = [3,1,2,4,10,9,8,15,8,9,3]

def bubbleSort(lista):
    n_elementos = len(lista)
    if n_elementos >1:
        for index, elem in enumerate(lista):
            if not index == n_elementos - 1:
                if lista[index] > lista[index + 1]:
                    aux = lista[index]
                    lista[index] = lista[index + 1]
                    lista[index + 1] = aux
                    bubbleSort(lista)
    else:
        print('lista pequena')

    return 0

bubbleSort(lista)
print(lista)
