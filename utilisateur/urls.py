from django.urls import path
from dashbord.views import index
from . import views
app_name='utilisateur'
urlpatterns = [
   path('utilisateur/', views.utilisateur_view, name='index'),
    path('ajouteru/', views.ajouter_utilisateur_view, name='add'),
    path('modifieru/', views.modifier_utilisateur_view, name='edit'),
    
]

