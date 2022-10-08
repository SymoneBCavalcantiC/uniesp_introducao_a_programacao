#Ler o ano atual e o ano de nascimento de uma pessoa.
#Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).


ano = (int(input("Digite o ano atual: ")))
ano_nasc = (int(input("Digite o ano em que você nasceu: ")))
idade = (ano - ano_nasc)

if idade < 16:
    print(f"Você ainda não poderá votar.")
elif idade >=16 and idade < 70:
    print(f"Você poderá votar! Verifique seu título eleitoral e vote consciente!")
else:
    print(f"Seu voto é facultativo: escolha se quer votar.")