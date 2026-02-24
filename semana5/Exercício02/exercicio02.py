t = eval(input('Digite a temperatura: '))


def temperatura(t):
    if t >= 86:
        print('Quente!')
    elif t < 86 and t >= 32:
        print('Frio!')
    else:
        print('Congelando!')


temperatura(t)
