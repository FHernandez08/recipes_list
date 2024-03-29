from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item>", views.recipe_items_by_number),
    path("<str:item>", views.recipe_items, name="recipe-list")
]
