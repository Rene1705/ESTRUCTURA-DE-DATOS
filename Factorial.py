def factorial(n):

    if n == 1:
        return 1
    else:

       resultado = factorial(n - 1)
       solution = resultado * n

        return solution
try:
     num = int(input("Ingrese el número para calcular el factorial: "))
     print("El factorial de", num, "es", factorial(num))
except ValueError:
    print("Error: El número ingresado no es un número entero valido")
