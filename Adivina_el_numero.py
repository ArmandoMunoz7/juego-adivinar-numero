import random as rd

numero = rd.randint(1, 100)
contador = 0

print("======= ADIVINA EL NUMERO SECRETO =======")

while True:
    try:
        intento = int(input("\nESCRIBE UN NUMERO ENTRE 1 Y 100: "))
        if intento <= 0:
            print("\nINGRESA UN NUMERO MAYOR A 0.")
            continue
        contador = contador +1
        if intento > numero:
            print("DEMASIADO ALTO, INTENTA DE NUEVO")
            continue
        elif intento < numero:
            print("DEMASIADO BAJO, INTENTA DE NUEVO")
            continue
        else:
            print(f"\nFELICIDADES ACERTASTE EL NUMERO SECRETO EN {contador} INTENTOS")
        break
    except ValueError:
        print("\nINGRESA UN NUMERO VALIDO")