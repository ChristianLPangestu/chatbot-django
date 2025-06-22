from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CustomLoginForm(forms.Form):
    username  = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username or email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )

    def clean(self):
        email_or_username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if not email_or_username or not password:
            return self.cleaned_data

        # Cari user berdasarkan username atau email
        user = User.objects.filter(username=email_or_username).first()
        if not user:
            user = User.objects.filter(email=email_or_username).first()

        if not user:
            self.add_error('username ', 'Username or email not found.')
            return self.cleaned_data

        auth_user = authenticate(username=user.username, password=password)
        if auth_user is None:
            self.add_error('password', ' Incorrect password.')
        else:
            self.user = auth_user

        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)
    
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password1', "Passwords do not match.")
            self.add_error('password2', "Passwords do not match.")