from django.shortcuts import render
from django.http import HttpResponse

from collections import defaultdict

recipe_list ={}

recipe_list["name"] = [
    "Baked Garlic Parmesan Chicken",
    "Soy Honey-Glazed Salmon with Asparagus",
    "Shrimp Scampi with Pasta",
    "Asian Glazed Chicken Thighs",
    "Vegan Sweet Potato Chickpea Curry"
]
recipe_list["description"] = []
recipe_list["ingredients"] = []
recipe_list["instructions"]= []

# Create your views here.
def index(request):
    return

def recipe_items_by_number(request):
    return

def recipe_items(request):
    return