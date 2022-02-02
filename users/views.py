from django.shortcuts import render

# Create your views here.
def SignIn(request):
    return render(request, 'SignIn.html')
    

def index(request):
    return render(request, 'index.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

def logout(request):
    return render(request, 'logout.html')

def Register(request):
    return render(request, 'Register.html')