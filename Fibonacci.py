def rana(n):
    if n == 0:
        return 0:
    elif n == 1:
        return 1
    else:
        return rana(n-1) + rana(-2)

def main():
    try:
       n = int(input("Ingrese un número para calcular el enésimo número de Fibonacci: "))
       if n < 0:
           print("Por favor, ingreseun número entero no negativo.")
       else:
           print(f"El enésimo número de Fibonacci para n={n} es {rana(n)}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
