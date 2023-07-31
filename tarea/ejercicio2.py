"""
Simular una tienda, Definir 5 productos con su precio.
Ofrecer al usuario lo que desea comprar.
El usuario puede comprar hasta 3 veces.
Preguntar al usuario la contidad de ese producto que quiere comprar.

Si las unidades a comprar son =>20, aplicar un descuento del 50%, USANDO FUNCION
Si las unidades a comprar son =>10 <20, aplicar un descuento del 30%, USANDO FUNCION ó la misma de arriba
Si las unidades a comprar son >=1 <10, no aplicar descuento.
Calcular subtotal y total final
"""


def total_desc50(cantidad, valor):
    resultado = (cantidad * valor) / 2
    return resultado


def total_desc30(cantidad, valor):
    resultado = (cantidad * valor) * 0.3
    return resultado


def total(cantidad, valor):
    resultado = cantidad * valor
    return resultado


productos = []
subtotal = 0
totales = 0
cantidades = 0

if __name__ == "__main__":
    print("Bienvedio a la tienda noseasapo")
    print("""
    Tenemos estos productos:
    1. Manzanas $500
    2. Papitas $2000
    3. Gaseosa 1.5 $5000
    4. Leche $2500
    5. Arepas $1900""")

    pregunta = int(input("¿Cuantas veces piensas comprar? (Maximo 3): "))
    while pregunta >= 4:
        print("Dije que maximo 3, aprenda a leer")
        pregunta = int(input("¿Cuantas veces piensas comprar? (Maximo 3): "))
    else:
        for i in range(pregunta):
            productos.append(input("¿Que productos quieres comprar?: "))
            cantidad = int(input("¿Cuanta cantidad quieres comprar?: "))
            cantidades += cantidad
            valor = int(input("¿Valor del producto?: "))
            subtotal += valor * cantidad
            if cantidad < 10:
                totales += total(cantidad, valor)
            elif 10 <= cantidad < 20:
                totales += total_desc30(cantidad, valor)
            else:
                totales += total_desc50(cantidad, valor)
    print(f"Los productos fueron: {productos}\nEl subtotal fue: {subtotal} \nEl total fue: {totales}")
    print("Gracias por su compra")
 