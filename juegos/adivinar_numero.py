from random import randint

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    x = randint(1, 10)
    y = int(input("Adivina que número es: "))

    if x == y:
        print("Bacán lo has adivinado")

    else:

        while x != y:
            y = int(input("Adivina que número es: "))

            if x == y:
                print("Bacán lo has adivinado")

            else:
                print("intenta de nuevo")

adivinar_numero()
