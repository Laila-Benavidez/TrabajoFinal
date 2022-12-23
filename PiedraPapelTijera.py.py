import random
from time import sleep

opciones= ["piedra", "papel", "tijera"]
def opcion():
    opcion= input("selecciona SI para continuar, NO para salir").lower
    return opcion()


print("Hola! Espero que estes bien, en este apartado jugaremos a piedra, papel o tijera🤩")
sleep(1)
print("""Te explicare las reglas, las cuales son sencillas, cada uno elige una opcion
piedra le gana a tijeras
tijeras le gana a papel
papel le gana a piedra
si ambos elegimos lo mismo es un empate, estas listo? comencemos""")
sleep(2)
seleccion=opcion()

sleep(1)
while seleccion=="si":
    jugador= input("Elige piedra, papel o tijera").lower()
    if jugador not in opciones: 
        print("No es una opcion valida, intenta nuevamente😓")
        continue #para que vuelva a preguntar
    computadora= random.choice(opciones)
    print("Yo elijo: ", computadora)
    sleep(1) #No sea tan rapido el resultado
    if jugador==computadora:
        print(F"¡Empatamos!, los dos elegimos {computadora}😎")
        sleep(1)
        seleccion=opcion()
        print(seleccion)
        continue
    elif jugador=="piedra" and computadora=="tijera":
        print(f"Muy bien, ganaste, la piedra✊ le gana a las tijeras✌")
        sleep(1)
        seleccion=opcion()
        continue
    elif jugador=="papel" and computadora=="piedra":
        print(f"Muy bien, ganaste, el papel✋ le gana a la piedra✊")
        sleep(1)
        seleccion=opcion()
        continue
    elif jugador=="tijera" and computadora=="papel":
        print(f"Muy bien, ganaste, la tijera✌le gana al papel✋")
        sleep(1)
        seleccion=opcion()
        continue
    else:
        print(F"Perdiste, {computadora} gana contra {jugador}😵")
        sleep(1)
        seleccion=opcion()
        continue
sleep(1)
print("Gracias por jugar, hasta la proxima❤")
