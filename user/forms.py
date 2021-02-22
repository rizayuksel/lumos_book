from django import forms

#These are login and sign up forms.

class LoginForm(forms.Form): 
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    email = forms.CharField(max_length=100, label="E-Mail")
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Password Again", widget=forms.PasswordInput)

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if (password and confirm and password != confirm): 
            raise forms.ValidationError("Passwords Do Not Match")

        values = { 
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "username": username,
            "password": password
        }
        return values #Send for views.