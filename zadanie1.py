def kwadrat_liczby(liczba):
    liczba = liczba ** 2
    return liczba

liczba = float(input("Podaj liczbę: "))

print(f"Kwadrat podanej liczby: {kwadrat_liczby(liczba):.0f}")