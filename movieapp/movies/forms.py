from django import forms
from .models import Comment
from django.forms import widgets

class CommentForm(forms.ModelForm):
    class Meta:
        numbers = (
            ('1', '1 Star'),
            ('2', '2 Stars'),
            ('3', '3 Stars'),
            ('4', '4 Stars'),
            ('5', '5 Stars'),
        )
        model = Comment
        # field = ['full_name', 'email', 'text', 'rating']
        exclude = ['movie', 'date_added',]
        labels = {
            "full_name": "Name Surname",
            "email": "Email",
            "text": "Comment",
            "rating": "Score"
        }
        widgets = {
            "full_name": widgets.TextInput(attrs={"class":"form-control"}),
            "email": widgets.EmailInput(attrs={"class":"form-control"}),
            "text": widgets.Textarea(attrs={"class":"form-control"}),
            "rating": widgets.Select(attrs={"class":"form-control custom-select"},choices=numbers),
        }