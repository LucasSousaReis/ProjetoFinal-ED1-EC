#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 02:11:59 2020

@author: lucassousareis
"""


from PIL import Image        
import matplotlib.pyplot as plt 
                   
# Classe que define as coordenadas dos nós da Qtree
class Ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# Classe para associar pixel para cada nó da estrutura
class Pixel(object):
    def __init__(self, cor = [0, 0, 0], 
            SuperiorEsquerdo = Ponto(0, 0), 
            InferiorDireito = Ponto(0, 0)):
        self.R = cor[0]
        self.G = cor[1]
        self.B = cor[2]
        self.SuperiorEsquerdo = SuperiorEsquerdo
        self.InferiorDireito = InferiorDireito


class Quadtree():
    def __init__(self, imagem):
        # Armazena a imagem como um mapa de pixels
        self.imagem = imagem.load
        # Inicializa o numero de nós da árvore
        self.tamanho = 0
        
        # Vetor de nós
        self.tree = []
        self.x = imagem.tamanho[0]
        self.y = imagem.tamanho[1]
    
        # Quantidade total de nós folha
        tamanho = imagem.tamanho[0] * imagem.tamanho[1]
        

def main():

    imagem=Image.open("image.png").convert('RGB')
    plt.imshow(imagem)
   

if __name__=="__main__":
    main()
        
