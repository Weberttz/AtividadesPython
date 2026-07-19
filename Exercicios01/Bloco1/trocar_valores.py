def main():
    a = float(input("Digite o número 1: "))
    b = float(input("Digite o número 2: "))

    a, b = b, a # trocar valores em uma linha

    print(f"O valor de A: {a}")
    print(f"O valor de B: {b}")

main()