#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 02:11:59 2020

@author: lucassousareis
"""


import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

imagem = mpimg.imread('imageForQuadtreeCompression.jpg')
imagem.shape
plt.imshow(imagem)                   
                   
class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Node():
    def __init__(self,xi,yi,l,a,pontos):
        self.xi = xi
        self.yi = yi
        self.largura = l
        self.altura = a
        self.pontos = pontos
        self.nosfilhos = []
class QuadTree():
    
    
        
def get_largura(self):
    return self.largura

def get_altura(self):
    return self.altura
def get_pontos(self):
    return self.pontos
