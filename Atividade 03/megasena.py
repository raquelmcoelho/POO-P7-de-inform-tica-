"""Para ganhar o prêmio máximo na Mega Sena, é necessário
acertar todos os 6 números em seu bilhete com os 6 números entre 1 e 60
sorteados. Escreva um programa que gere uma seleção aleatória de 6 números para
uma aposta. Certifique-se de que os 6 números selecionados não contenham
duplicatas. Exibir os números em ordem crescente."""

import random
# criando lista de 1 a 60 com as opções
lista = list(range(1,61))
# embaralhando a lista
random.shuffle(lista)
# slicing só 6 números dessa lista embaralhada de opções
lista2 = lista[0:6:1]
# organizando em ordem crescente
lista2.sort()
print(lista2)