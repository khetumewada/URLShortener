from django import forms
from .models import ShortURL

class ShortenForm(forms.ModelForm):
    custom_url = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter custom short name (optional)",
            "class": "w-full rounded-lg border-gray-300 focus:border-indigo-500 focus:ring focus:ring-indigo-200 px-3 py-2 shadow-sm"
        })
    )

    class Meta:
        model = ShortURL
        fields = ["link", "custom_url"]
        widgets = {
            "link": forms.URLInput(attrs={
                "placeholder": "Paste your long URL here...",
                "class": "w-full rounded-lg border-gray-300 focus:border-indigo-500 focus:ring focus:ring-indigo-200 px-3 py-2 shadow-sm"
            }),
        }
