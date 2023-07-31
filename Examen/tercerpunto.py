valorhora = float(input("¿Cuanto te pagan la hora?:"))
horaentrada = int(input("Escribe tu hora de entrada en hora en militar:"))
horastrabajadas = int(input("Escribe las horas trabajadas en horario militar:"))
diastrabajados = int(input("¿Cuantos dias trabajaste?:"))
sumar = horaentrada + horastrabajadas 

if horaentrada > 15 or horastrabajadas > 8:
    print("Error")
elif sumar <= 18:
    pago = horastrabajadas * valorhora
    pagodias = pago * diastrabajados
    print(f"Su pago al dia fue de {pago} y su pago total fue de {pagodias}")
else:
    if sumar == 19:
        pago = ((horastrabajadas * valorhora) * 0.10) + horastrabajadas * valorhora
        pagodias = pago * diastrabajados
        print(f"Su pago al dia fue de {pago} y su pago total fue de {pagodias}")
    elif sumar == 20:
        pago = ((horastrabajadas * valorhora) * 0.20) + horastrabajadas * valorhora
        pagodias = pago * diastrabajados
        print(f"Su pago al dia fue de {pago} y su pago total fue de {pagodias}")
    elif sumar == 21:
        pago = ((horastrabajadas * valorhora) * 0.30) + horastrabajadas * valorhora
        pagodias = pago * diastrabajados
        print(f"Su pago al dia fue de {pago} y su pago total fue de {pagodias}")
    elif sumar == 22:
        pago = ((horastrabajadas * valorhora) * 0.40) + horastrabajadas * valorhora
        pagodias = pago * diastrabajados
        print(f"Su pago al dia fue de {pago} y su pago total fue de {pagodias}")
    else:
        pago = ((horastrabajadas * valorhora) * 0.50) + horastrabajadas * valorhora
        pagodias = pago * diastrabajados
        print(f"Su pago al dia fue de {pago} y su pago total fue de {pagodias}")
 