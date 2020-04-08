# -*- coding:utf-8 -*-
# Fichier : python exo_djangogirls_2_4.py
# Dossier : C:\Users\User\Desktop\exo-djangogirls

# Introduction au langage Python

# Les boucles

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
    hi(name)
    print('Next girl :')

print()

# Fonction range s'utilise avec des nombres
for i in range(1, 6):
    print(i)

