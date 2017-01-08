"""test_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from core.views import UserView, RegisterView, AuthTokenView
from post.views import PostView

router = routers.DefaultRouter()
router.register(r'users', UserView)

schema_view = get_swagger_view(title='Test API Docs')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-docs/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', AuthTokenView.as_view(), name='auth'),
    url(r'^registration/', RegisterView.as_view(), name='registration'),
    url(r'^posts/', PostView.as_view(), name='post')
]
