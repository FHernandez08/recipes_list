from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

recipe_list ={
    "Baked Garlic Parmesan Chicken": "Breaded chicken breasts flavored with garlic and Parmesan cheese are baked until golden and crispy for the easiest chicken dish ever. Serve with a salad and pasta for a quick, scrumptions dinner.",
    "Soy Honey_Glazed Salmon with Asparagus": "This lovely meal with salmon, asparagus, and rice is made with few ingredients. Serve with your choice of grain and other veggies if desired. This recipe is easy to double for large families.",
    "Shrimp Scampi with Pasta": "Shrimp scampi with linguine is the ultimate seafood pasta dish. Works with any pasta; angel hair is less filling.",
    "Asian Glazed Chicken Thighs": "These Asian chicken thighs are slightly spicy but the sweetness tames the heat. Delicious served with rice.",
    "Vegan Sweet Potato Chickpea Curry": "This sweet potato chickpea curry is a yummy vegan dish. Served with basmati rice and naan bread."
}

# Create your views here.
def index(request):
    list_items = ""
    recipes = list(recipe_list.keys())

    return render(request, "recipe/index.html", {
        "recipes": recipes
    })


def recipe_items_by_number(request, recipe):
    recipes = list(recipe_list.keys())

    if recipe > len(recipes):
        return HttpResponseNotFound("This recipe is not found on this website.")
    
    redirect_recipe = recipes[recipe - 1]
    redirect_path = reverse("recipe", args=[redirect_recipe])
    return HttpResponseRedirect(redirect_path)


def recipe_items(request, recipe):
    try:
        recipe_text = recipe_list[recipe]
        return render(request, "recipe/templates/recipe.html", {
            "text": recipe_text,
            "recipe": recipe
        })
    except:
        raise Http404