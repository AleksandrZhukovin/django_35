from django.shortcuts import render, redirect

from account.forms import RegistrationForm
from account.models import User


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return redirect('login/')
    return render(request, 'account/register.html', {'form': form})
