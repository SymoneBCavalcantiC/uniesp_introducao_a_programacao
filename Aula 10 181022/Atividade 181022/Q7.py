# Faça um algoritmo para ler dois vetores V1 e V2 de 10 números cada. 
# Calcular e escrever a quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.

from random import randint

v1 = []
v2 = []

for v in range(10):
    v1.append(randint(0,10))
    v2.append(randint(0,10))

print(v1)
print(v2)

for n in range(len(v1)):
    if v1[n] == v2[n]:
        print(f"Os itens {v1[n]} e {v2[n]}, na posição {n} são iguais nas duas listas.")

