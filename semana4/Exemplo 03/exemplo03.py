def f(x):
    'Exemplo de documentação de funções que será impressa por meio da função help()'
    res = x ** 2 + 1  # calcula x ao quadrado + 1
    return res       # retorna o resultado


x = int(input('Passe o valor de x: '))
print(f(x))
