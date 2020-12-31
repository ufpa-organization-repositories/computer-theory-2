def particao(xs, inicio, final):
    seguidor = lider = inicio
    while lider < final:
        if xs[lider] <= xs[final]:
            xs[seguidor], xs[lider] = xs[lider], xs[seguidor]
            seguidor += 1
        lider += 1
    xs[seguidor], xs[final] = xs[final], xs[seguidor]
    return seguidor


def _quicksort(xs, inicio, final):
    if inicio >= final:
        return
    p = particao(xs, inicio, final)
    _quicksort(xs, inicio, p - 1)
    _quicksort(xs, p + 1, final)


def quicksort(xs):
    _quicksort(xs, 0, len(xs) - 1)

xs = [5,4,3,2,1]
quicksort(xs)
print(xs)