n1 = eval(input('Digite a primeira nota: '))
n2 = eval(input('Digite a segunda nota: '))

media = 0.4 * n1 + 0.6 * n2

if media >= 5.0:
    print('Parabéns, você foi aprovado! Sua média foi:', media)
else:
    print('Desculpe, você foi reprovado! Sua média foi:', media)
