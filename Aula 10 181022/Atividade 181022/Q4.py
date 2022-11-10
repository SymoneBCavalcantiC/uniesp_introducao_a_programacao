# Ler um vetor A de 10 números. 
# Após, ler mais um número e guardar em uma variável X. 
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. 
# Logo após, imprimir o vetor M.

from random import randint

vetor_a = []

for n in range(10):
    n = vetor_a.append(randint(0,100))

print(vetor_a)

x = randint(0,100)

print(x)

vetor_m = []

for c,v in enumerate(vetor_a):
    vetor_m.append(v * x)
    
print(vetor_m)
