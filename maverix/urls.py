
from django.conf.urls import include, url
from django.contrib import admin
from account.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('weather.urls')),
    url(r'^login/', login_view, name='login'),
  ]
