from django.urls import path
from . import views

urlpatterns= [
    path('',views.homepageview,name="home"),
    path('about',views.aboutpageview,name="about"),
    path('contact',views.contactpageview,name="contact"),
    path('form',views.myform,name="myform"),
    path('formprocess',views.process,name="process"),
    path('signup',views.signup,name="signup"),
    path('signup_page',views.page,name="page"),
    path('registration',views.registration,name="registration"),
    path('slist',views.studentlist.as_view(),name='s1')
]
