from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Contact

User = get_user_model()
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exculde = ['timestamp']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4,
                'cols': 15,
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none',
                'placeholder': 'Enter your message...',
            }),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'w-full bg-white border-none focus:outline-none',
            'placeholder': 'Enter username or email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full bg-white border-none focus:outline-none',
            'placeholder': 'Enter your password'
        })

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your e-mail'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['password1'].widget.attrs[
            'placeholder'] = 'Enter a strong password'
        self.fields['password2'].widget.attrs[
            'placeholder'] = 'Confirm password'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'That email address is already registered!')
        return email