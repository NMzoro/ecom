from rest_framework import serializers
from .models import Client, Produit, Commande, LigneCommande, Facture

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class LigneCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneCommande
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    lignes = LigneCommandeSerializer(source='lignecommande_set', many=True, read_only=True)

    class Meta:
        model = Commande
        fields = ['id', 'client', 'date_commande', 'statut', 'lignes']

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'