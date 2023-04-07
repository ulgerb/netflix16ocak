from django.shortcuts import render

# Create your views here.


def profilePage(request):
   context = {}
   return render(request, 'user/profile.html', context)


def accountPage(request):
   context = {}
   return render(request, 'user/hesap.html', context)


def loginUser(request):
   context = {}
   return render(request, 'user/login.html', context)


def registerUser(request):
   context = {}
   return render(request, 'user/register.html', context)
