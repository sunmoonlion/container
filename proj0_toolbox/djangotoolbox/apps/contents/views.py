from django.shortcuts import render
from django.views import View

class IndexView(View):
    """首页广告"""

    def get(self, request):
        """提供首页"""
        return render(request, 'index.html')