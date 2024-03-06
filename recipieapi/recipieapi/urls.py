"""
URL configuration for recipieapi project.

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
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from recipie import views

router=SimpleRouter()

from rest_framework.authtoken import views as rviews         #import aliasing

router.register('recipie',views.Recipiedetail)
router.register('review',views.Reviewrating)
router.register('user',views.CreateUser)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('recipie', views.Recipiedetail.as_view()),
    path('api-token-auth/',rviews.obtain_auth_token),       #login view
    path('search/',views.search.as_view()),
]
