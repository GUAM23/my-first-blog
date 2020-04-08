# -*- coding:utf-8 -*-
# Fichier : python exo_djangogirls_4_1.py
# Dossier : C:\Users\User\Desktop\exo-djangogirls
# Activer environnement virtuel : myvenv\Scripts\activate

# Introduction au langage Python

# Votre premier projet Django (43)

# Se placer dans le virtualenv, on va créer le dossier mysite (ainsi que le fichier manage.py) en tapant la commande suivante (ne pas oublier le point) : 
# django-admin startproject mysite .

# Dans le dossier mysite, settings contient la configuration du site web et urls.py contient une liste de patterne d'URL utilisés par urlresolver.

# Dans le fichier settings, on change la ligne TIME_ZONE = 'UTC' en TIME_ZONE = 'Europe/Paris'

# Dans le même fichier, on ajoute la ligne suivante à la fin du fichier : STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# On va utiliser sqlite3 comme gestionnaire de base de données.

# On va créer la base de données de notre blog (en se placant dans le dossier contenant le fichier manage.py) en tapant la commande suivante dans la console : python manage.py migrate

# Il nous suffit ensuite de lancer le serveur et voir si le site fonctionne, on tape (toujours dans le dossier contenant le fichier manage.py) : python manage.py runserver 

# Le blog s'affiche dans le navigateur : http://127.0.0.1:8000/
# On appuie sur Ctrl + C pour arrêter le serveur

