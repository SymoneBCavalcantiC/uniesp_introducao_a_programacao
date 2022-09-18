# Seja criativo ao desenvolver esse programa: 
# a) Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
# b) Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
# c) Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você poderá enviar novos convites. Imprima o nome dessas pessoas que não poderão comparecer.
# d) Modifique sua lista, substitua os desistentes por novos convidados.
# e) Exiba um novo convite para cada pessoa que continua presente na lista.


lista_convid = ["Maria Bethania", "Caetano Veloso", "Ivete Sangalo", "Djavan", "Lenine"]

for nome in lista_convid:
    print(f"Querido(a), {nome}! Dê-me a honra da sua presença comparecendo a um jantar em minha casa! Será no domingo, dia 25, a partir das 21h. Conto com sua presença!")


# Ivete Sangalo e Djavan não poderão comparecer ao jantar.


lista_convid_atual = ["Maria Bethania", "Caetano Veloso", "Lenine", "Regina Casé", "Pedro Bial"]
for nome in lista_convid_atual:
        print(f"Querido(a), {nome}! Dê-me a honra da sua presença comparecendo a um jantar em minha casa! Será no domingo, dia 25, a partir das 21h. Conto com sua presença!")

