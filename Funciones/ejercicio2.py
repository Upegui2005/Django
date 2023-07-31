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


if __name__ == "__main__":
    print("Bienvedio a la tienda noseasapo")
    print("""
    Tenemos estos productos:
    1. Manzanas $500
    2. Papitas $2000
    3. Gaseosa 1.5 $5000
    4. Leche $2500
    5. Arepas $1900""")
