def potega_liczby(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * potega_liczby(a, n - 1)
    else:
        return 1 / a * potega_liczby(a, -n)

a = float(input("Podaj liczbę a: "))
n = int(input("Podaj stopień potęgi, do którego chcesz podnieść liczbę a: "))

print(f"Liczba {a} podniesiona do potęgi {n} wynosi: {potega_liczby(a, n)}")