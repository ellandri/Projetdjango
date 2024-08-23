from django.shortcuts import render
from .forms import ProfesseurForm

# Create your views here.
def professeur(request):
    return render(request, 'html/professeur.html')

def ajouter_professeur_view(request):
    form = ProfesseurForm()

    return render(request, 'html/ajouter_professeur.html', {'form': form})

def modifier_professeur_view(request):
    return render(request, 'html/modifier_professeur.html')

