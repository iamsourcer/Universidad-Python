#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 

def iniciar_tablero(dimension=5):
    celda = '˜'
    fila = []
    for _ in range(dimension):
        fila.append(celda)

    tablero = []
    for _ in range(dimension):
        tablero.append(fila)
    return tablero


def mostrar_fila(fila):
    for celda in fila:
        print(celda, end=' ')
    print()


def mostrar_tablero(tablero):
    fila_abc = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    dimension = len(tablero)
    print('   ', end='')
    # for i in range(dimension):
    #     print(fila_abc[i], end=' ')
    # print()
    print(' '.join(list(fila_abc[:dimension])))

    for i in range(dimension):
        if i < 10:
            print(' ', end='')
        print(i, end=' ')
        mostrar_fila(tablero[i])


def posicionar_barco(largo, disposicion, celda_inicial):
    # falta un parametro CLAVE!
    pass


def disparar(fila, columna):
    # toma parametros fila y columna y retorna ???
    # falta un parametro CLAVE!
    pass


def verificar_hundidos():
    pass


tablero = iniciar_tablero()
# mostrar_fila(tablero[0])
mostrar_tablero(tablero)
