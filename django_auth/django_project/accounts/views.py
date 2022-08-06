from django.shortcuts import render, redirect #old codes
from django.urls import reverse_lazy #old codes
from django.contrib import messages #old codes
from django.views import View
from django.contrib.auth import login, authenticate

from .forms import UserRegistrationForm
from .forms import LoginForm


class SignUpView(View):
    form_class = UserRegistrationForm #old codes
    success_url = reverse_lazy("login") #old codes
    initial = {'key': 'value'}
    template_name = 'registration/sign up.html' #old codes

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/login')

        return render(request, self.template_name, {'form': form})
    
    class LogInView(View):
        form_class = LoginForm
        success_url = reverse_lazy("home")
        initial = {'key': 'value'}
        template_name = 'registration/login.html'
    
        def login(request):
            form = LoginForm(request.POST or None)
            if form.is_valid():
                    email = form.cleaned_data.get('email')
                    password = form.cleaned_data.get('password')
                    user = authenticate(email=email, password=password)
                    login(request, user)
                    return redirect('home')

            context = {
                    'form':form,
            }
            return render(request, "login.html", context)
# Create your views here.
