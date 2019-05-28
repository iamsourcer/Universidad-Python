#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep


PASSWORD = 'Johnny1@'
check_pass = None
INTENTOS = 3

for intento in range(INTENTOS):
    check_pass = input('Ingresa tu contraseña:')
    if check_pass == PASSWORD:
        break
    sleep(3 + intento)

if check_pass == PASSWORD:
    print('Entraste!')
    return True
else:
    print('te qudaste sin intentos')
    return False







# # version con flag
#
# flag = False
# while not flag:
#     check_pass = input('Ingresa tu contraseña:')
#     if check_pass == PASSWORD:
#         flag = True
# print('Entraste!')
#
# # version con break
#
# while True:
#     check_pass = input('Ingresa tu contraseña:')
#     if check_pass == PASSWORD:
#         break
# print('Entraste!')
