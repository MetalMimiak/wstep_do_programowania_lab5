def parametry(*args):
    #A.
    print("Wartości parametrów:")
    for parametr in args:
        print(parametr)

    #B.
    liczby = [x for x in args if isinstance(x, (int, float))]
    if len(liczby) == 0:
        return None #brak podanych argumentów, brak max wartości
    max = liczby[0]
    for x in liczby[1:]:
        if x > max:
            max = x
    print(f"Maksymalna wartość wynosi: {max}")

parametry("tekst", 54, True, 82.6, 12)