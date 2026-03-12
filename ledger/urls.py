from django.urls import path
from . import views

app_name = 'ledger'

urlpatterns = [
    path('recipe/', views.recipe_list, name='recipe-list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipe/add/', views.RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image/', views.RecipeImageCreateView.as_view(), name='recipe-add-image'),
]