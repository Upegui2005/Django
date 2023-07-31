#Averiguar si un numero es par o impar. Luego, averiguar si es positivo o negativo 
#Residuos, Factores 

#Control de errores (Exepciones) en python
#Try... Except 

try:
    num = int(input("Digite un numero: "))
    if num % 2  == 0 and num <=0:
        print(f"{num}, Es par y negativo")
    elif num % 2 == 0 and num >=0:
        print(f"{num} Es par y positivo")
    elif num % 2 != 0 and num <=0:
        print(f"{num}, Es impar y negativo")
    elif num % 2 != 0 and num >=0:
        print(f"{num}, Es impar y positivo")
    else:
        print("Error....")     
except Exception as e:
    print(f"¿Que mierda escribiste para que saliera error?")
