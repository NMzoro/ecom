from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    adresse = models.TextField()
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('EN_COURS', 'En cours'),
        ('LIVREE', 'Livrée'),
        ('ANNULEE', 'Annulée'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')
    produits = models.ManyToManyField(Produit, through='LigneCommande')

    def __str__(self):
        return f"Commande {self.id} - {self.client}"

class LigneCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produit.nom} ({self.quantite})"

class Facture(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    date_facturation = models.DateTimeField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    payee = models.BooleanField(default=False)

    def __str__(self):
        return f"Facture {self.id} - Commande {self.commande.id}"
