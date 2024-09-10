from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login_page/',views.login_page,name='login_page'),
    path('register_page/',views.register_page,name="register_page"),
    path('search_page/',views.search_page,name="search_page"),
    path('logout/', views.logout_page, name='logout_page'),
    path('profile/',views.profile_page,name='profile_page'),
    path('about/',views.about_page,name='about_page')

]
