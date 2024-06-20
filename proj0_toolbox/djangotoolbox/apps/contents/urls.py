from django.urls import path

from . import views

app_name = 'contents'
urlpatterns = [
    # 首页: '/'
    path(r'', views.IndexView.as_view(), name='index'),
]