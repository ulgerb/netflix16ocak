from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def profilePage(request):
   
   context = {}
   return render(request, 'user/profile.html', context)


def accountPage(request):
   context = {}
   return render(request, 'user/hesap.html', context)


def loginUser(request):

   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password") 
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
         login(request, user)
         messages.success(request, "Hoş geldiniz")
         return redirect('profilePage')
      else:
         messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
         return redirect('loginUser')
         
   
   context = {}
   return render(request, 'user/login.html', context)


def registerUser(request):

   if request.method == "POST":
      fname = request.POST.get("fname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      
      if password1==password2:
         if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
               user = User.objects.create_user(username=username, password=password1, first_name=fname, email=email)
               user.save()
               messages.success(request, "Kaydınız Başarıyla Oluşturuldu..")
               return redirect("loginUser")
            else:
               messages.warning(request, "Bu Email adresi sitemize kayıtlı!")
               hata = "email"
               # return redirect('registerUser')
         else:
            messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor!")
            hata = "username"
            # return redirect('registerUser')
      else:
         messages.warning(request, "Şifreler aynı değil!")
         hata = "password"
         # return redirect('registerUser')
      context = {}
      if hata == "email":
         context.update({
            "fname":fname,
            "username": username,
            "password1": password1,
            "hata" : hata,
         })
      elif hata == "username":
         context.update({
            "fname":fname,
            "email": email,
            "password1": password1,
            "hata" : hata,
         })
      elif hata == "password":
         context.update({
             "fname": fname,
             "username": username,
             "email": email,
             "hata": hata,
         })
         
      
      return render(request, 'user/register.html', context)
   
   context = {}
   return render(request, 'user/register.html', context)
