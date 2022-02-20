from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name="home"),
    path('student/create/', views.StudentCreate.as_view(), name='create-student'),
    # path('student/list/', views.StudentList.as_view(), name='create-student'),
    # path('student/update/<int:id>', views.StudentUpdate.as_view(), name='create-student'),

]
