# while
abacate = 1

while abacate <= 10:
    print(abacate)
    abacate +=1

# Exemplo de For
for abacaxi in range(1, 11, 1):
    print(abacaxi)

controle = True

while controle:
    print("Digite 0 para sair")
    print("Digite outro número para rodar")
    num = int(input("Digite o número escolhido:"))

    if num == 0:
        controle = False
    elif num > 10:
        print(f'{num} é maior que 10')
    elif num < 10 and num != 0:
        print(f'{num} é menor que 10')
    