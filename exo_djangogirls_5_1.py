# -*- coding:utf-8 -*-
# Fichier : python exo_djangogirls_5_1.py
# Dossier : C:\Users\User\Desktop\exo-djangogirls
# Activer environnement virtuel : myvenv\Scripts\activate

# Introduction au langage Python

# Les modèles dans Django (46)

# On vacréer une application (blog et son fichier) en tapant la ligne de commande suivante (toujours dans le dossier contenant le fichier manage.py) : python manage.py startapp blog

# Afin de pouvoir utiliser la nouvelle application, on va ajouter 'blog' dans le fichier mysite/settings

# On copie ensuite le code suivant dans le fichier blog/models.py :

# from django.db import models
# from django.utils import timezone

# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

# Attention !!!
# Remplacer la ligne suivante : author = models.ForeignKey('auth.User')
# par author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

# On va ensuite ajouter notre nouveau modèle à notre base de données en tapant la ligne de commande suivante : 
# python manage.py makemigrations blog

# Tapez ensuite la ligne de commande suivante : python manage.py migrate blog

# Ensuite on tape le code suivant dans le fichier blog/admin.py :
# from django.contrib import admin
# from .models import Post

# admin.site.register(Post)

# On tape ensuite pour voir le résultat : myvenv\Scripts\activate 
# Puis http://127.0.0.1:8000/admin/

# On tape Ctrl + c pour reveniren mode console. On va créer un superuser, on tape donc : python manage.py createsuperuser
# nom utilisateur : flores
# adresse mail : guancavilca@gmail.com 
# mot de passe : poilu2310

# On retourne dans l'interface d'administration en tapant : python manage.py runserver 
# Puis http://127.0.0.1:8000/admin/

# Pas réussit à entrer dans l'interface d'administration !