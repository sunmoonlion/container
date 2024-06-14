
# from .views import RegisterView
from django.urls import path, re_path

from . import views
app_name = 'users'
urlpatterns = [
    # 用户注册: reverse(users:register) == '/register/'
    path(r'register/', views.RegisterView.as_view(), name='register'),
]