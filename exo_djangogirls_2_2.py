# -*- coding:utf-8 -*-
# Fichier : python exo_djangogirls_2_2.py
# Dossier : C:\Users\User\Desktop\exo-djangogirls

# Introduction au langage Python

# if elif else

if 3 > 2:
    print('Ca marche ma gueule !')

print() # saut de ligne

if 5 > 2:
    print('5 est toujours plus grand que 2')
else:
    print('5 n\'est pas plus grand que 2')

print()

name = 'Sonja'

if name == 'Ola':
    print("Hey Ola !")
elif name == 'Sonja':
    print("Hey Sonja !") 
else:
    print('Hey anonymous !')

print()

volume = 97 # changer le volume

if volume < 20:
    print("C'est plutôt calme.")
elif 20 <= volume < 40:
    print("Une jolie musique de fond.")
elif 40 <= volume < 60:
    print("Parfait, je peux entendre toute les détails de la musique.")
elif 60 <= volume < 80:
    print("Sympa pour faire la fête !")
elif 80 <= volume < 100:
    print("Moins fort la musique !")
else:
    print("Appelez les Hendeks !")
