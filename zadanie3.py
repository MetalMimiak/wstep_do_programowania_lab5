def powitanie(imie="Użytkowniku", jezyk="polski"):
    if jezyk.lower() == "polski":
        print(f"Cześć, {imie}")
    elif jezyk.lower() == "angielski":
        print(f"Hello, {imie}")
    elif jezyk.lower() == "niemiecki":
        print(f"Guten Morgen, {imie}")
    else:
        print(f"Witaj, {imie}")

imie = str(input("Podaj imię: "))
jezyk = str(input("Podaj język: "))

powitanie(imie, jezyk)

powitanie()