# EMPRESA DE TEXTILES

nombre = input("Ingrese su nombre: ")
departamento = int(input("A que departamento perteneces\n[1001]Atencion al cliente\n[1002]Logistica"
                         "\n[1003]Gerencia\n: "))
antiguedad = int(input("Hace cuantos año[s] presta servicio en la empresa: "))

if departamento == 1001:  # DEPARTAMENTO DE ATENCION AL CLIENTE
    if antiguedad == 1:
        print("El trabajador {} del departamento de atencion al cliente cuenta con una antiguedad de {} "
              "año en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (6) Dias de vacaciones")

    elif 2 <= antiguedad <= 6:
        print("El trabajador {} del departamento de atencion al cliente cuenta con una antiguedad de {} "
              "años en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (14) Dias de vacaciones")

    elif antiguedad >= 7:
        print("El trabajador {} del departamento de atencion al cliente cuenta con una antiguedad de {} "
              "años en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (20) Dias de vacaciones")

elif departamento == 1002:  # DEPARTAMENTO DE LOGISTICA
    if antiguedad == 1:
        print("El trabajador {} del departamento de logistica cuenta con una antiguedad de {} "
              "año en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (7) Dias de vacaciones")

    elif 2 <= antiguedad <= 6:
        print("El trabajador {} del departamento de logistica cuenta con una antiguedad de {} "
              "años en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (15) Dias de vacaciones")

    elif antiguedad >= 7:
        print("El trabajador {} del departamento de logistica cuenta con una antiguedad de {} "
              "años en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (22) Dias de vacaciones")

elif departamento == 1003:  # DEPARTAMENTO DE GERENCIA
    if antiguedad == 1:
        print("El trabajador {} del departamento de gerencia cuenta con una antiguedad de {} "
              "año en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (10) Dias de vacaciones")

    elif 2 <= antiguedad <= 6:
        print("El trabajador {} del departamento de gerencia cuenta con una antiguedad de {} "
              "años en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (20) Dias de vacaciones")

    elif antiguedad >= 7:
        print("El trabajador {} del departamento de gerencia cuenta con una antiguedad de {} "
              "años en la empresa".format(nombre, antiguedad))
        print("\nTiene Derecho a (30) Dias de vacaciones")
