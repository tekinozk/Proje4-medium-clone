from django.urls import path
from user_profile.views import login_view,logout_view,register_view


app_name = "user"
urlpatterns = [
    path('login/', login_view,name="login_view"),
    path('logout/', logout_view,name="logout_view"),
    #REGISTER:
    path('register/', register_view,name="register_view"),
]
