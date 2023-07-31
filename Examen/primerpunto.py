num = int(input("Digite un numero:"))
num2 = int(input("Digite un numero:"))
num3 = int(input("Digite un numero:"))
num4 = int(input("Digite un numero:"))
num5 = int(input("Digite un numero:"))
num6 = int(input("Digite un numero:"))

if num > num2:
    if num2 > num3:
        if num3 > num4:
            if num4 > num5:
                if num5 > num6:
                    print(f"El {num} es el mayor y {num6} es el menor")
        else: 
            if num3 < num4:
                if num3 > num6:
                    print(f"El {num} es el mayor y {num6} es el menor")
                elif num6 > num3:
                    print(f"El {num} es el mayor y {num6} es el menor")           
    else:
        if num6 > num2:
            print(f"El {num} es el mayor y {num2} es el menor")
        else:
            print(f"El {num} es el mayor y {num6} es el menor")
