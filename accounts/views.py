from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import LoginUserForm 

@login_required
def private_page_1(request):
    return render(request, "accounts/private_page_1.html")

@login_required
def private_page_2(request):
    return render(request, "accounts/private_page_2.html")

