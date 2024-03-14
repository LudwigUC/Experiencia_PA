from random import randint
from time import sleep

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    print("Veamos que tan buena memoria tienes...")

    w = False
    while w == False:
        print("Memoriza la siguiente secuencia")
        list = []
        for i in range(7):
            list.append(randint(0,9))

        print(list)
        print("Tienes 3 seg para memorizarla...")
        sleep(3)
        for i in range(5):
            print(" ")
        print("Ingresa uno a uno los números que viste:")
        ans = []
        for i in range(7):
            q = int(input())
            ans.append(q)

        print(list)
        print(ans)
        
        if ans == list:
            print("has ganaooo")
            w = True
        else:
            print("buen intento")

    print("FIN DEL JUEGO")


memoria()