#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:46:21 2023

@author: fabrizio
"""


def funcion (*args):
    print (args)

funcion (1,5,9,5,"Hola")

#%%

def sum_all (*args):
    x = 0
    for n in args:
        x = x + n
    return x

print(sum_all(1,5,9,5,5,9))

#%%

def sum_all (*args):
    if len(args) == 1:
        return args[0]
    else:
        ans = args[0] + sum_all(*args[1:])
        return ans
        
print(sum_all(1,5,9,5,5,9))

#%% 

def func (*args, **kwargs):
    print (args)
    print (kwargs)

print(func("as",nombre = "Oli", apellido = "Agüero"))

#%% 
def saludar (nombre1, apellido):
    print (f"Hola {nombre1} {apellido}")

dic = {"nombre1":"Oli", "apellido":"Agüero"}

print (saludar(**dic))

#%%

import numpy as np

lista = [1,2,3]

lista2 = np.array(lista)

listita = lista * 2

listita2 = lista2 * 2

print(lista)

print(lista2)

print(listita)

print(listita2)

#%%

"""
Los sets no están ordenados y borra los repetidos 
"""
s = {3,9,1,3,6,15}

def f(x):
    return 2*x + 3

"""
Para recursión siempre hay que definir el caso base para que en algún momento termine 
la función
Después ver una forma de simplificar el problema. 
"""

def fact (n):
    if n == 0:
        return 1
    else:
         ans = n*fact(n-1)
         return ans
    
def suma (n):
    if n == 0:
        return 0
    else:
         ans = n + fact(n-1)
         return ans

def cuenta (n):
    if n == 0:
        return 0
    else:
         ans = (n+1)*(n/2)
         return ans

#%%

#recursividad

def MCD_euclides (a,b):
    if b==0:
        return a 
    else:
        resto = a%b
        ans = MCD_euclides (b,resto)
        return ans

a = int(input("Ingrese un número natural:"))
b = int(input ("Ingrese otro número natural:"))

resultado = MCD_euclides (a,b)

print ("El MCD es", resultado)


#%%
"""Función para pasar de números decimales a binarios"""

def dec_a_bin (num):
    if num < 0:
        print ("Error. El número debe ser positivo.")
    if num == 0:
        return ""
    else:
        div = num // 2
        ans = dec_a_bin(div) + str(num%2)
        return ans
        
num = int(input("Ingrese un número:"))

print("Su número binario es", dec_a_bin(num))
    

#%%

def fibonacci (n):
    if n in {0,1}:
        return n 
    else:
        ans = fibonacci (n-1) + fibonacci (n-2)
        return ans 

fibonacci (5)


#%%

"""Base de programa para el juego de los elementos"""

lista = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 
 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 
 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium', 
 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium', 
 'Europium', 'Fermium', 'Flerovium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 
 'Germanium', 'Gold', 'Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 
 'Iodine', 'Iridium', 'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 
 'Livermorium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury',
 'Molybdenum', 'Moscovium', 'Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium',
 'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 
 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 
 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 
 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 
 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 
 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 
 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

list_ans = []

def secuencia (elemento,lista):
    for palabra in lista:
        palabra = palabra.lower()
        if palabra[-1] == elemento[0]:
            list_ans.append(palabra)
        if palabra[0] == elemento[-1]:
            list_ans.append(palabra)
    return list_ans

elemento = input("Ingrese un elemento:")
respuesta = secuencia (elemento, lista)
print(respuesta)

#%%

"""Función para sacar el valor actual de una lista de flujos y una TIR"""

l_flujos = [1500,3200,6800,2330,4790,5092]

def valor_actual (flujos,TIR):
    if len(flujos) == 0:
        return 0
    else:
        valor = flujos[0]/(1+TIR)**len(flujos)
        VA = valor + valor_actual (flujos[1:],TIR)
        return VA

print (valor_actual(l_flujos,0.05))

def valor_futuro (flujos,TIR):
    if len(flujos) == 0:    
        return 0
    else:
        valor = flujos[0]*(1+TIR)**len(flujos)
        VF = valor + valor_futuro(flujos[1:],TIR)
        return VF
    
#%%

class human:
    pass
x = human()

#%%
 
class A ():
    x = 23

class B (A):
    y = 30
    x = 12

z = B()

#%%

class A():
    x=23
class B (A):
    y=40
    def __init__(self, value):
        self.z=value
    

w =B(50)

print(w.z)

#%%

class FF ():
    def __init__(self, flujos, tasa):
        self.flujos = flujos
        self.tasa = tasa
    
    def VAN (self, tir, n = 0):
        if n == len(self.flujos):
            salida = 0
            """
            utilizo 2 returns por recursividad
            """
        else:
            salida = self.flujos[n]+1/(1+tir)*self.VAN(tir,n+1)
        salida = self.VAN (tir, self.flujos)
        return salida
    
    def VF (self, t):
        pass

va= FF([-100,50,20,90],0.5)


#%%

def funcion (*args):
    print(args)
    
funcion("a lucas le gusta filosofia")

#%%

def sum_all (*args):
    if len(args) == 1: 
        return args [0]
    else: 
        ans = args[0] + sum_all(*args[1:])
        return ans
        
        
print(sum_all(1,5,9))

#%%

def sum_all (*args):
    x = 0
    for numeros in args:
        x += numeros
    return x

print(sum_all(1,5,9))

#%%

def func (*args, **kwargs):
    print (kwargs)

print (func(nombre = 'Fer', apellido = 'Kricun'))

#%%

def saludar (primer_nombre, apellido):
    print (f"Hola {primer_nombre} {apellido} ")
    
nombre = { 
    "primer_nombre": "Lucas",
    "apellido": "Gens"
    }
saludar(**nombre)

#%%

class Alumno:
    pass

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.nombre = "Fernando"
alumno1.apellido = "Kricun"
alumno1.email = "fkricun@udesa.edu.ar"

alumno2.nombre = "Fernando"
alumno2.apellido = "Herrera"
alumno2.email = "fherrera@udesa.edu.ar"

print(alumno1.email)
print(alumno2.email)

#%%

class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.email = nombre[0].lower() + apellido.lower() + "@udesa.edu.ar"
        
alumno1 = Alumno("Fernando", "Kricun")
alumno2 = Alumno("Fernando", "Herrera")

print(alumno1.email)
print(alumno2.email)



#%%

##otra opcion de valor futuro

class ValorFuturoTIR:
    def __init__(self, flujos_fondos):
        self.flujos_fondos = flujos_fondos
    
    def valor_futuro(self, tir, periodo=None):
        vp = 0
        vf = 0
        n = len(self.flujos_fondos)
        if periodo is None:
            for i in range(n):
                vp += self.flujos_fondos[i] / (1 + tir) ** i
            vf = vp * (1 + tir) ** n
        else:
            fp = self.flujos_fondos[periodo] / (1 + tir) ** periodo
            for i in range(periodo):
                vp += self.flujos_fondos[i] / (1 + tir) ** i
            vf = vp + fp
        return vf
    
flujos_fondos = [-100, 200, 300, 400, 500]
vft = ValorFuturoTIR(flujos_fondos)
vf = vft.valor_futuro(0.10, 4)
print(vf)

#%%

def z(x):
    return sum(x)

if __name__ == "__main__":
    a = zip(*[[1,2,3],[4,5,6],[7,8,9]])
    b = list(map(lambda x: sum(x), a))
    print (b)
    #lambda es para funciones basicas, no es necesario crear una f(x)
    #zip agarra el primer valor de cada lista y hace una tupla y asi
    
#%%

def s(x):
    return sum(x)

if __name__ == "__main__":
    a = zip(*[[1,2,3],[4,5,6],[7,8,9]])
    b = list(filter(lambda x: x[1] >= 5, a))
    print (b)
    
    #filter, se esta usando para que solo devuelva las listas que su numero de la posicion 1 es > a 5
    
#%%

def r(x):
    return sum(x)

if __name__ == "__main__":
    a = zip(*[[1,2,3],[4,5,6],[7,8,9]])
    b = list(sorted(a, key = lambda x: x[2], reverse = True))
    print (b)

#sorted te acomoda la funcion en este caso mira el numero en la posicion 2 y los acomoda con sus listas de mayor a menor

#%%

class myarray1:
    def __init__(self, elems):
        self.elems = elems
    def __add__ (self, other):
        aux = zip(self.elems, other.elems)
        aux = map(lambda x: list(zip(*x)),aux)
        aux = list(map(lambda x: list(map(lambda a: sum(a),x)),aux))
        return aux
    
    def __mul__(self, other):
        aux = map(lambda x: list(map(lambda a: a * other, x)), self.elems)
        return list(aux)
    
    def __rmul__ (self, other):
        return self * other
    
    def __matmul__ (self,other):
        if len(other.elems) == len(self.elems[0]):
            matrix_2t = list(zip(*other.elems))
            matrix_1 = self.elems
            aux1 = [len(matrix_2t) * fila for fila in matrix_1]
            aux2 = matrix_2t * len(matrix_2t)
            aux3 = []
            for elem in aux1:
                aux3 += elem
            aux = zip(aux3, aux2)
            return list(aux)
if __name__ == "__main__":
    matrix1 = myarray1 ([[1,2,3],[4,5,6],[7,8,9]])
    matrix2 = myarray1 ([[1,2,3],[4,5,6],[7,8,9]])
    print(matrix1 + matrix2)
    print (3 * matrix1)
    print (matrix1@matrix2)
        
            



