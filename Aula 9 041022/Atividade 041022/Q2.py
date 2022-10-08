# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus números favoritos.
# Use seus nomes para serem as chaves de cada número favorito. 
# Ao final, exiba o nome de cada pessoa e seu número favorito.

nprefer = {"Josi": 11, "Leide": 12, "Eduardo": 13, "Flavio": 25, "Monica": 26}

for k,v in nprefer.items():
    print(f'O número preferido de {k} é {v}.')