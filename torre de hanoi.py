#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:27:52 2023

@author: fabrizio
"""

def juego_hanoi (disco, torre1 = 1, torre2 = 2, torre3 = 3):
    if disco == 1:
        print (torre1 ,"a" ,torre3)
        
    else:
        juego_hanoi(disco -1, torre1, torre3, torre2)
        print(torre1, "a", torre3)
        juego_hanoi (disco -1, torre2, torre1, torre3)
    return


juego_hanoi(5)