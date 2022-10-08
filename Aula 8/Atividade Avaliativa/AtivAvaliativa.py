#ATIVIDADE AVALIATIVA - Questão 1:
#[FORBELLONE, 2022] Construa um algoritmo para calcular
#as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo
#que os valores A, B, C são fornecidos pelo usuário.
#(considere que a equação possui duas raizes reais).

import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")



# ATIVIDADE AVALIATIVA - Questão 2:
#[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, 
#P(x1, y1) e Q(x2, y2), imprima a distância entre eles.

import math

xp = float(input("Digite a coordenada X de P: "))
yp = float(input("Digite a coordenada Y de P: "))
xq = float(input("Digite a coordenada X de Q: "))
yq = float(input("Digite a coordenada Y de Q: "))

distancia = math.sqrt(((xp - yp) ** 2) + ((xq - yq) ** 2))
print(f"A distancia entre os pontos P e Q fornecidos é: {distancia}")


#ATIVIDADE AVALIATIVA: Questão 3
#Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; 
# calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.
# SÍMBOLO  OPERAÇÃO
#    +     Adição
#    -     Subtração
#    *     Multiplicação
#    /     Divisão



oper = int(input("Digite a operação desejada: 1, para ADIÇÃO; ou 2 para SUBTRAÇÃO; ou 3 para MULTIPLICAÇÃO; ou 4 para DIVISÃO: "))
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))


if oper == 1:
        soma = n1 + n2
        print(f"A adição dos dois números é: {soma}")
    
elif oper == 2:
        subtr = n1 - n2
        print(f"A subtração dos dois números é: {subtr}")
    
elif oper == 3:
        mult = n1 * n2
        print(f"A multiplicação dos dois números é: {mult}")
    
elif oper == 4:
        divis = n1 / n2
        print(f"A divisão dos dois números é: {divis}")

else:
    print(f"Digite um número válido: 1 para Adição, ou 2 para Subtração, ou 3 para multiplicação, ou 4 para divisão.")



# ATIVIDADE AVALIATIVA: Questão 4
# O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a 
# condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². 
# Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.
# IMC em adultos        CONDIÇÃO
# Abaixo de 18,5        Abaixo do peso
# Entre 18,5 e 25       Peso normal
# Entre 25 e 30         Acima do peso
# acima de 30           Obeso


peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura (para decimais, use ponto e não vírgula): "))
imc = (peso / (alt**2))

if imc < 18.5 and imc >0:
    print(f"Seu IMC é: {imc}: Sua condição é: ABAIXO DO PESO. ")

elif imc >= 18.5 and imc <25:
    print(f"Seu IMC é: {imc}: Sua condição é: PESO NORMAL. ")

elif imc >=25 and imc <30:
    print(f"Seu IMC é: {imc}: Sua condição é: ACIMA DO PESO. ")

elif imc >= 30:
    print(f"Seu IMC é: {imc}: Sua condição é: OBESO. ")

else:
    print(f"Digite números de peso e/ou altura válidos.")



# ATIVIDADE AVALIATIVA: Questão 5
# Escrever um algoritmo que leia uma quantidade desconhecida de números e 
# conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deve terminar quando for lido um número negativo.

x = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0

while x >= 0:
    x = int(input("Digite um número: "))
    if x >=0 and x < 25:
        i1 = i1 + 1
    elif x >= 26 and x < 50:
        i2 = i2 + 1
    elif x >= 51 and x < 75:
        i3 = i3 + 1
    elif x >= 76 and x <= 100:
        i4 = i4 + 1
print(f"O Intervalo de [0-25] tem {i1} números")
print(f"O Intervalo de [26-50] tem {i2} números")
print(f"O Intervalo de [51-75] tem {i3} números")
print(f"O Intervalo de [76-100] tem {i4} números5")



# ATIVIDADE AVALIATIVA: Questão 6
#Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

num = int(input("Digite um número: "))
c = num
f = 1
print(f"{num}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(f" x " if c > 1 else " = ", end="")
    f = f * c
    c -= 1
print(f"{f}")

