"""
def suma(a, b):
    resultado = a + b
    return resultado


print(suma(5, 5))
"""


# 1 forma
def saludo():
    # Doc string
    """ Esta funcion sirve para saludar a los aprendices """
    print("Hola aprendices")
    # return None


saludo()
saludo()
saludo()

# 2 forma, usando argumentos, sin retornos

name = input("¿Como te llamas?: ")


def saludo_especial(nombre):
    """ Esta funcion sirve para saludar a una persona especifica """
    print(f"Hola {nombre}")


saludo_especial(name)
saludo_especial("Pepito")
saludo_especial(2)
saludo_especial(True)
saludo_especial(input("¿Como te llamas?: "))


# 3 forma, uso de retorno (return)

def pesos_dolares(pesos, trm):
    resultado = pesos / trm
    return resultado


def dolares_pesos(dolares, trm):
    resultado = dolares * trm
    return resultado


if __name__ == "__main__":
    while True:
        opc = int(input("""
        Que desea hacer? 
        1. Convertir de pesos a dolares
        2. Convertir de dolares a pesos
        3. Salir
        """))
        if opc == 1:
            pesos = int(input("¿Cuantos pesos tienes?: "))
            trm = int(input("¿A cuanto esta la tasa representativa del mercado?: "))
            pesos_dolares(pesos, trm)
            print(f"Resultado: ${pesos_dolares(pesos, trm):.2f}")
        elif opc == 2:
            dolares = int(input("¿Cuantos dolares tiene?: "))
            trm = int(input("¿A cuanto esta la tasa representativa del mercado?: "))
            dolares_pesos(dolares, trm)
            print(f"Resultado: ${dolares_pesos(dolares, trm)}")
        elif opc == 3:
            print("Saliste")
            break
        else:
            print("Opcion invalida... intente de nuevo")
