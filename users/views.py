from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime 
import calendar
from .utils import get_plot
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

# Create your views here.
def SignIn(request):
    if request.user.is_authenticated:
        return render(404)
    else:
        return render(request, 'SignIn.html')
    

def index(request):
    return render(request, 'index.html')


class DashboardAPI(APIView):
    def get(self, request):
        current_user = request.user
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        curr_month = calendar.month_name[currentMonth]
        payment_objects = Payment.objects.filter(username=current_user)
        status_objects = Payment.objects.filter(username=current_user, month=curr_month, year=currentYear )
        house_objects = MyAppUser.objects.filter(user=current_user)
        user_serialiizer = MyAppUserSerializer(current_user)
        payment_serializer = PaymentSerializer(payment_objects)
        current_payment_serializer = PaymentSerializer(status_objects)
        return  Response(user_serialiizer.data, payment_serializer.data, current_payment_serializer.data)  )

@login_required
def Dashboard(request):
    current_user = request.user
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    curr_month = calendar.month_name[currentMonth]
    payment_objects = Payment.objects.filter(username=current_user)
    status_objects = Payment.objects.filter(username=current_user, month=curr_month, year=currentYear )
    house_objects = MyAppUser.objects.filter(user=current_user)
    return render(request, 'Dashboard.html',
        {'payment_objects':payment_objects,'house_objects':house_objects, 'status_objects':status_objects}
    )
@login_required
def PaidHouses(request):
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    curr_month = calendar.month_name[currentMonth]
    paid_objects = Payment.objects.filter(month=curr_month, year=currentYear)
    if request.user.is_superuser:
        return render(request, 'PaidHouses.html', {'paid_objects':paid_objects})
    else:
        return render(404)

def Revenue(request):   
    if request.user.is_superuser:
        return render(request, 'MonthlyRevenue.html')
    
def sale(request):
    qs = Sale.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x,y)
    return render(request, 'sale.html',{'chart': chart})

@login_required
def UnpaidHouses(request):
    if request.user.is_superuser:
        return render(request, 'UnpaidHouses.html')
    else:
        return render(404)


@login_required
def ConfirmPayment(request):
    return render(request, 'Payment.html')

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


