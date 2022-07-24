from django.forms import ModelForm
from .models import Beer, Reviews

class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'brewery']

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['review']