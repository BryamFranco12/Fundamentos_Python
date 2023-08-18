# Par o Impar

numero = int(input("Ingrese el numero: "))

numerodef = numero % 2

if numerodef == 0:
    print("EL NUMERO INGRESADO", numero, "es Par")
else:
    print("EL NUMERO INGRESADO", numero, "es Impar")
