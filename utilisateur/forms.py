    
from django import forms
from .models import Utilisateur 

class UtilisateurForm(forms.Form):
        Pseudo = forms.CharField(max_length=10)
        Mot_de_passe = forms.CharField(max_length=100)
        Confirmer_mot_de_passe = forms.CharField(max_length=10)
