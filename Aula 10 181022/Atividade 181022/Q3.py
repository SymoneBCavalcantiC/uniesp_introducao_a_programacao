# Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

from random import randint

RAND_MIN = 1
RAND_MAX = 100

vetor = []

n = 0
while n < 20:
    numero = randint(RAND_MIN, RAND_MAX)
    vetor.append(numero)
    n += 1

menor = vetor[0]
maior = vetor[0]

for i in vetor:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

print(f"Lista: {vetor}")
print(f"Menor número {menor} posicionado em: {vetor.index(menor)} e Maior número {maior} posicionado em: {vetor.index(maior)}")