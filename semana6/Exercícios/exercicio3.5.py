""" Implemente um programa que solicite do usuário uma lista de palavras 
(ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de quatro letras
nessa lista. """

l = []
palavra = input('Digite uma palavra: ')
while palavra != '':
    l.append(palavra)
    palavra = input('Digite uma palavra: ')


for palavra in l:
    if len(palavra) == 4:
        print(palavra)
