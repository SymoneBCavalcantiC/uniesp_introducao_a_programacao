# Ler o ano atual e o ano de nascimento de uma pessoa.
# Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

idade = (int(input("Digite o ano do seu nascimento: ")))
ano = 2022
voto = (ano - idade)

if voto <16:
    print(f"Você ainda não poderá votar este ano!")
elif voto >= 16 and voto < 70:
    print(f"Você poderá votar este ano! Verifique seu título e vote consciente.")
else:
    print(f"Seu voto é facultativo: escolha se quer votar esse ano!")
