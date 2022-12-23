import random

def lazarDados():
    return random.randint(1,6)
    
print("Hola! Espero que estes bien, en esta oportunidad vamos a jugar a tirar el dado. ¿Estas listo?😄")
jugador= int(input("Deseas tirar ahora el dado?, responde por favor 1 para si, 2 para no🎲"))

while True:
    try:
        if jugador == 1:
            resultado= lazarDados()
            print("El numero del dado es⭐", resultado)
            jugador= int(input("Deseas tirar nuevamente el dado?, responde por favor 1 para si o 2 para no🎲"))
        elif jugador > 2:
            print("el numero no corresponde😐")
            jugador= int(input("Deseas tirar nuevamente el dado?, responde por favor 1 para si o 2 para no🎲"))
        elif jugador==2:
            print ("Muchas gracias por haber jugado, nos vemos pronto👋")         
            print ("Hasta la proxima😄")
            break
    except:
        print("Lo lamento, el caracter no es correcto, intentalo nuevamente😐")
        