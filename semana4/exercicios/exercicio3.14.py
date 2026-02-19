""" Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro
e último elementos da lista. Você pode considerar que a lista não estará vazia.  """


def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]


if __name__ == "__main__":
    ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
    trocaPU(ingredientes)
    print(ingredientes)

    numeros = [1, 2, 3, 4, 5]
    trocaPU(numeros)
    print(numeros)

    unico = [42]
    trocaPU(unico)
    print(unico)
