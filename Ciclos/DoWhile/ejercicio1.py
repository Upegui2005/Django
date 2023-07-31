# Preguntar a el usuario numeros hasta que diga salir
# Mustra la sumatoria de ellos

suma = 0
while True:
    num = input("Digite un un numero o la palabra salir para finalizar:").lower()
    if num == "salir":
        print("Saliste")
        break
    else:
        suma = suma + int(num)
print(f"La suma de todos es: {suma}")
