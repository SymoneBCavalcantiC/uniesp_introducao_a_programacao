# Faça um algoritmo para ler um vetor de 20 números. 
# Após isto, deverá ser lido mais um número qualquer e verificar se esse número existe no vetor ou não. 
# Se existir, o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).

from random import randint

lista = []

for l in range(20):
    lista.append(randint(0,100))

print(lista)

busca = (int(input("Digite o número para buscar na lista: ")))

if busca in lista:
    b = lista.index(busca)
    del lista[b]
print(lista)
