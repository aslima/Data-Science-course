# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:57:25 2017

@author: Alexandre Sales Lima

  Cursos de Big Data & Data Science
  Trabalho 1 Questão 1
"""




def resultado (p1,p2,p3):
    
    media = round((p1 + p2 + p3)/3,1)
    if media >= 7 :
        return print( "Media " + str(media) +" Passou direto!!"  )
    elif media >5:
        return print("Media " + str(media) + " Ficou de recuperacao.")
    else:
        return print("Media " + str(media) +" Ficou reprovado.")

        
resultado(7,8.5,6.5)        