from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# form para el registro de usuario
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields= ['username', 'email', 'first_name', 'last_name', 'password1','password2']
        

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe prueba con otro.")
        return email