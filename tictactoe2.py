#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

a1, a2, a3 = 0, 0, 0
b1, b2, b3 = 0, 0, 0
c1, c2, c3 = 0, 0, 0


def sorteo_inicial():
    return randint(1, 2)


def mostrar_tablero():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3

    print(a1, '|', b1, '|', c1)
    print('- ' * 5)
    print(a2, '|', b2, '|', c2)
    print('- ' * 5)
    print(a3, '|', b3, '|', c3)


def validar_posicion(posicion):
    if not isinstance(posicion, str):
        print('validar_posicion:', posicion, 'no es una cadena')
        return False

    if len(posicion) != 2:
        print('validar_posicion: la posicion no tiene 2 caracteres')
        return False

    if posicion[0] != 'a' and posicion[0] != 'b' and posicion[0] != 'c':
        print(posicion[0])
        print('validar_posicion en su indice 0 no es a, b o c')
        return False

    if posicion[1] != '1'and posicion[1] != '2' and posicion[1] != '3':
        print('validar_posicion en su indice 1 no es 1, 2 o 3')
        return False
    return True


def verificar_posicion_libre(posicion):
    global a1, b1, c1, a2, b2, c2, a3, b3, c3

    if not validar_posicion(posicion):
        return False
    if posicion == 'a1':
        return a1 == 0  # Esto retorna True o False porque evalua la expresion
    if posicion == 'a2':
        return a2 == 0
    if posicion == 'a3':
        return a3 == 0
    if posicion == 'b1':
        return b1 == 0
    if posicion == 'b2':
        return b2 == 0
    if posicion == 'b3':
        return b3 == 0
    if posicion == 'c1':
        return c1 == 0
    if posicion == 'c2':
        return c2 == 0
    if posicion == 'c3':
        return c3 == 0


def validar_jugador(jugador):
    if not isinstance(jugador, int):
        print('validar_jugador: No es un entero')
        return False
        # sigo teniendo quilombitos con los AND y los ORs
    if jugador != 1 and jugador != 2:
        print('validar_jugador:', jugador, 'no es 1 o 2')
        return False
    return True


def poner_ficha(jugador, posicion):
    global a1, b1, c1, a2, b2, c2, a3, b3, c3

    if not validar_jugador(jugador):
        return False
    chequeo = verificar_posicion_libre(posicion)
    if chequeo is None:
        return False
    if chequeo is False:
        print('Posicion ocupada!')

    if posicion == 'a1':
        a1 = jugador
    elif posicion == 'a2':
        a2 = jugador
    elif posicion == 'a3':
        a3 = jugador
    elif posicion == 'b1':
        b1 = jugador
    elif posicion == 'b2':
        b2 = jugador
    elif posicion == 'b3':
        b3 = jugador
    elif posicion == 'c1':
        c1 = jugador
    elif posicion == 'c2':
        c2 = jugador
    if posicion == 'c3':
        c3 = jugador

    return True


def chequear_lineaH():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3

    ganador = 0
    if a1 == b1 and b1 == c1 and a1 != 0:
        ganador = a1

    if a2 == b2 and b2 == c2 and a2 != 0:
        ganador = a2

    if a3 == b3 and b3 == c3 and a3 != 0:
        ganador = a3

    return ganador


def chequear_lineaV():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3
    ganador = 0

    if a1 == a2 and a2 == a3 and a1 != 0:
        ganador = a1
    if b1 == b2 and b2 == b3 and b1 != 0:
        ganador = b1
    if c1 == c2 and c2 == c3 and c1 != 0:
        ganador = a1
    return ganador


def chequear_lineaD():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3
    ganador = 0
    diagonal_descendente = a1 == b2 and b2 == c3 and a1 != 0
    if diagonal_descendente:
        ganador = a1
    diagonal_ascendente = a3 == b2 and b2 == c1 and a3 != 0
    if diagonal_ascendente:
        ganador = a3
    print('da:', diagonal_ascendente, 'dd:', diagonal_descendente)
    return ganador


def hay_linea():
    # Combina los chequeos anteriores
    # return (int): chequea si hay un ganador.
    #   retorna 1 si es jugador 1
    #   retorna 2 si es jugador 2
    #   retorna 0 si no hay ganadores
    ganador = chequear_lineaH()
    if ganador != 0:
        return ganador
    ganador = chequear_lineaV()
    if ganador != 0:
        return ganador
    # ganador = chequear_lineaD()
    # if ganador != 0:
    #     return ganador
    # return 0
    return chequear_lineaD()

def tablero_lleno():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    condicion1 = a1 != 0 and a2 != 0 and a3 != 0
    condicion2 = b1 != 0 and b2 != 0 and b3 != 0
    condicion3 = c1 != 0 and c2 != 0 and c3 != 0
    return condicion1 and condicion2 and condicion3


def cambiar_jugador(jugador):
    # param jugador(int): numero de jugador actual
    # return (int): jugador actualizado de 1 a 2 o de 2 a 1
    if jugador == 1:
        return 2
    else:
        return 1


def main():
    print('TA - TE - TI (v2.0)')
    print()
    jugador = sorteo_inicial()
    print('Comienza el jugador: {}'.format(jugador))
    # assert (validar_jugador(13) is False)

    while not tablero_lleno() and not hay_linea():
        jugada_valida = False
        while not jugada_valida:
            posicion = input('Jugador {} ingresar posicion:'.format(jugador))
            posicion = posicion.lower()
            jugada_valida = poner_ficha(jugador, posicion)
            if jugada_valida:
                mostrar_tablero()
                jugador = cambiar_jugador(jugador)

    if tablero_lleno():
        print('Empate!')
    else:
        print('Felicitaciones ganaste!')


if __name__ == '__main__':
    main()
