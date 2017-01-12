# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:42:20 2017

@author: Alexandre Sales Lima

  Cursos de Big Data & Data Science
  Trabalho 1 Questão 2
"""

import numpy as np



def fibonacci(n):
    if n == 0:
        return print( 0)
    elif n == 1:
        return print( 1 ) 
    f = np.zeros(n,dtype = int)    
    f[0] = 0
    f[1] = 1
    for i in range(2,n,1):
        f[i] = f[i-1] + f[i-2]
        
        
    return print(f[i])
    
    
fibonacci(11)   