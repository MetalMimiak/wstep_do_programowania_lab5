def wyraz_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return wyraz_fibonacci(n - 1) + wyraz_fibonacci(n - 2)
    
n = int(input("Podaj wartość n: "))

if n < 0:
    print("n nie może być liczbą ujemną")
else:
    print(f"Dla n = {n}, {n}-ty wyraz ciągu fibonacciego wynosi: {wyraz_fibonacci(n)}")