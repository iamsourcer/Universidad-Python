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


def mostrar_tablero(tablero):
    for fila in tablero:
        mostrar_fila(fila)
        print()
    # TODO: agregar indices de fila letra y de columna numero


def posicionar_barco(largo, disposicion, celda_inicial):
    # falta un parametro CLAVE!
    pass


def disparar(fila, columna):
    # toma parametros fila y columna y retorna ???
    # falta un parametro CLAVE!
    pass


def verificar_hundidos():
    pass


tablero = iniciar_tablero(20)
# mostrar_fila(tablero[0])
mostrar_tablero(tablero)
