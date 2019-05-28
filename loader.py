#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


def loading(seconds, chars, fps=8):
    i = 0
    for step in range(seconds * fps):
        print(chars[i], end="", flush=True)
        time.sleep(1/fps)
        print("\b" * len(chars[i]), end="", flush=True)
        i += 1
        i = i % len(chars)


dots = ['.   ', '..  ', '... ', '....', '... ', '..  ']
chars = ['|', '/', '-', '\\']
punto = ['.   ', '  . ', '   .', '  . ', ' .  ']

loading(5, punto, 8)
