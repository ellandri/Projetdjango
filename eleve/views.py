from django.shortcuts import render
from .forms import EleveForm

# Create your views here.
def eleve(request):
    return render(request, 'html/eleve.html')

def ajouter_eleve_view(request):
    form = EleveForm()
    
    return render(request, 'html/ajouter_eleve.html', {'form': form})

def modifier_eleve_view(request):
    return render(request, 'html/modifier_eleve.html')

