from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
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
        if len(username) < 6 or len(password) < 6:
            messages.warning(request,f"Kullanıcı adınız ya da parolanız geçersiz...")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,f" Heey! {request.user.username} Hoşgeldin!")
            return redirect("home_view")
        elif len(password) > 6 and user==None:
            messages.warning(request,f"Bir şeyler yanlış görünüyor!")

      


    return render(request,"user_profile/login.html",context)

def logout_view(request):
    messages.info(request,f" Heey! {request.user.username} Oturumun Sonlandı")
    logout(request)
    return redirect("/")