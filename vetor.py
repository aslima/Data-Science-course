# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:42:20 2017

@author: Alexandre Sales Lima

  Cursos de Big Data & Data Science
  Trabalho 1 Questão 3
"""



import numpy as np

def cria_vetor(v1):
    tm = len(v1)*2    
    v2 = np.zeros(tm, dtype = int)      # Cria um vetor com o dobro do tamanho de v1    
    v1a = v1*2                          # Multiplica v1 por 2
    x = 0
    y = 0

    for i in range(tm):
        if i%2 == 0:			     # Identifica se i é par 
            v2[i]=v1[x]
            x += 1
        else:
            v2[i]=v1a[y]
            y += 1
    return print (v2)                   # Retorna v2 preenchido


v = np.array([1,9,6,1,27,36,18,25])

cria_vetor(v)