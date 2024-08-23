from django.urls import path
from dashbord.views import index
from . import views
app_name='rapport'
urlpatterns = [
   path('rapport/', views.rapport_view, name='rapport'),
    
    
]