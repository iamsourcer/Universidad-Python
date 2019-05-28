#!/usr/bin/env python3


# matrix = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10],
#           [11, 12, 13, 14, 15]]

# matrix[1][2]

# for fila in matrix:
#     for celda in fila:
#         print(celda, end=' ')
#     print()


# char = '@'
# alto = 9
# ancho = 10
# incremento = -1
# for fila in range(alto):
#     for col in range(ancho):
#         print(char, end=' ')
#     print()
#     ancho += incremento
#     if ancho == 1:
#         incremento = 1


'''
@@@@@@@@@@ 0 - 10
2@@@@@@@@2 1 - 8
22@@@@@@22 2 - 6
222@@@@222 3 - 4
2222@@2222 4 - 2

'''

"""
2222@@2222
222@@@@222
22@@@@@@22
2@@@@@@@@2
@@@@@@@@@@

"""


def calc_ancho(fila, ancho):
    return ancho - (2 * fila)

# espacio = ' '
# char = '@'
# ancho = 10
# alto = 5
# for fila in range(alto):
#     # imprimir espacios de inicio
#     for _ in range(fila):
#         print(espacio, end='')
#     # imprimir char
#     for _ in range(calc_ancho(fila, ancho)):
#         print(char, end='')
#     # imprimir espacios del final
#     for _ in range(fila):
#         print(espacio, end='')
#     print()


space = ' '
char = '@'
lenght = 10
height = 5
count = lenght

for row in range(height):
    # print out the spaces
    for _ in range(height - row - 1):
        print(space, end='')
    for _ in range(lenght - count + 2):
        print(char, end='')
    for _ in range(height - row - 1):
        print(space, end='')
    count -= 2
    print()

#
# days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
#
#
# def calendario(day, days):
#     return days[(day % 7) - 1]
#
#
# preguntame = int(input('Dame un dia: '))
# print(calendario(preguntame, days))
