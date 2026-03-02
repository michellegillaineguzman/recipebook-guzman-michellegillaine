from django.urls import path
from . import views

app_name = 'ledger'

urlpatterns = [
    path('', views.recipe_list, name='recipe-list'),
    path('<int:pk>/', views.recipe_detail, name='recipe-detail'),  
]