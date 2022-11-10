# Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. 
# Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. 
# Escrever a média da turma e o resultado da contagem.

notas = []

for nota in range(20):
    notas.append(int(input(f"Digite a nota do aluno: ")))

qtd_lista = len(notas)

soma = 0
for nota in notas:
    soma = soma + nota

media = soma / qtd_lista

qtd_alunos_media = 0
for nota_aluno in notas:
    if nota_aluno > media:
        qtd_alunos_media += 1

print(f"Média da turma: {media} com {qtd_alunos_media} alunos acima da média")
