# Matrices, Vectores(listas) multidimensionales

aprendices = [
    [999, "Andres", "Martinez"],
    [555, "Maria", "Ossa"],
    [555, "Leidy", "Echavarria"]
]

tam1 = len(aprendices)
print("="*40)
print("Cedula\t\tNombre\t\tApellido")
print("="*40)
for x in range(tam1):
    tam2 = len(aprendices[x])
    for y in range(tam2):
        print(aprendices[x][y], end="\t\t\t")
    print("\n----------------------------------------")
