from django.urls import path
from .views import recipe_list, recipe

app_name = "ledger"

urlpatterns = [
    path("recipes/", recipe_list, name="recipe-list"),
    path("recipe/<str:name>/", recipe, name="recipe"),
]