# -*- coding:utf-8 -*-
# Fichier : python exo_djangogirls_2_3.py
# Dossier : C:\Users\User\Desktop\exo-djangogirls

# Introduction au langage Python

# Vos propres fonctions

def hi():
    print("Hi there !")
    print("How are you motherfucker ?")

hi()

print()

def hi(name): # on ajoute un paramètre à la fonction
    if name == 'Ola':
        print("Hi Ola !")
    elif name == 'Sonja':
        print("Hi Sonja !") 
    else:
        print('Hi anonymous !')

hi("Ola")
hi("Sonja")
hi("Herbert")

print()

def hi(name):
    print('Hi ' + name + '!')
hi('Rachel')

