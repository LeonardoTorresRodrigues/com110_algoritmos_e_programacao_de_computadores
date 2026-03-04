"""
Supondo que a variável previsão tenha recebido a string

'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:

A variável cont, a quantidade de ocorrências da string 'day' na string previsão.
A variável clima, o índice em que a substring 'sunny' começa.
A variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny' é substituída por 'cloudy'.
"""

previsao = 'It will be a sunny day today'

# 1. Contar ocorrências de 'day'
cont = previsao.count('day')
print(cont)  # 2

# 2. Índice onde 'sunny' começa
clima = previsao.index('sunny')
print(clima)  # 13

# 3. Substituir 'sunny' por 'cloudy'
troca = previsao.replace('sunny', 'cloudy')
print(troca)  # 'It will be a cloudy day today'
