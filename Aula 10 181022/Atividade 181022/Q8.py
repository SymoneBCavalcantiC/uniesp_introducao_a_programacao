# Faça um algoritmo para ler um vetor de 30 números. 
# Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

vetor = []

for v in range(30):
    vetor. append(randint(0,30))

print(vetor)

busca = (int(input("Qual número deseja buscar no vetor? ")))

if busca in vetor:
    print(vetor.count(busca))