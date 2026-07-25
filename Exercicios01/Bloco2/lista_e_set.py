# https://www-w3schools-com.translate.goog/python/python_sets_add.asp?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc

def main():
    lista_frutas = ["maça", "banana", "abacaxi", "mamão", "banana", "abacaxi", "morango"]
    set_frutas = set() # criar set vazio

    set_frutas.update(lista_frutas) # adiciona lista ao set

    print(f"Tamanho da lista: {len(lista_frutas)}")
    print(f"Lista = {lista_frutas}")
    print(f"Tamanho do set: {len(set_frutas)}")
    print(f"Set = {set_frutas}")

main()