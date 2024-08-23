from django.shortcuts import render

# Create your views here.
def rapport_view(request):
    return render(request, 'html/rapport.html')