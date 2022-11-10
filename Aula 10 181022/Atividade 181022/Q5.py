# Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B. 
# Exemplo: A[0] + B[0] deverá ser salva em N[0].

from random import randint

vetor_a = []
vetor_b = []
vetor_n = []

for i in range(10):
    a = vetor_a.append(randint(0,10))
    b = vetor_b.append(randint(0,10))

print(vetor_a)
print(vetor_b)

for c,v in enumerate(vetor_a):
    vetor_n.append(v + (vetor_b[c]))

print(vetor_n)