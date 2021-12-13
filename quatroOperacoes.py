#Crie um algoritmo em Python, que dado dois números informados pelo usuário e
#sua operação (das 4 operações básicas da matemática), realize os cálculos
#adequados dentro de funções.

print("-------------------Início da execução-------------------")
numero1 = float(input("Qual o primeiro número? "))
numero2 = float(input("Qual o segundo número? "))
operacao = input("Qual a operacao desejada? (Insira '+' para somar, '-' para subtrair, '*' para multiplicar e '/' para dividir!) ")
def digaQualAOperacao(operacao):
    if operacao == "+":
        return "Você escolheu somar!"
    elif operacao == "-":
        return "Você escolheu subtrair!"
    elif operacao == "*":
        return "Voce escolheu multiplicar!"
    elif operacao == "/":
        return "Você escolheu dividir!"
def quatroOperacoes (numero1, numero2):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        return numero1 / numero2

print(digaQualAOperacao(operacao))
print("O resultado da sua operação é: ", quatroOperacoes(numero1,numero2))
print("-------------------Final da execução-------------------")