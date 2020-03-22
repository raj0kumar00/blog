from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.signin,name='signin'),
    path('register/',views.register,name="register"),
    path('logout/',views.Logout,name='logout'),
    path('test',views.test,name='test'),
    path('UsernameChecker',views.UsernameChecker,name="UsernameChecker"),
    path('post/<slug:slug>/',views.post_detail,name="post_detail"),
    path('create/',views.createpost,name="createpost"),
    path('search/',views.search,name='search'),
    path('result/',views.search,name='result'),
]