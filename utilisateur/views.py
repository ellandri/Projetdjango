from django.shortcuts import render
from .forms import  UtilisateurForm

# Create your views here.
def utilisateur_view(request):
    return render(request, 'html/utilisateur.html')

def modifier_utilisateur_view(request):
    return render(request, 'html/modifier_utilisateur.html')

def ajouter_utilisateur_view(request):
    form = UtilisateurForm()
    return render(request, 'html/ajouter_utilisateur.html', {'form': form})
