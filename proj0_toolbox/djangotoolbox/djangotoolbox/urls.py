"""
URL configuration for djangotoolbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # users
    path('', include('users.urls',namespace='users')),
    # contents
    path('', include('contents.urls',namespace='contents')),
    # verifications
    path(r'', include('verifications.urls')),
    # areas
    path(r'', include('areas.urls')),
]
# 开发时访问媒体资源，这不同于静态文件的访问机制（静态文件通过配置staticfiles_dirs来查找静态文件）
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

