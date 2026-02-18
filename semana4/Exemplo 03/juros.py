def juros(preco, juros):
    res = preco * (1+(juros / 100))
    return res


preco = int(input('Qual o valor preço: '))
taxaDeJuros = int(input('Qual o valor da taxa de juros: '))

print(juros(preco, taxaDeJuros))
