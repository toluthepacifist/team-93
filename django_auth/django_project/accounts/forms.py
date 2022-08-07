from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;', 'class': 'form-control',}))
    last_name = forms.CharField(label="Last Name", max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(label="Username", max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(label="Email", required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(label="Password", max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(label="Confirm", max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class':'email-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'password-input'}))
    
    class Meta:
            model = User
            fields = ['email', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist, please <a href="/sign up">register</a>')
            if not user.check_password(password):
                raise forms.ValidationError('You have entered the wrong password. <a href="#">Did you forget your password?</a>')
            if not user.is_active:
                raise forms.ValidationError('This account is not active. Please <a href="#">contact support</a>')
            return super(LoginForm, self).clean(*args, **kwargs)
