from django import forms
from .models import ProductReview

class ProductReviewForms(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"write Review"}))

    class Meta:
        model = ProductReview
        fields = ['review','rating']