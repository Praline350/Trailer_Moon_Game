from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import messages

from django.conf import settings

from authentication.forms import LoginForm, SignUpForm


class LoginPageView(View):
    template_name = "authentication/login.html"
    login_form_class = LoginForm
    signup_form_class = SignUpForm

    def get(self, request):
        """Handle GET requests: instantiate blank forms for login and sign up."""
        if request.user.is_authenticated:
            return redirect("home")
        login_form = self.login_form_class()
        signup_form = self.signup_form_class()
        context = {
            "login_form": login_form,
            "signup_form": signup_form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        """Handle POST requests: authenticate user or create a new account."""
        login_form = self.login_form_class(request.POST)
        signup_form = self.signup_form_class(request.POST)
        if "login_form" in request.POST:
            if login_form.is_valid():
                user = authenticate(
                    username=login_form.cleaned_data["login_username"],
                    password=login_form.cleaned_data["password"],
                )
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.error(request, "Identifiants Invalides")
        if "signup_form" in request.POST:
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Erreur d'inscription")
        context = {
            "login_form": login_form,
            "signup_form": signup_form,
        }
        return render(request, self.template_name, context=context)

@login_required
def logout_user(request):
    """Log out the user and redirect to the login page."""
    logout(request)
    return redirect("login")

