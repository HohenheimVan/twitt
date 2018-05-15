"""twitter URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from twitter_app.views import IndexView, AddTwittView, UserView, ContentDetailsView, MessagesView, LoginView, \
    RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^add_twitt/$', AddTwittView.as_view(), name='add-twitt'),
    url(r'^user/(?P<user_id>(\d)+)$', UserView.as_view(), name='user'),
    url(r'^content/$', ContentDetailsView.as_view(), name='content'),
    url(r'messages/$', MessagesView.as_view(), name='messages'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'register/$', RegisterView.as_view(), name='register'),


]
