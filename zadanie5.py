def bmi(waga, wzrost):
    bmi = waga / wzrost ** 2
    bmi_zaokr = round(bmi, 2)

    if bmi < 18.5:
        zakres_bmi = "niedowaga"
    elif bmi < 25:
        zakres_bmi = "pożądana masa ciała"
    elif bmi < 30:
        zakres_bmi = "nadwaga"
    elif bmi < 35:
        zakres_bmi = "otyłość I stopnia"
    elif bmi < 40:
        zakres_bmi = "otyłość II stopnia"
    else:
        zakres_bmi = "otyłość III stopnia"

    print(f"Twoje BMI: {bmi_zaokr}")
    print(f"Zakres: {zakres_bmi}")

    return bmi_zaokr, zakres_bmi


wzrost = float(input("Podaj wzrost [w metrach]: "))
waga = float(input("Podaj wagę [w kilogramach]: "))

bmi(waga, wzrost)