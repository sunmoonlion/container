
# from .views import RegisterView
from django.urls import path, re_path

from . import views
app_name = 'users'
urlpatterns = [
    # 用户注册: reverse(users:register) == '/register/'
    path(r'register/', views.RegisterView.as_view(), name='register'),
    # 判断用户名是否重复注册
    re_path(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$', views.UsernameCountView.as_view()),
    # 判断用户名是否重复注册
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # 用户登录
    path(r'login/', views.LoginView.as_view(), name='login'),
    # 用户退出登录
    path(r'logout/', views.LogoutView.as_view(), name='logout'),
    # 用户中心
    path(r'info/', views.UserInfoView.as_view(), name='info'),
]