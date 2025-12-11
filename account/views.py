from django.shortcuts import render

from account.forms import RegistrationForm


def register(request):
    form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})
