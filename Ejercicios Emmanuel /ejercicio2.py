#Pedir tres productos ( nombre y precio), calcular el promedio de ellos
#Mostrar todos los nombres, precio y promedio
#Saludar

nombre = input("Escribe tu nombre: ")
np1 = input("Digite el nombre del primer producto: ")
pp1 = int(input("Digite el precio del primer producto: "))
np2 = input("Digite el nombre del segundo producto: ")
pp2 = int(input("Digite el precio del segundo producto: "))
np3 = input("digite el nombre del tercer proyecto: ")
pp3 = int(input("Digite el precio del tercer producto: "))

promedio = (pp1 + pp2 + pp3) / 3 

print(f"Hola {nombre}, Los nombres y precios de los productos son: {np1}:${pp1},{np2}:${pp2},{np3}:${pp3} y el promedio es: {promedio}")