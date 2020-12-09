#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 03:54:57 2020

@author: lucassousareis
"""



from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
 

# Cada nó é identificado por um ponto ()
class Ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#   Classe que atribui Pixel a cada  nó da estrutura
class Pixel(object):
    def __init__(self, cor = [0, 0, 0], 
            superiorEsquerdo = Ponto(0, 0), 
            superiorDireito = Ponto(0, 0)):
        self.R = cor[0]
        self.G = cor[1]
        self.B = cor[2]
        self.superiorEsquerdo = superiorEsquerdo
        self.superiorDireito = superiorDireito
 
# Implementação da Quadtree via vetores 
class quadtree():
    def __init__(self, imagem):
 
        # Número de total de nós 
        self.size = 0
 
        
        self.imagem = imagem.load()
 
        # vetor de nos
        self.tree = []
        self.x = imagem.size[0]
        self.y = imagem.size[1]
 
        # Numero total de nos folha
        size = imagem.size[0] * imagem.size[1]
 
        # conta numero de nos
        while(size >= 1):
            self.size += size
            size /= 4
            size=int(size)
 
        size = imagem.size[0] * imagem.size[1]
 
    
        for i in range(self.size):
            self.tree.append(Pixel())
 
        # Armazena primeiramente os nos folha
        count = 0
        for i in range(imagem.size[0] - 1, 0, -2):
            for j in range(imagem.size[1] - 1, 0, -2):
                self.tree[self.size - 1 - 4 * count] = Pixel(self.imagem[i, j], 
                        Ponto(i, j), 
                        Ponto(i, j))
                self.tree[self.size - 2 - 4 * count] = Pixel(self.imagem[i, j - 1], 
                        Ponto(i, j - 1),
                        Ponto(i, j - 1))
                self.tree[self.size - 3 - 4 * count] = Pixel(self.imagem[i - 1, j], 
                        Ponto(i - 1, j), 
                        Ponto(i - 1, j))
                self.tree[self.size - 4 - 4 * count] = Pixel(self.imagem[i - 1, j - 1], 
                        Ponto(i - 1, j - 1), 
                        Ponto(i - 1, j - 1))
                count += 1
 
        # Calcula e cria nos nao folha
        for i in range(self.size - 4 * count - 1, -1, -1):

            self.tree[i] = Pixel(
                [(self.tree[4 * i + 1].R + self.tree[4 * i + 2].R + self.tree[4 * i + 3].R + self.tree[4 * i + 4].R) / 4,
                 (self.tree[4 * i + 1].G + self.tree[4 * i + 2].G + self.tree[4 * i + 3].G + self.tree[4 * i + 4].G) / 4,
                 (self.tree[4 * i + 1].B + self.tree[4 * i + 2].B + self.tree[4 * i + 3].B + self.tree[4 * i + 4].B) / 4],
                self.tree[4 * i + 1].superiorEsquerdo,
                self.tree[4 * i + 4].superiorDireito)
        

    # A partir do nivel de compressao produz outra imagem
    def disp(self, nivel):
        k = 0
 
        # Determina ponto de inicio da compressao, estabelece um treshhold
        for i in range(0, nivel):
            k = 4 * k + 1
 
        
        if (k > self.size):
            print('Tente outra vez com um nível de compressão menor')
            return
 
        img = Image.new("RGB", (self.x, self.y), "black")
        pixels = img.load()
 
        # Começando por k até o ultimo nó da estrutura
        for i in self.tree[k : 4 * k]:
            x1 = i.superiorEsquerdo.x
            y1 = i.superiorEsquerdo.y
            x2 = i.superiorDireito.x
            y2 = i.superiorDireito.y
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
 
                    # atribui valor RGB especifico a cada no
                    pixels[x, y] = (int(i.R), int(i.G), int(i.B))
 
        
        #mg.show();
        #plt.subplot(212)
        #plt.imshow(img)
        #plt.title('Imagem Comprimida ')
        # Salva imagem obtida via decomposição
        #img.save('2.jpg')
        return img



def main():

    
    #I=imagem.open("imagem.png").convert('RGB')
    imagem=Image.open("emc.jpg").convert('RGB')
    Tree=quadtree(imagem)
    img2 = Tree.disp(4)
    img3 = Tree.disp(6)
    img4 = Tree.disp(7)
    plt.subplot(2, 2, 1)
    plt.imshow(imagem)
    plt.title('Imagem Original')
    
    plt.subplot(2, 2, 2)
    plt.imshow(img2)
    plt.title('n = 4', fontsize = 14)


    plt.subplot(2, 2, 3)
    plt.imshow(img3)
    plt.title('n = 5', fontsize = 14)


    plt.subplot(2, 2, 4)
    plt.imshow(img4)
    plt.title('n = 7', fontsize = 14)


    figure.tight_layout(pad=0.6)
    plt.show()   


    
if __name__=="__main__":
    main(),