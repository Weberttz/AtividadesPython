# https://www-geeksforgeeks-org.translate.goog/python/enumerate-in-python/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc&_x_tr_hist=true

def main():
    linguagens = ["Python", "C", "C++", "Java", "Prolog"]

    for k, v in enumerate(linguagens):
        print(k, v)

    tupla = list(enumerate(linguagens))

    print(f"Tupla = {tupla}\n")

    favoritas = {"Reflections": 10, "Do I Wanna Know?": 10, "505": 10}

    for i, (k, v) in enumerate(favoritas.items()):
        print(f"Id:{i} Nome: {k} Nota:{v}")

main()