mes = input("Digite su mes de nacimiento")
dia = int(input("Digite su dia de nacimiento"))

if mes == "Enero":
    if dia >= 21:
        print("Acuario")
    else:
        print("Crapricornio")
elif mes == "Febrero":
    if dia <=19:
        print("Acuario")
    else:
        print("Piscis")
elif mes == "Marzo":
    if dia <=20:
        print("Piscis")
    else:
        print("Aries")
elif mes == "Abril":
    if dia <=20: 
        print("Aries")
    else:
        print("Tauro")
elif mes == "Mayo":
    if dia <= 20:
        print("Tauro")
    else:
        print("Gemimis")
elif mes == "Junio":
    if dia <= 21:
        print("Geminis")
