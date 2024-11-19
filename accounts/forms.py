from django import forms

class LoginUserForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    cpf = forms.CharField(max_length=11)  # ou use o campo "CPF" apropriado