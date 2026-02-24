""" Exercício 3.3

Traduza estas declarações em instruções if/else do Python:

Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'
Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'. """

ano = 2024
if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

bilhete = [1, 2, 3, 4, 5]
loteria = [1, 2, 3, 4, 5]
if bilhete == loteria:
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez...')
