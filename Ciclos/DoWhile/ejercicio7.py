n = int(input("Digite un num para saber su factorial:"))

total = 1
cont = n

while cont > 1:
    total = total * cont
    print(cont)
    cont -= 1

print(f"{n}! = {total}")
