p1 = input("¿Estudiaste para el examen?")
if p1 == "si":
    print("Continuar con la siguiente pregunta")
    p2 = input("¿Aprobo el examen?")
    if p2 == "si":
        print("Continuar con la siguiente pregunta")
    elif p2 == "no":
        print("Estudiar Mas")
    p3 = input("¿Su calificacion fue mayor a 3.5?")
    if p3 == "si":
        print("Continuar con la siguiente pregunta")
    elif p3 == "no":
        p4 = input("Fue mayor a 2?")
        if p4 == "si":
            print("Casi lo logras")
        else:
            print("Debes ezforzarte mas")
    p5 = input("¿Ya termino el trimestre?")
    if p5 == "si":
        print("Felicidades")
    else: 
        print("Sigue asi")
else:
    print("Finalizado")
