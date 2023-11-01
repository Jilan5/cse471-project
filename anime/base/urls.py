from django.urls import path
from . import views


urlpatterns=[
   
    path('',views.Home,name="home"),

    path('profile/<str:pk>',views.userProfile, name="user-profile"),
    path('update-user/',views.updateUser,name='update-user'),
]