from random import randint
from time import sleep

def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """

    x = randint(1, 10)
    z = False

    while z == False:
        y = int(input("""Crees que el número es:
(1) Par
(2) Impar
"""))

        if y == 1:
            print("Así que crees que es par...")
            sleep(1)
            if x%2 == 0:
                print("Bacán lo has adivinado")
                z = True
            else:
                print("Intenta de nuevo")

        elif y == 2:
            print("Así que crees que es impar...")
            sleep(1)
            if x%2 != 0:
                print("Bacán lo has adivinado")
                z = True
            else:
                print("Intenta de nuevo")

        else:
            print("Agrega un input válido -> (1) o (2)")
    
    print("FIN DEL JUEGO")

adivinar_par_o_impar()
