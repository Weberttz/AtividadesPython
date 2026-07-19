def main():
    num = float(input("Digite o número 1: "))

    classificacao = ("par" if num % 2 == 0 else "ímpar")

    print(f"O número {num} é {classificacao}")

main()