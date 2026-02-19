""" Implemente a função perimeter(), que aceita, como entrada, 
o raio de um círculo (um número não negativo) e retorna o perímetro do círculo. """

import math


def perimeter(radius):
    if radius < 0:
        raise ValueError("O raio deve ser um número não negativo.")
    return 2 * math.pi * radius


# Testes
if __name__ == "__main__":
    print(perimeter(1))
    print(perimeter(5))
    print(perimeter(0))
