"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url='home/', permanent=False), name='index'),
    path('men/', include('men.urls')),
    path('kids/', include('kids.urls')),
    path('women/', include('women.urls')),
    path('accessories/', include('accessories.urls')),
    path('contactus/', include('contactus.urls')),
    path('single/', include('single.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
