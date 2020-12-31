def particao(array, baixo, alto):
    i = (baixo - 1)  # index of smaller element
    pivor = array[alto]  # pivor

    for j in range(baixo, alto):

        if array[j] <= pivor:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[alto] = array[alto], array[i + 1]
    return (i + 1)

def quickSort(array, baixo, alto):
    if baixo < alto:
        pi = particao(array, baixo, alto)
        quickSort(array, baixo, pi - 1)
        quickSort(array, pi + 1, alto)


array = [8, 2, 15, 9, 7, 11]
n = len(array)
quickSort(array, 0, n - 1)
for i in range(n):
    print ("%d" % array[i]),