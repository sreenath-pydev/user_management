from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from .forms import SignupForm, LoginForm, NewPasswordForm
from django.utils.http import urlsafe_base64_decode

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

    def form_invalid(self, form):
        print("Login failed for user:", form.cleaned_data.get('username'))
        response = super().form_invalid(form)
        if form.errors:
            response.context_data['error_message'] = "Invalid username or password."
        return response

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('dashboard')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Home View
def home(request):
    return render(request, 'accounts/home.html')

# Dashboard View
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Password Reset View
def password_reset_view(request):
    error_message = None
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)

                # Generate UID and token
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                # Get current domain
                domain = get_current_site(request).domain
                reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})

                # Full reset link
                reset_link = f'http://{domain}{reset_url}'

                # Send reset email
                send_mail(
                    'Password Reset Request',
                    f'Hello {user.username},\n\nClick the link below to reset your password:\n{reset_link}\n\nIf you did not request this, please ignore this email.',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Password reset link has been sent to your email.')
                return HttpResponseRedirect(reverse('password_reset_done'))
            except User.DoesNotExist:
                error_message = 'No account found with this email address.'
        else:
            error_message = 'Please provide a valid email address.'
    else:
        form = PasswordResetForm()

    return render(request, 'accounts/password_reset.html', {
        'form': form,
        'error_message': error_message,
    })

# Password Reset Confirm View
def password_reset_confirm(request, uidb64=None, token=None):
    error_message = None
    if request.method == 'POST':
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 != password2:
                error_message = "Passwords do not match."
            else:
                try:
                    # Decode the user ID and fetch the user
                    user_id = force_bytes(urlsafe_base64_decode(uidb64))
                    user = User.objects.get(pk=user_id)
                    
                    # Check the token validity
                    if default_token_generator.check_token(user, token):
                        user.set_password(password1)
                        user.save()
                        messages.success(request, 'Your password has been reset successfully.')
                        return redirect('password_reset_complete')
                    else:
                        error_message = "The reset link is invalid or has expired."
                except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                    error_message = "Invalid reset request. Please try again."
        else:
            error_message = "Please correct the errors in the form."
    else:
        form = NewPasswordForm()

    return render(request, 'accounts/password_reset_confirm.html', {
        'form': form,
        'error_message': error_message,
    })
