from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

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

def register_view(request):
    context=dict()
    if request.method == "POST":
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        twitter = post_info.get('twitter')
        if email != email_confirm:
            messages.warning(request,"Email adresleri Eşleşmedi...")
            return redirect ("user:register_view")
        if password != password_confirm:
            messages.warning(request,"Şifreler Eşleşmedi...")
            return redirect ("user:register_view")
        if len(email) < 3 or len(password) < 3 or len(first_name) < 3 or len(last_name) < 3:
            messages.warning(request,"Minimum karakter sayısını tamamlamalısınız...")
            return redirect ("user:register_view")

        user,created = User.objects.get_or_create(username=email)
        if not created:
            user = authenticate(request,username=email,password=password)
            if user is not None:
                messages.warning(request,"Daha önce kayıt olmuşsunuz... Ana Sayfaya Yönlendirildiniz...")
                login(request,user)
                return redirect("/")
        messages.warning(request,"Bu e-posta adresi zaten kayıtlı...")
        return redirect ("user:login_view")

    return render(request,"user_profile/register.html",context)
            


