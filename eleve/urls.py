from django.urls import path
from dashbord.views import index
from . import views
app_name='eleve'
urlpatterns = [
   path('eleve/', views.eleve, name='index'),
   path('ajouter/', views.ajouter_eleve_view, name='add'),
    path('modifier/', views.modifier_eleve_view, name='edit'),

    
    
]