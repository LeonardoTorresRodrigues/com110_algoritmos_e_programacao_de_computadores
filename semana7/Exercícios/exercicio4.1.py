"""
Comece executando a atribuição:

s = '0123456789'
Agora, escreva expressões (usando s e o operador de indexação) que sejam avaliadas como:

'234'
'78'
'1234567'
'0123'
'789'
"""

s = '0123456789'

# 1. '234'
print(s[2:5])

# 2. '78'
print(s[7:9])

# 3. '1234567'
print(s[1:8])

# 4. '0123'
print(s[0:4])   # ou s[:4]

# 5. '789'
print(s[7:])    # ou s[7:10]
