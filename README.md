This project will be a similar construction to the monthly challenges project that was created from the Django course I am currently taking.

The recipes list project is created to practice the topics learned in the course and throghout the project:
  1. URLs
  2. Views
  3. Templates
  4. Static Files

The goal for this project is to have a full grasp of the 4 topics listed above, by implementing my own version of the 4 topics, and being able to get a successful Django project.

Completing this project, I encountered two problems,
  1. not having the proper URL for the proper view
  2. not having the data on the template appearing for the view

  To correct the first problem, I had to correct the name for the url path in the apps urls.py file to show the right view for the site.
    path("<str:item>", views.recipe_items, name="recipe-list") <= using this name for the url path, was able to connect the views.py file for the app to the template

    <li><a href="{% url 'recipe-list' recipe %}">{{ recipe|title }}</a></li> <= the template was able to recognize the url and display the function for the views, which was a group of links
  To correct the second problem, we changed the values in the arguments for the render function which was able to display the specific view for the website once the link for the url for that specific view was clicked.
    def recipe_items(request, item):
    try:
        recipe_text = recipe_list[item]
        return render(request, "recipe/recipe.html", {
            "text": recipe_text,
            "recipe": item   <= this is what needed to be fixed because it was giving an error
        })
    except:
        raise Http404()
