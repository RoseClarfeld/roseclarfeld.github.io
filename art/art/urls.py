"""art URL Configuration

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
# art/urls.py
from django.conf.urls import url
from welcome import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^biography/$', views.BiographyPageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
    url(r'^paintings/$', views.PaintingsPageView.as_view()),
    url(r'^index/$', views.HomePageView.as_view())
]
