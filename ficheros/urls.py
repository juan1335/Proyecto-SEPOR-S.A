from django.urls import path
from . import views

urlpatterns = [
    path('listficheros/compramatprima/', views.listcomatprima, name='compramatpr'),
    path('listficheros/materiapr/', views.listmatprima, name='materiaprima'),
    path('listficheros/listfabricacion/', views.listfabricaciones, name='listafabricacion'),
    path('listficheros/formulas/', views.listformulas, name='formulas'),
    path('listficheros/formdepago/', views.listformpagos, name='formapago')
]