from django.urls import path, include
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name="app-home"),

    path('student/', include([
        path('list/', views.StudentList.as_view(), name='list-student'),
        path('create/', views.StudentCreate.as_view(), name='create-student'),
        path('update/<int:pk>', views.StudentUpdate.as_view(), name='update-student'),
        path("delete/<int:pk>", views.StudentDelete.as_view(), name='delete-student')
    ]))

]

