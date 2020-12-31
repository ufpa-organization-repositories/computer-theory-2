def bubblesort(lista):
    tamanho_lista = len(lista) - 1

    for i in range(tamanho_lista):

        for j in range(tamanho_lista - i):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

lista = [2, 1, 5, 4, 3]
print(bubblesort(lista))
