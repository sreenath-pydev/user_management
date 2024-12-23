from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
# signup
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

# login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'input',
        'placeholder' : 'Username',
        'id' : 'username',
    }))

    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class' : 'input',
        'placeholder' : 'Password',
        'id' : 'password',
    }))

# password reset
class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'placeholder': 'Enter your email',
            'required': 'required',
        })
    )

# password change
class NewPasswordForm(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Enter your new password',
            'required': 'required',
        }),
        validators=[validate_password],  # Add Django's password validators
        error_messages={
            'required': 'Password is required.',
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Confirm your new password',
            'required': 'required',
        }),
        error_messages={
            'required': 'Confirmation password is required.',
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Passwords do not match.')