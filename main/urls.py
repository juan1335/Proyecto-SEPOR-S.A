from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('listficheros/', views.listficheros, name='ficheros'),
    path('compmateriapr/', views.materiaprima, name='materiapr'),
    path('fabricacion/', views.fabricacion, name='fabricacion'),
    path('entinventario/', views.entinvetario, name='entinventario'),
    path('escalloform/', views.escalloforma, name='escandallo'),
    path('mantenimiento/', views.mantficheros, name='mantficheros'),
]