#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 02:11:59 2020

@author: lucassousareis
"""


from PIL import Image        
import matplotlib.pyplot as plt
import numpy as np
                   
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
        self.imagem = imagem.load()
        # Inicializa o numero de nós da árvore
        self.size = 0
        # Vetor de nós
        self.tree = []
        self.x = imagem.size[0]
        self.y = imagem.size[1]
    
        # Quantidade total de nós folha ou seja qtd de pixels dimensao da imagem
        size = imagem.size[0] * imagem.size[1]
        
        while(size >=1):
            self.size =+ self.size
            size/=4
            size = int(size)
            
            size = imagem.size[0] * imagem.size[1]
            
            for i in range(self.size):
                self.tree.append(Pixel())
                
            k = 0;
            
            for i in range(imagem.size[0] -1, 0 , -2):
                for j in range(imagem.size[1], 0,-2):
                     self.tree[self.size - 1 - 4 * k] = Pixel(self.imagem[i, j], 
                        Ponto(i, j), 
                        Ponto(i, j))
                self.tree[self.size - 2 - 4 * k] = Pixel(self.imagem[i, j - 1], 
                        Ponto(i, j - 1),
                        Ponto(i, j - 1))
                self.tree[self.size - 3 - 4 * k] = Pixel(self.imagem[i - 1, j], 
                        Ponto(i - 1, j), 
                        Ponto(i - 1, j))
                self.tree[self.size - 4 - 4 * k] = Pixel(self.imagem[i - 1, j - 1], 
                        Ponto(i - 1, j - 1), 
                        Ponto(i - 1, j - 1))
                k += 1
                
                
            for i in range(self.size - 4 * k - 1, -1, -1):

                self.tree[i] = Pixel(
                [(self.tree[4 * i + 1].R + self.tree[4 * i + 2].R + self.tree[4 * i + 3].R + self.tree[4 * i + 4].R) / 4,
                 (self.tree[4 * i + 1].G + self.tree[4 * i + 2].G + self.tree[4 * i + 3].G + self.tree[4 * i + 4].G) / 4,
                 (self.tree[4 * i + 1].B + self.tree[4 * i + 2].B + self.tree[4 * i + 3].B + self.tree[4 * i + 4].B) / 4],
                self.tree[4 * i + 1].SuperiorEsquerdo,
                self.tree[4 * i + 4].SuperiorDireito)
                
                
    def display(self, nivel):
        n = 0
 
        # Calcula a posição do nó inicial.
        for i in range(0, nivel):
            n = 4 * n + 1
 
        # Termina o código caso  nível de compressão seja inválido
        if (n > self.dim):
            print('Nivel inválido para compressão maior que a altura da árvore')
            return
 
        # Creates a new image.
        img = Image.new("RGB", (self.x, self.y), "black")
        pixels = img.load()
 
        # Movendo do nó inicial ao final tendo como parâmetro o nível de compressão dado
        for i in self.tree[n : 4 * n]:
            x1 = i.SuperiorEsquerdo.x
            y1 = i.SuperiorEsquerdo.y
            x2 = i.InferiorDireito.x
            y2 = i.InferiorDireito.y
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
 
                    # Atribui a cada pixel um valor RGB
                    pixels[x, y] = (int(i.R), int(i.G), int(i.B))
 
        # Display nova imagem
        img.show();
        plt.imshow(img)
        #Salva imagem obtida via descompressão no diretório do projeto
        img.save('2.jpg')
            
            
        

def main():
    # Faz o upload da imagem
    imagem=Image.open("image.png").convert('RGB')
    # Modifica a imagem para que possa ser utilizável (imagem quadrada)
    largura = np.ceil(np.sqrt(imagem.size[0]*imagem.size[1])).astype(int)  
    imagem = imagem.resize((largura, largura)
    plt.imshow(imagem)
    Tree = Quadtree(imagem)
    Tree.display(8)
    

if __name__=="__main__":
    main()
        
