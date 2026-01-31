from django import forms

class MealForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0)
    weight = forms.FloatField(label='Weight (kg)', min_value=0)
    height = forms.FloatField(label='Height (cm)', min_value=0)
    meal_type = forms.ChoiceField(
        label='Meal Type',
        choices=[
            ('vegitarian', 'Vegetarian'),
            ('non_vegitarian', 'Non-Vegetarian'),
            ('vegan', 'Vegan'),
        ])
    location = forms.CharField(label='Location', max_length=100)
    meal_purpose = forms.ChoiceField(
        label='Meal Purpose',
        choices=[
            ('weight_loss', 'Weight Loss'),
            ('muscle_gain', 'Muscle Gain'),
            ('maintenance', 'Maintenance'),
        ])
    
