from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["first_name", "last_name", "company", "email",
                  "cell", "country", "comment"]
        widgets = {
            "first_name" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            "company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            "cell": TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),

        }

