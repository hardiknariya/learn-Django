from django.urls import path, include
from account import views

app_name = 'home'
urlpatterns = [
    path('', views.Index.as_view(), name="user-list"),
    path('register/', views.UserRegister.as_view(), name='user-register'),
    path('login/', views.UserLogin.as_view(), name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),

]

