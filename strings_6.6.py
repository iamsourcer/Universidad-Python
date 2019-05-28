#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cadena_limpia(cadena, caracteres_no_validos):
    lista_cadena = list(cadena)
    for letra in cadena:
        if letra in caracteres_no_validos:
            lista_cadena.remove(letra)

    return ''.join(lista_cadena)


def consonantes(cadena):
    vocales = 'AEIOUaeiou'
    return cadena_limpia(cadena, vocales)


def vocales(cadena):
    consonantes = 'BCDFGHIJKLMNPQRSTVWXYZbcdfghijklmnpqrstvwxyz'
    return cadena_limpia(cadena, consonantes)

# print(consonantes('Jonathan'))
# print(cadena_limpia('dni 31.060.013', ' dniDNI.'))


def next_vocal(vocal):
    vocales = ['a', 'e', 'i', 'o', 'u']
    indice = vocales.index(vocal)
    reemplazo = (indice + 1) % 5
    return vocales[reemplazo]


def siguiente_vocal(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    nueva_cadena = []
    for letra in cadena:
        # for i in range(len(vocales)):
        #     if letra == vocales[i]:
        #         if i == 4:
        #             r = 0
        #         else:
        #             r = i + 1
        #
        #         print(letra, vocales[r])

        if letra in vocales:
            nueva_cadena.append(next_vocal(letra))
        else:
            nueva_cadena.append(letra)
    return ''.join(nueva_cadena)


# print(siguiente_vocal('las clases de python son lo mas'))


def palindromo(cadena):
    cadena = cadena.lower()
    largo = len(cadena)
    if largo % 2 == 1:
        largo -= 1
    limite = largo // 2

    for i in range(limite):
        j = -1 - i
        if cadena[i] != cadena[j]:
            return False
    return True


print(palindromo('Menem'))
