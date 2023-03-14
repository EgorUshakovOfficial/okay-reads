from django.forms import ModelForm
from ..models import Review

# Review form
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'comment', 'rating']
