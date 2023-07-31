# Condicionales anidados
# Un condicional dentro de otro
# Son infinitos

tengo_dinero = "Si"
tengo_hambre = "Si"
plato_correcto = "Si"

if tengo_dinero == "Si":
    if tengo_hambre == "Si":
        print("Comer")
    else:
        print("Espera a tener hambre")
else:
    if tengo_hambre == "Si":
        print("Fiar.... ")
    else:
        if plato_correcto == "Si":
            print("Fio y como")
        else:
            print("Me voy para la casa")
