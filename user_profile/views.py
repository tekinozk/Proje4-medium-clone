from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

def login_view(request):
    # login olan user direkt olarak anasayfaya gidebilmeli
    context = dict(
    ) 
    if request.user.is_authenticated:
        messages.success(request,f" Heey! {request.user.username} daha önce giriş yapmıştınız")
        return redirect("home_view")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,f" Heey! {request.user.username} Hoşgeldin!")
            return redirect("home_view")
        else:
            messages.warning(request,f" Heey! {request.user.username} Bir şeyler yanlış görünüyor!")


    return render(request,"user_profile/login.html",context)