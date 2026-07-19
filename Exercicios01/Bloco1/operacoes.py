def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def calcular_divisao_real(num1, num2):
    if num2 == 0: return 0
    return num1 / num2

def calcular_divisao_inteira(num1, num2):
    if num2 == 0: return 0
    return num1 // num2

def calcular_resto_divisao(num1, num2):
    if num2 == 0: return 0
    return num1 % num2

def main():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))

    print(f"Soma: {somar(num1, num2)}")
    print(f"Subtração: {subtrair(num1, num2)}")
    print(f"Multiplicação: {multiplicar(num1, num2)}")
    print(f"Divisão Real: {calcular_divisao_real(num1, num2)}")
    print(f"Divisão Inteira: {calcular_divisao_inteira(num1, num2)}")
    print(f"Resto de Divisão: {calcular_resto_divisao(num1, num2)}")

main()