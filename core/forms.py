# from django import forms
# from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     email = forms.EmailField(required=True)
#     cpf = forms.CharField(max_length=11, required=True)
#     senha = forms.CharField(widget=forms.PasswordInput, required=True)

# class CadastroForm(forms.ModelForm):
#     senha = forms.CharField(widget=forms.PasswordInput, required=True)
#     senha_confirmacao = forms.CharField(widget=forms.PasswordInput, required=True)
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username']  # username será o CPF, ou o que for usar como nome de usuário
    
#     def clean(self):
#         cleaned_data = super().clean()
#         senha = cleaned_data.get('senha')
#         senha_confirmacao = cleaned_data.get('senha_confirmacao')

#         if senha != senha_confirmacao:
#             raise forms.ValidationError('As senhas não coincidem.')
        
#         return cleaned_data


from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'celular', 'date', 'email', 'sexo']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    cpf = forms.CharField(label='CPF', max_length=11)




    



    