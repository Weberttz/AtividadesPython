def encontrar_min_e_max(lista):
    menor = lista[0]
    maior = 0
    for numero in lista:
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero

    return (menor, maior)


def main():
    tupla1 = (1, 2, 10, 0, 100, 1011, 8, 9)
    print(f"Tipo de tupla1: {type(tupla1)}")

    tupla2 = encontrar_min_e_max(tupla1)
    print(f"Tipo de 'tupla2': {type(tupla2)}")

    print(f"tupla2 = {tupla2}")

main()