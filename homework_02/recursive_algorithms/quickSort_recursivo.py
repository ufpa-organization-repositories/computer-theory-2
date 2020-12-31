# quickSort recursivo
from random import randrange

def particiona(lista):
    print(lista)
    pivo = lista[-1]
    i = 0
    j = len(lista) - 2
    sub_lista_esquerda = []
    sub_lista_direita = []

    while not i == j:
        while lista[i] < pivo:
            i += 1
            if i == j: break
        while lista[j] > pivo:
            j -= 1

        lista[i], lista[j] = lista[j], lista[i]
        print(i, j)
        i += 1
        if i == j: break
        j -= 1

    for elem in lista[:i]:
        sub_lista_esquerda.append(elem)
    for elem in lista[j:len(lista) - 1]:
        sub_lista_direita.append(elem)

    print(i, j)
    print(sub_lista_esquerda, sub_lista_direita)
    lista = []
    for elem in sub_lista_esquerda: lista.append(elem)
    lista.append(pivo)
    for elem in sub_lista_direita: lista.append(elem)
    print(lista)
    return sub_lista_esquerda, sub_lista_direita

# particiona(lista)

def quickSort(lista):
    left, right = particiona(lista)
    quickSort(lista=left)
    quickSort(lista=right)




sub_lista_esquerda = []
sub_lista_direita = []
lista = [3,6,2,5,9,10,8,1,4,7]
n = len(lista)

quickSort(lista)
# print(lista)

