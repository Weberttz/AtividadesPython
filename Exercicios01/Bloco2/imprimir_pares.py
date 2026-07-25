def main():
    numeros = [1, 0, 9, 11, 97, 22, 43, 10, 97, 110]
    pares = [n for n in numeros if n % 2 == 0] # recolhe todo número par da lista de números

    print(pares)

main()