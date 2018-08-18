from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from .forms import CustomUserCreationForm


### see https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            print("invalid form",email)
            print("email ",email)
            print("raw_password",raw_password)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
