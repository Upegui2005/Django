#Construya un software que permita saber el mayor de los tres 

num = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))
num3 = int(input("Digite el ultimo numero: "))

if num > num2 > num3:
    print(f"{num}, Es el mayor")
elif num < num2 > num3:
    print(f"{num2}, Es el mayor")
else:
    print(f"{num3}, Es el mayor")