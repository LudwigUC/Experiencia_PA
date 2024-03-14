from random import randint
from time import sleep

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    print(""" BIENVENIDO A PIEDRA, PAPEL O TIJERA
          
Lucharás contra el PC, que escogerá una opción en UNO...""")
    sleep(1)
    print("DOS...")
    sleep(1)
    print("""Ahora es cuando debes lanzar tu jugada!
¿Qué eliges?:
          
(1) Piedra
(2) Papel
(3) Tijera """)
    y = randint(1,3)
    w = False

    while w == False:
        x = int(input("-> "))
        z = 0

        print("TREEEEEEEEEEEEEES")

        w = True
        if x == 1:
            if y == 2:
                z = -1
            elif y == 2:
                z = 1
        elif x == 2:
            if y == 1:
                z = 1
            elif y == 3:
                z = -1
        elif x == 3:
            if y == 1:
                z = -1
            elif y == 2:
                z = 1
        else:
            print("Agrega un input válido")
            w = False

    if z == 0:
        print("Empataste")
    elif z == -1:
        print("Perdiste")
    else:
        print("Ganaste")


    print("FIN DEL JUEGO")

cachipun()