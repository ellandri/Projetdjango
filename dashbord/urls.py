from django.urls import path
from dashbord.views import index
from . import views
app_name='dashboard'
urlpatterns = [
   path('dashbord', views.index, name='index'),
    path('', views.connect_view, name='connect'),

    
]