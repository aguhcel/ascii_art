#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:16:49 2020

@author: 4guhc3l
"""

# Importamos las herramientas para el procesamiento de la imagen
from PIL import Image

# Elegimos la imagen que vamos a convertir
# Hay que aclarar que el 10 es por que se reescala una imagen de 1/10
# Todo dependera de la imagen que ocupemos es el tamaño que vamos a reescalar
# En mi caso es una imagen de 512*512 que se reescala a una imagen de 51*51
imagen = Image.open("doge.jpg")
imagen = imagen.resize((int(imagen.width / 10), int(imagen.height / 10)))

# Definimos los caracteres ASCII que ocuparemos
caracteres = '.', '*', '$'
texto = ''
a, b = 0, 0
x, y, z = 0, 0, 0

# Para cada pixel en la imagen
while y < imagen.height:
# Encontramos el brillo de la imagen
    brillo = sum(imagen.getpixel((x, y))) / 3
# dependiendo del brillo es ASCII que se le asigna
    while z < 3:
        a += 85
        if brillo <= a and brillo >= b:
            texto += caracteres[z]
            texto += caracteres[z]
        b += 85
        z += 1
    z = 0
    a = 0
    b = 0
    if x == imagen.width - 1:
        texto += '\n'
        y += 1
        x = 0
    else:
        x += 1

#Print the output
print(texto)
