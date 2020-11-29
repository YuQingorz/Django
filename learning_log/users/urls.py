"""为应用程序users定义URL模式"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [

    # 登录页面
    path('', include('django.contrib.auth.urls')),

    # 注册
    path('register/', views.register, name='register'),
]

