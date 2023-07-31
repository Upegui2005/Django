edades = [18, 58, "ap"]

print(edades)
print(len(edades))

edades.insert(4, "ADSO")
print(edades)
print(len(edades))

edades = []
for i in range(3):
    edades.append(int(input(f"Digite la edad {i+1}: ")))
print(edades)