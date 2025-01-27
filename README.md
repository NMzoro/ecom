# Ecommerce Django Rest Framework API

## Description

Ce projet est une API Django Rest Framework (DRF) pour un site e-commerce, permettant de gérer les entités suivantes :
- Clients
- Produits
- Commandes
- Factures

Les utilisateurs peuvent s'authentifier, ajouter des produits, passer des commandes, et générer des factures. L'API RESTful est sécurisée et utilise l'authentification de base.

## Prérequis

- Python 3.x
- Django 3.x ou supérieur
- Django Rest Framework (DRF)

## Installation

1. Clonez ce repository :

   ```bash
   git clone https://github.com/NMzoro/ecom.git
   cd ecommerce
- Créez le fichier de migration de la base de données et appliquez-le :
   ```bash
  python manage.py makemigrations
  python manage.py migrate


- Créez un superutilisateur pour accéder à l'interface d'administration (facultatif) :
   ```bash
  python manage.py createsuperuser

- Lancez le serveur de développement :
   ```bash
  python manage.py runserver

- Structure du projet

    ecommerce/ : Dossier principal du projet Django
        api/ : Application principale de l'API
            models.py : Définit les modèles Client, Produit, Commande, Facture
            serializers.py : Sérialise les modèles pour l'API
            views.py : Contient les vues API utilisant DRF ViewSets
            urls.py : Routes de l'API
        ecommerce/ : Paramètres du projet
            settings.py : Paramètres de configuration du projet, y compris DRF
            urls.py : Routes du projet, incluant celles de l'API

Endpoints

    POST /api/clients/ : Créer un client
    GET /api/clients/ : Liste des clients
    GET /api/clients/{id}/ : Détails d'un client
    PUT /api/clients/{id}/ : Mettre à jour un client
    DELETE /api/clients/{id}/ : Supprimer un client
    POST /api/produits/ : Créer un produit
    GET /api/produits/ : Liste des produits
    GET /api/produits/{id}/ : Détails d'un produit
    POST /api/commandes/ : Créer une commande
    GET /api/commandes/ : Liste des commandes
    GET /api/commandes/{id}/ : Détails d'une commande
    POST /api/factures/ : Créer une facture
    GET /api/factures/ : Liste des factures
    GET /api/factures/{id}/ : Détails d'une facture
Authentification

L'API utilise l'authentification de base, où chaque utilisateur doit se connecter pour accéder aux données. Vous pouvez tester l'API en utilisant un outil comme Postman avec les informations d'identification de votre superutilisateur.
Exemple d'authentification avec Postman :

    Méthode : GET ou POST
    URL : http://127.0.0.1:8000/api/clients/
    Dans l'onglet Authorization, choisissez Basic Auth et entrez vos informations de superutilisateur.
