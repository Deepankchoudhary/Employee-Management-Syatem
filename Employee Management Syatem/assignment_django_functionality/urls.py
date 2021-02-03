from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.signin,name="login"),
    path('signup/',views.signup,name="signup"),
    path('home/',views.home,name="home"),
    path('testapp/', include('testapp.urls')),
    path('logout/',views.signout,name="logout"),

]
