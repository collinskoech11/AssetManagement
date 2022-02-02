from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def SignIn(request):
    if request.user.is_authenticated:
        return render(404)
    else:
        return render(request, 'SignIn.html')
    

def index(request):
    return render(request, 'index.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

def logout(request):
    return render(request, 'logout.html')

def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, Your account was created successfully')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'Register.html', {'form':form})