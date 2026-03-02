from django.shortcuts import render, get_object_or_404
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {
        "recipes": recipes
    })


def recipe(request, name):
    recipe = get_object_or_404(Recipe, name=name)
    return render(request, "ledger/recipe_detail.html", {
        "recipe": recipe
    })