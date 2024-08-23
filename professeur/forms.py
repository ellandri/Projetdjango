    
from django import forms
from .models import Professeur 
class ProfesseurForm(forms.Form):
        Nom = forms.CharField(max_length=10)
        Prenom = forms.CharField(max_length=10)
        genre = forms.CharField(max_length=10)
        Matricule = forms.CharField(max_length=10)
        Prenom = forms.CharField(max_length=10)
        Téléphone = forms.CharField(max_length=10)
        ville = forms.CharField(max_length=10)
        date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

        CHOICES = [
        ('option1', 'Sélectionner une matière'),
        ('option2', 'Mathématique'),
        ('option3', 'Français'),

        ]
    
        choix = forms.ChoiceField(
            choices=CHOICES,
            widget=forms.Select(attrs={'class': 'form-group'})
        )

