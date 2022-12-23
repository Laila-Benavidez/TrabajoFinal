presentacion=input("Hola! Bienvenido, me podrias decir tu nombre por favor")
print(F"Hola {presentacion}, espero que estes bien, vamos a divertirnos un rato")
print("El juego consiste en que debes avinar el numero que estoy pensando entre el 1 al 30, comencemos😀")
numero=int(input("Ingresa un numero"))
while numero != 18:
    print("Lo siento, no adivinaste, intenta de nuevo😅")
    print("Una pista, es una fecha importante para la Argentina ⚽")
    numero=int(input("Ingresa un nuevo numero"))
    if numero>30:
        print("El numero esta fuera del rango, es muy alto, recuerda que es del 1 al 30☝")
    elif numero >1:
        print("El numero esta fuera del rango, es muy pequeño, recuerda que es del 1 al 30☝")
print ("Muy bien, el numero era 18, GANASTE🥳 ")
