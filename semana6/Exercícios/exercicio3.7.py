""" 
Escreva um laço for que exiba a seguinte sequência de números, um por linha. 
Inteiros de 3 até 12, inclusive este.
Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).
Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.
"""

# 1. Inteiros de 3 até 12, inclusive
for i in range(3, 13):
    print(i)

# 2. De 0 até 9 (exclusive), passo 2 → 0, 2, 4, 6, 8
for i in range(0, 9, 2):
    print(i)

# 3. De 0 até 24 (exclusive), passo 3
for i in range(0, 24, 3):
    print(i)

# 4. De 3 até 12 (exclusive), passo 5 → 3, 8
for i in range(3, 12, 5):
    print(i)
