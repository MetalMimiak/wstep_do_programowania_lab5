lista_liczb = [2, 5, 6, 2, 8, 3, 1, 9, 23, 67, 42, 23, 7]

def srednia_liczb(lista_liczb):
    srednia_liczb = sum(lista_liczb) / len(lista_liczb)
    return srednia_liczb

print(f"Średnia liczb: {srednia_liczb(lista_liczb)}")