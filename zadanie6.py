def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Długości boków trójkąta muszą być większe od zera")
        return

    if a + b <= c or b + c <= a or a + c <= b:
        print("Z podanych boków nie da się ułożyć trójkąta")
        return

    try:
        #połowa obwodu trójkąta
        s = (a + b + c) / 2
        pole = (s * (s-a) * (s-b) * (s-c)) ** 0.5
        print(f"Pole trójkąta wynosi: {pole}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

pole_trojkata(a, b, c)