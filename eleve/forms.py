    
from django import forms
from .models import Eleve  # Assurez-vous que cela correspond à votre fichier models.py

class EleveForm(forms.Form):
        Nom = forms.CharField(max_length=10)
        Prenom = forms.CharField(max_length=10)
        genre = forms.CharField(max_length=10)
        Matricule = forms.CharField(max_length=10)
        Prenom = forms.CharField(max_length=10)
        Téléphone = forms.CharField(max_length=10)
        ville = forms.CharField(max_length=10)
        date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

        CHOICES = [
        ('option1', 'Tle'),
        ('option2', '1ere'),
        ('option3', '2nd'),

        ]
    
        choix = forms.ChoiceField(
            choices=CHOICES,
            widget=forms.Select(attrs={'class': 'form-group'})
        )

