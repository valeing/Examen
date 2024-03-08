import random
palabras=['Gitano','Kamikaze','Tormenta,', 'Agua','Aguacate','Amor','Guerra','calamar','Bronce','Oro','Cabello']
palabra=random.choice(palabras)
totalletras=len(palabra)

respuesta = ['-' for _ in range (len(palabra)) ]

salida = ''. join(respuesta)

print(salida)

print('adivina la palabra',totalletras,'letras')

respuesta = 0
while respuesta < 3:
    entrada = input("Ingresa la palabra:")
    respuesta +=1
    if entrada == "Incorrecto":
        break
    else:
        print("se ha superado el numero de intentos")
        print("numero de intento",respuesta)


    
    
    