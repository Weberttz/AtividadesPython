def main():
    lista_alunos = {
       1: {"nome": "Webert", "nota":10},
       2: {"nome": "Maria", "nota":7.1},
       3: {"nome": "Bruno", "nota":2.2},
       4: {"nome": "Felipe", "nota":5},
       5: {"nome": "Carol", "nota":10},
       6: {"nome": "Marcos", "nota":6.75}
    }

    media = 7.00

    for id, pessoa in lista_alunos.items():
        if pessoa["nota"] > media:
            print(f"Nome: {pessoa["nome"]} nota: {pessoa["nota"]}")

main()