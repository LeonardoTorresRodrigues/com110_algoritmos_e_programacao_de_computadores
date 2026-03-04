"""
Implemantar uma função em Python que verifica se uma matriz bidimensional é simétrica ou não
"""


def simetrica(m):
    nlinhas = len(m)
    ncolunas = len(m[0])

    for i in range(nlinhas):
        for j in range(i+1, ncolunas):
            if m[i][j] != m[j][i]:
                return False
    return True


m = [[1, 2, 2], [2, 4, 5], [3, 5, 2]]
print(simetrica(m))
