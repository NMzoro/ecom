from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProduitViewSet, CommandeViewSet, FactureViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'commandes', CommandeViewSet)
router.register(r'factures', FactureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]