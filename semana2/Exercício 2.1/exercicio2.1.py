# A soma dos primeiros inteiros positivos
soma = sum(range(1, 6))
print(f"A soma dos 5 primeiros inteiros positivos é: {soma}")

# A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
idades = [('Sara', 23), ('Mark', 19), ('Fátima', 31)]
valores_idades = [pessoa[1] for pessoa in idades]
media = sum(valores_idades) / len(valores_idades)
print(f"A média das idades é: {media:.2f}")

# O número de veze que 73 cabe em 403
vezes_cabe = 403 // 73
print(f"73 cabe {vezes_cabe} vezes em 403.")

# O resto de quando 403 é dividido por 73
resto = 403 % 73
print(f"O resto da divisão de 403 por 73 é: {resto}")

# 2 à 10ª potência
potencia = 2 ** 10
print(f"2 elevado a 10 é {potencia}")

# Valor absoluto da distância entre alturas
altura_sara = 54
altura_mark = 57
distancia = abs(altura_sara - altura_mark)
print(f"O valor absoluto da distância é {distancia} polegadas")

# O menor preço entre os valores
precos = [34.99, 29.95, 31.50]
menor_preco = min(precos)
print(f"O menor preço é R$ {menor_preco}")
