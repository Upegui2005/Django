pizza = input("¿Pizza vegetariana o carnivora?:").lower()

if pizza == "carnivora":
    print("Solo puedes elegir un ingrediente, los cuales son:\n-Peperoni\n-Jamon\n-Salmon")
    ingrediente = input("Di el ingrediente:").lower()
    if ingrediente == "peperoni":
        print("Elegiste carnivora, esta pizza trae:\n-Queso\n-Tomate\n-Peperoni")
    elif ingrediente == "jamon":
        print("Elegiste carnivora, esta pizza trae:\n-Queso\n-Tomate\n-Jamon")
    else:
        print("Elegiste carnivora, esta pizza trae:\n-Queso\n-Tomate\n-Salmon")
else:
    print("Solo puedes elegir un ingrediente, los cuales son:\n-Pimiento\n-Tofu")
    ingrediente = input("Di el ingrediente:").lower()
    if ingrediente == "pimiento":
        print("Elegiste vegetariana, esta pizza trae:\n-Queso\n-Tomate\n-Pimiento")
    else:
        print("Elegiste vegetariana, esta pizza trae:\n-Queso\n-Tomate\n-Tofu")
