def main():
    nomes = ["Jonh", "Mario", "Yasmin", "Selena"]
    notas = ["5.0", "7.2", "10.0", "4.5"]

    print("Nome\tNota")
    for nome, nota in zip(nomes, notas):
        print(f"{nome}\t{nota}")

main()