"""rentalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.index),
    path('Register', views.Register),
    path('Sale', views.sale),
    path('Revenue', views.Revenue),
    path('Payment', views.ConfirmPayment),
    path('PaidHouses', views.PaidHouses),
    path('UnpaidHouses', views.UnpaidHouses),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html')),
    path('SignIn',auth_view.LoginView.as_view(template_name='SignIn.html')),
    path('Dashboard/index', views.Dashboard),
]
