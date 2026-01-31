from django.shortcuts import render
from .forms import MealForm
from google import genai
# Create your views here.
def meal_view(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            # Process the form data here
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            meal_type = form.cleaned_data['meal_type']
            location = form.cleaned_data['location']
            meal_purpose = form.cleaned_data['meal_purpose']
            # You can add your logic to handle the data here
            prompt = f"I am a {age} year old person, weighing {weight} kg and {height} cm tall. I want a {meal_type} meal for {meal_purpose} in {location}. Give me a weekily meal plan.Generate a table with days as row and breakfast, lunch, dinner as columns. Also include a grocery list. Genertae only table tags and its elements not html"
            client = genai.Client(api_key="AIzaSyAzvx390EwBis0NbkmV7gzLm5ua4rlHPJY")
            response = client.models.generate_content(model = "gemini-2.5-flash",contents = prompt)

            return render(request, 'meal_form.html', {'form': form, 'response': response.text})
    else:
        form = MealForm()

    return render(request, 'meal_form.html', {'form': form})