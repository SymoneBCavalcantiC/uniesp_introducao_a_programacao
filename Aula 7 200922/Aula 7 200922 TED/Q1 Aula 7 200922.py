#As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia; e R$ 1,00 se forem compradas ao menos 12. 
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.


num = (int(input("Digite o número de maçãs que deseja comprar: ")))

if 0 < num < 12:
    valor = num * 1.30
    print(f"O custo total pela compra de {num} maçãs é: R$ {valor}")
elif num >= 12 :
    valor = num * 1
    print(f"O custo total pela compra de {num} maçãs é: R$ {valor}")

