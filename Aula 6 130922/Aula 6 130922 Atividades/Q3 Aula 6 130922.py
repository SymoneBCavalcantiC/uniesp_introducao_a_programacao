# Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada pessoa acessando cada elemento da lista um de cada vez.

lista_amigos = ['Analicia', 'Talita', 'Joana', 'Isabelly', 'Danilo']

for nome in lista_amigos:
    print(f'{nome}, obrigada por vir a aula!')


print(len(lista_amigos))

x = 0
while x < len(lista_amigos):
    print(f'{lista_amigos[x]}, obrigado por vir a aula!')
    x +=1