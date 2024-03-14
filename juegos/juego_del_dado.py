from random import(randint)

def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    print("""Asumamos ya sabes las reglas del juego...""")
    z = False
    pc = 0
    user = 0
    
    while z == False:
        print("Presiona enter para lanzar un dado...")
        input()
        x = randint(1,6)
        print(f"Te ha salido un: {x}")
        user += x
        print(f"Sumas {user} puntos")
        if user >= 30:
            print("has ganado!")
            z = True
            break
        y = randint(1,6)
        print(f"Al pc le ha salido un {y}")
        pc += y
        print(f"El pc suma {pc} puntos")
        if pc >= 30:
            print("has perdido :()")
            z = True
    
    print("FIN DEL JUEGO")


juego_del_dado()