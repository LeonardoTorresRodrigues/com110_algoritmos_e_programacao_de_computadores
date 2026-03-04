# Imprimir as vogais dos nomes de uma lista

str_list = ['João', 'Roberto', 'Rafael']

for nome in str_list:
    for c in nome:
        if c in 'aeiou':
            print(c)
