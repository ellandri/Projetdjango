from django.urls import path
from dashbord.views import index
from . import views
app_name='professeur'
urlpatterns = [
   path('professeur/', views.professeur, name='index'),
   path('ajouterp/', views.ajouter_professeur_view, name='add'),
    path('modifierp/', views.modifier_professeur_view, name='edit'),

    
]