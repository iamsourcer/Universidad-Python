#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# datos = tablero

"""
Tenemos un tablero que consta de 9 casilleros representados como variables int

        a1, b1, c1
        a2, b2, c2
        a3, b3, c3

Los valores posibles para estos int son:

    0 - casillero libre
    1 - ficha jugador 1
    2 - ficha jugador 2

En esta primera version utilizaremos variables globales

"""

# El tablero inicia vacio
a1, b1, c1 = 0, 0, 0
a2, b2, c2 = 0, 0, 0
a3, b3, c3 = 0, 0, 0

# Logica = funciones


def mostrar_tablero():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    # No retorna nada, imprime por pantalla
    print()
    print(a1, '|', b1, '|', c1)
    print(5 * '- ')
    print(a2, '|', b2, '|', c2)
    print(5 * '- ')
    print(a3, '|', b3, '|', c3)
    print()


def sorteo_inicial():
    # retorna un int 1 o 2
    return random.randint(1, 2)


def validar_jugador(jugador):
    if jugador != 1 or jugador != 2:
        return False
    return True


def validar_posicion(posicion):
    if not isinstance(posicion, str):
        print('validar_posicion:', posicion, 'no es un string')
        return False
    if len(posicion) != 2:
        print('validar_posicion:', posicion, 'no tiene 2 caracteres')
        return False
    # if not posicion[0].isalpha():
    #     return False
    if posicion[0] != 'a' and posicion[0] != 'b' and posicion[0] != 'c':
        print('validar_posicion:', posicion, 'no empieza con a,b,c')
        return False
    # if not posicion[1].isdigit():
    #     return False
    if posicion[1] != '1' and posicion[1] != '2' and posicion[1] != '3':
        print('validar_posicion:', posicion, 'no termina con 1,2 o 3')
        return False

    return True


def test_validar_posicion():
    assert (validar_posicion(13) is False), 'Validar string no funca'
    assert (validar_posicion('1234') is False), 'Validar largo no funca'
    assert (validar_posicion('z1') is False), 'Validar posicion[0] no funca'
    assert (validar_posicion('a8') is False), 'Validar posicion[1] no funca'
    assert (validar_posicion('a1') is True), 'Validar posicion no funca'


# def verificar_posicion_libre(posicion):
#     # retorna True o False segun corresponda
#     if not validar_posicion(posicion):
#         print('ERROR - Posicion no valida')
#         return
#     # if globals()[posicion] == 0:
#     #     return True
#     # else:
#     #     return False
#     return globals()[posicion] == 0


def verificar_posicion_libre(posicion):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if not validar_posicion(posicion):
        return
    if posicion == 'a1':
        return a1 == 0
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


def poner_ficha(jugador, posicion):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    # Utiliza funcion verificar_posicion_libre para validar la jugada y nos
    # retorna True o False
    if not isinstance(jugador, int):
        print('poner_ficha:  parametro jugador no es entero')
        return False
    if jugador != 1 and jugador != 2:
        print('poner_ficha:  parametro jugador no es 1 o 2')
        return False
    chequeo = verificar_posicion_libre(posicion)
    if chequeo is None:
        return False
    if chequeo is False:
        print('poner_ficha: parametro posicion ocupado')
        return False


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

    # yo ya se que voy a retornar true siempre
    return True


def chequear_lineaH():
    # return (int)
    global a1, b1, c1, a2, b2, c2, a3, b3, c3
    ganador = 0
    if a1 == b1 and b1 == c1 and a1 != 0:
        ganador = a1  # Elijo cualquier variable porque son todas iguales
    if a2 == b2 and b2 == c2 and a2 != 0:
        ganador = a2
    if a3 == b3 and b3 == c3 and a3 != 0:
        ganador = a3
    return ganador


def chequear_lineaV():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3
    condicion1 = a1 == a2 and a2 == a3 and a1 != 0
    condicion2 = b1 == b2 and b2 == b3 and b1 != 0
    condicion3 = c1 == c2 and c2 == c3 and c1 != 0

    return condicion1 or condicion2 or condicion3


def chequear_lineaD():
    global a1, b1, c1, a2, b2, c2, a3, b3, c3
    diagonal_descendente = a1 == b2 and b2 == c3 and a1 != 0
    diagonal_ascendente = a3 == b2 and b2 == c1 and a2 != 0

    return diagonal_ascendente or diagonal_descendente


def chequear_linea():
    # Combina los chequeos anteriores
    # return (int): chequea si hay un ganador.
    #   retorna 1 si es jugador 1
    #   retorna 2 si es jugador 2
    #   retorna 0 si no hay ganadores
    ganador = 0
    if chequear_lineaH:
        ganador = chequear_lineaH


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

    print('TA TE TI')
    print()
    jugador = sorteo_inicial()
    print('Empieza Jugador :', jugador)

    while not tablero_lleno() and not chequear_linea():
        jugada_valida = False
        while not jugada_valida:
            posicion = input(f'Jugador {jugador} ingresar posicion:').lower()
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
