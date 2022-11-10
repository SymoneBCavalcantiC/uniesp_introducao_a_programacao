# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, 
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

clubes = []

for clube in range(10):
    clubes.append(str(input(f"Digite o nome do clube: ")))

busca = (str(input("Digite o nome do clube que deseja buscar: ")))

if busca in clubes:
    print(f"ACHEI! {busca} está na lista de clubes!")
else:
    print(f"NÃO ACHEI! {busca} não está na lista de clubes!")