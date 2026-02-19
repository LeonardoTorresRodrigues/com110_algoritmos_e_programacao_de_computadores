""" Escreva a função negatives(), que aceita uma lista como entrada 
e exibe, um por linha, os valores negativos na lista. """


def negatives(lst):
    for num in lst:
        if num < 0:
            print(num)


if __name__ == "__main__":
    negatives([4, 0, -1, -3, 6, -9])
    print("---")
    negatives([1, 2, 3])
    print("---")
    negatives([-5, -10, 0, 7])
